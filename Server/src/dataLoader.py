import json
import numpy as np
from nltk.tokenize import word_tokenize
import re

tweets_json = []
token_to_id = {}
tokenize_tweets = []
labels = []

for line in open('Dataset for Detection of Cyber-Trolls.json', 'r'):
    tweets_json.append(json.loads(line))

for tweet in tweets_json:
    tokenize_tweets.append(word_tokenize(tweet['content']))
    labels.append(tweet['annotation']['label'][0])

max_tweet = max(len(l) for l in tokenize_tweets)
tweets = np.empty((tokenize_tweets.__len__(), max_tweet), dtype=int)
tokens_counter = 1

for tweet, i in zip(tokenize_tweets, range(len(tokenize_tweets))):
    tokens_id_arr = []
    tmp_tokens = []

    for token in tweet:
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|' \
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', token)
        token = re.sub("(@[A-Za-z0-9_]+)", "", token)
        if len(token) > 0:
            token_lower = token.lower()
            if token_lower not in token_to_id:
                token_to_id[token_lower] = tokens_counter
                tokens_counter += 1
            tmp_tokens.append(token_to_id.get(token_lower))

    tweet_len = len(tmp_tokens)
    if (tweet_len < max_tweet):
        zeros = list(np.zeros(max_tweet - tweet_len))
        tweets[i] = np.array(zeros + tmp_tokens)
    else:
        tweets[i] = np.array(tmp_tokens)

print(tokenize_tweets)
print(tweets)
print(labels)