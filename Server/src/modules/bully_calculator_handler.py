from Api.flask_app.db_handler.db_handler import MongoHandler
from Server.src.userLatestTweets import get_user_time_line

IS_SCREEN_NAME = True
TWEETS_COUNT = 100

caching_mongo_client = MongoHandler().get_caching_mongo_client()


def calculate_bully_score(user):
    timeline = get_user_time_line(IS_SCREEN_NAME, user, TWEETS_COUNT)
    first_tweet = timeline.next()
    cached_result = caching_mongo_client.find_one({"tweet_id": first_tweet["id"]})
    if cached_result:
        return cached_result["score"], "Score was received from cache"
    timeline.prev()
    # TODO: send to model for calculation
