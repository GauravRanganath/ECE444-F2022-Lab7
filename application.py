from flask import Flask, request, json, jsonify

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

application = Flask(__name__)

loaded_model = None
with open('basic_classifier.pkl', 'rb') as fid:
    loaded_model = pickle.load(fid)

vectorizer = None
with open('count_vectorizer.pkl', 'rb') as vd:
    vectorizer = pickle.load(vd)


@application.route('/')
def home():
    return "<h1>Lab 7</h1>"


@application.route('/predict', methods=['GET'])
def predict():
    text = request.args.get('text')

    if text is None:
        resp = jsonify({'error': 'No input text specified to predict result.'})
        resp.status_code = 400
        return resp
    else:
        output = loaded_model.predict(vectorizer.transform([text]))[0]
        prediction = 0 if output == "REAL" else 1

    return {'text': text, 'prediction': prediction}


if __name__ == '__main__':
    application.run()
