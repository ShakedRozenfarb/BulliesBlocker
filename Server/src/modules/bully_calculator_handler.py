from cachetools.func import ttl_cache

from Server.src.modules.db_handler import MongoHandler
from Server.src.modules.user_latest_tweets import get_user_time_line
from Server.src.modules.userTweetsPrediction import predictLabels
IS_SCREEN_NAME = True
TWEETS_COUNT = 100

caching_mongo_client = MongoHandler().get_caching_mongo_client()


@ttl_cache()
def calculate_bully_score(user):
    timeline = get_user_time_line(IS_SCREEN_NAME, user, TWEETS_COUNT)
    bully_counter = 0
    undefined_counter = 0
    non_bully_counter = 0
    cached_tweets = []
    tweets_to_calculate = []
    for tweet in timeline:
        result = caching_mongo_client.find_one({"tweet_id": tweet.id_str}, {'_id': False})
        if not result:
            result = {
                "tweet_id": tweet.id_str,
                "tweet_message": tweet.full_text,
                "tweet_date": tweet.created_at
            }
            tweets_to_calculate.append(result)
        else:
            cached_tweets.append(result)

    tweets_messages_to_calculate = [tweet_to_calculate["tweet_message"] for tweet_to_calculate in tweets_to_calculate]

    if tweets_to_calculate:
        tweets_result = predictLabels(tweets_messages_to_calculate)
        for index in range(len(tweets_to_calculate)):
            if tweets_result[index] == 0:
                tweets_to_calculate[index]["is_bully"] = False
            elif tweets_result[index] == 1:
                tweets_to_calculate[index]["is_bully"] = True
            else:
                tweets_to_calculate[index]["is_bully"] = "undefined"
        caching_mongo_client.insert_many(tweets_to_calculate)

    all_tweets = cached_tweets + tweets_to_calculate
    for tweet in all_tweets:
        if tweet.get("_id"):
            del tweet["_id"]
        tweet_result = tweet.get("is_bully")
        if tweet_result == "undefined":
            undefined_counter = undefined_counter + 1
        elif tweet_result:
            bully_counter = bully_counter + 1
        else:
            non_bully_counter = non_bully_counter + 1

    return {
        "score": bully_counter / (bully_counter + non_bully_counter),
        "tweets": all_tweets,
        "undefined": undefined_counter
    }
