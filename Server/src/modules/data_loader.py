import json
from nltk.tokenize import word_tokenize
import re
import torch
from torch.utils.data import TensorDataset, DataLoader
import numpy as np
#import src.modules.globalVariables as globalVar
import Server.src.modules.globalVariables as globalVar

threshold = 0.5
import Server.src.modules.globalVariables as globalVar


def shuffle(a, b):
    assert len(a) == len(b)
    p = np.random.permutation(len(a))
    return a[p], b[p]


def tokenize_data(max_tweet, tokenize_tweets, tokens_counter, isTrainMode, token_to_id):
    tweets = np.empty((tokenize_tweets.__len__(), max_tweet), dtype=int)
    outliers = []
    for tweet, i in zip(tokenize_tweets, range(len(tokenize_tweets))):
        tmp_tokens = []

        for token in tweet:
            token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|' \
                           '(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', token)
            token = re.sub("(@[A-Za-z0-9_]+)", "", token)
            if len(token) > 0:
                token_lower = token.lower()
                if token_lower not in token_to_id:
                    if isTrainMode:
                        token_to_id[token_lower] = tokens_counter
                        tokens_counter += 1
                        tmp_tokens.append(token_to_id.get(token_lower))
                    else:
                        tmp_tokens.append(0)
                else:
                    tmp_tokens.append(token_to_id.get(token_lower))

        if(tmp_tokens.count(0) + tmp_tokens.count(331))/len(tmp_tokens) > threshold: # if token is unknown or hashtag
            outliers.append(i)

        tweet_len = len(tmp_tokens)
        if (tweet_len < max_tweet):
            zeros = list(np.zeros(max_tweet - tweet_len))
            tweets[i] = np.array(zeros + tmp_tokens)
        else:
            tweets[i] = np.array(tmp_tokens)
    return tweets, outliers


def load_data():
    batch_size = 50
    tweets_json = []
    tokenize_tweets = []
    labels = np.empty((20001, 1), dtype=int)

    for line in open('Dataset for Detection of Cyber-Trolls.json', 'r'):
        tweets_json.append(json.loads(line))

    i = 0
    for tweet in tweets_json:
        tokenize_tweets.append(word_tokenize(tweet['content']))
        labels[i] = np.array(tweet['annotation']['label'][0])
        i += 1

    max_tweet = max(len(l) for l in tokenize_tweets)
    tokens_counter = 1
    token_to_id = {}
    tweets, ignore = tokenize_data(max_tweet, tokenize_tweets, tokens_counter, True, token_to_id)

    # shuffle fix_tweets and split the data to test data and train data
    tweets, labels = shuffle(tweets, labels)

    train_tweets = tweets[0:20000]
    train_classification = labels[0:20000]
    test_tweets = tweets[14000:20000]
    test_classification = labels[14000:20000]
    '''
     train_tweets = tweets[0:14000]
        train_classification = labels[0:14000]
        test_tweets = tweets[14000:20000]
        test_classification = labels[14000:20000]
    '''

    train_data = TensorDataset(torch.from_numpy(train_tweets), torch.from_numpy(train_classification))
    train_loader = DataLoader(train_data, shuffle=True, batch_size=batch_size)
    test_data = TensorDataset(torch.from_numpy(test_tweets), torch.from_numpy(test_classification))
    test_loader = DataLoader(test_data, shuffle=True, batch_size=batch_size)

    vocabulary_size = len(token_to_id) + 1

    print(tokenize_tweets)
    print(tweets)
    print(labels)
    print(type(labels[0]))

    torch.save(token_to_id, globalVar.tokenToIdFile)

    return train_loader, test_loader, vocabulary_size, batch_size
