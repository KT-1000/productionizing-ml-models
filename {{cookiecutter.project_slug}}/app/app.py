from flask import Flask, request, Response
import json
import pandas as pd 
import pickle

app = Flask(__name__)

@app.route('/predict',methods=['POST'])
def predict():
	{{cookiecutter.project_slug}} = open('./data/{{cookiecutter.project_slug}}.pkl','rb')
	clf = joblib.load({{cookiecutter.project_slug}})

	message = request.get_json()
    json_input = {}
    data = [message]
    prediction = CHANGE
    json_input['prediction'] = prediction

    js = json.dumps(json_input)

    return Response(js, status=return_status, mimetype='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
