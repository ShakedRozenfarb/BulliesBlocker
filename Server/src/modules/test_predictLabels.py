from unittest import TestCase
from Server.src.modules.userTweetsPrediction import predictLabels


class TestPredictLabels(TestCase):
    def test_predictLabels_notBully(self):
        tweets = ["hi, how are you?"]
        result = predictLabels(tweets)
        assert result[0] == 0

    def test_predictLabels_bully(self):
        tweets = ["fuck you"]
        result = predictLabels(tweets)
        assert result[0] == 1

    def test_predictLabels_bully(self):
        tweets = ["fuck you", "hi how are you?"]
        result = predictLabels(tweets)
        assert result[0] == 1
        assert result[1] == 0

    def test_predictLabels_undefined(self):
         tweets = ["Text 'FLOYD' to 55156 #BlackLivesMatters #JusticeForGeorgeFloyd #JusticeforAhmaudArbery #JusticeforBreonnaTaylor"]
         result = predictLabels(tweets)
         assert result[0] == 2
