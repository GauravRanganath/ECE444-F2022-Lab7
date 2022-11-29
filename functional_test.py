import pytest
from application import application
import json

test_cases = [
    ("Donald Trump was the president of the United States", {
     'prediction': 0, 'text': 'Donald Trump was the president of the United States'}),
    ("Jupiter has been destroyed by a nuclear missle",
     {'prediction': 1, 'text': 'Jupiter has been destroyed by a nuclear missle'}),
    ("The Avengers movie came out in the year 2012",
     {'prediction': 0, 'text': 'The Avengers movie came out in the year 2012'}),
    ("Thor invents thunder",
     {'prediction': 1, 'text': 'Thor invents thunder'})
]


@pytest.mark.nondestructive
@pytest.mark.parametrize("test_input, expected", test_cases)
def test_predict(test_input, expected):
    response = application.test_client().get(
        '/predict?text=' + test_input)
    res = json.loads(response.data.decode('utf-8'))
    assert (res == expected)
