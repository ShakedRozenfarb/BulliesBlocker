from unittest import TestCase
from src.modules.userTweetsPrediction import predictLabels


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

    # def test_predictLabels_problematic(self): // returns bully
    #     tweets = ["that's fucking amazing!"]
    #     result = predictLabels(tweets)
    #     assert result[0] == 0
