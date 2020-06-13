from tweepy import OAuthHandler, API, Cursor
from Server.src.modules import twitter_api_config

auth = OAuthHandler(twitter_api_config.consumer_key, twitter_api_config.consumer_secret)
auth.set_access_token(twitter_api_config.access_token, twitter_api_config.access_token_secret)
auth_api = API(auth)

user_tweets = []


def get_user_time_line(is_screen_name, user, count):
    user_tweets.clear()
    if is_screen_name:
        return Cursor(auth_api.user_timeline,
                      screen_name=user,
                      include_rts=False,
                      tweet_mode='extended'
                      ).items(count)

    return Cursor(auth_api.user_timeline,
                  user_id=user,
                  include_rts=False,
                  tweet_mode='extended'
                  ).items(count)


''' 
# usage example
# get 20 recent tweets of BarackObama by his twitter 'screen name'

user_time_line = get_user_time_line(True, 'BarackObama', 20)

for tweet in user_time_line:
    print(tweet._json.get('full_text'))

'''

