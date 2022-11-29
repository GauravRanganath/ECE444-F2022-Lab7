import pytest
from application import application
import json
import requests

test_cases = [
    ("Donald Trump was the president of the United States", {
     'prediction': 0, 'text': 'Donald Trump was the president of the United States'}),
    ("Jupiter has been destroyed by a nuclear missile",
     {'prediction': 1, 'text': 'Jupiter has been destroyed by a nuclear missile'}),
    ("The Avengers movie came out in the year 2012",
     {'prediction': 0, 'text': 'The Avengers movie came out in the year 2012'}),
    ("Thor invents thunder",
     {'prediction': 1, 'text': 'Thor invents thunder'})
]


@pytest.mark.nondestructive
@pytest.mark.parametrize("test_input, expected", test_cases)
def test_predict(test_input, expected):
    response = requests.get(
        "http://lab7-env-2.eba-2ipmbe9n.us-east-1.elasticbeanstalk.com/predict?text=" + test_input)
    response_body = response.json()
    assert (response_body == expected)
