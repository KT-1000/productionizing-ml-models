import json
import logging
from flask import Flask,render_template,url_for,request,Response
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib

app = Flask(__name__)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

@app.route('/predict',methods=['POST'])
def predict():
    cv = CountVectorizer()
	{{cookiecutter.model_name}} = open('./data/{{cookiecutter.model_name}}.pkl','rb')
	clf = joblib.load({{cookiecutter.model_name}})

	message = request.form['message']
	data = [message]
	vect = cv.transform(data).toarray()
    prediction = clf.predict(vect)

    return jsonify(prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
