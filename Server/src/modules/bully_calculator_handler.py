from Server.src.modules.db_handler import MongoHandler
from Server.src.modules.user_latest_tweets import get_user_time_line

IS_SCREEN_NAME = True
TWEETS_COUNT = 100

caching_mongo_client = MongoHandler().get_caching_mongo_client()


def calculate_bully_score(user):
    timeline = get_user_time_line(IS_SCREEN_NAME, user, TWEETS_COUNT)
    bully_counter = 0
    non_bully_counter = 0
    cached_tweets = []
    calculated_tweets = []
    for tweet in timeline:
        print(tweet)
        result = caching_mongo_client.find_one({"tweet_id": tweet.id_str}, {'_id': False})
        if not result:
            result = {  # TODO: replace with model
                "tweet_id": tweet.id_str,
                "tweet_message": tweet.full_text,
                "is_bully": True
            }
            calculated_tweets.append(result)
        else:
            cached_tweets.append(result)

        if result.get("is_bully"):
            bully_counter = bully_counter + 1
        else:
            non_bully_counter = non_bully_counter + 1

    if calculated_tweets:
        caching_mongo_client.insert_many(calculated_tweets)
    return {
        "score": bully_counter / (bully_counter + non_bully_counter),
        "tweets": cached_tweets + calculated_tweets
    }
