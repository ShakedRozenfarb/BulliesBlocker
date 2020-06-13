import torch
from nltk import word_tokenize

from src.modules.data_loader import tokenize_data
import src.modules.globalVariables as globalVar


def predictLabels(user_tweets):
    tokenize_tweets = []

    token_to_id = torch.load(globalVar.tokenToIdFile)
    tokens_counter = len(token_to_id)+1
    for tweet in user_tweets:
        tokenize_tweets.append(word_tokenize(tweet))

    max_tweet = max(len(l) for l in tokenize_tweets)
    tokenize_tweets = tokenize_data(max_tweet, tokenize_tweets, tokens_counter, False, token_to_id)

    tokenize_tweets = torch.from_numpy(tokenize_tweets)
    net = torch.load(globalVar.modelFile)
    hidden = net.init_hidden(tokenize_tweets.__len__())
    hidden = tuple([each.data for each in hidden])
    inputs = tokenize_tweets.type(torch.LongTensor)

    outputs, hidden = net(inputs, hidden)
    predicted = torch.round(outputs)
    return predicted.tolist()