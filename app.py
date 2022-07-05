import numpy as np
from flask import Flask, request, jsonify, render_template,send_from_directory
import pickle
import pandas as pd
import sqlite3
app = Flask(__name__)
from flask_cors import CORS
CORS(app)
import json

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/validate',methods=['POST'])
def validate():
    return render_template('validate.html')

@app.route('/index',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/success',methods=['POST'])
def success():
    return render_template('success.html')

@app.route('/sqlerror',methods=['GET', 'POST'])
def sqlerror():
    return render_template('sql-error.html')


@app.route('/predict',methods=['GET'])

def predict():
	'''
	For rendering results on HTML GUI
	'''
	model = pickle.load(open(r'model.pkl', 'rb'))
	vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
	#text = request.form.values()
	text = request.args.get('sentence')
	temp_df = pd.DataFrame({text})
	post = vectorizer.transform(temp_df[0]).toarray()
	output = model.predict(post)
	if output[0] == 1:
		flag = 'yes'
	else:
		flag = 'no'
	print("Input " + text + " Result " + flag)
	return flag


@app.route('/login',methods=['POST'])
def login():
	'''
	Authentication
	'''
	password_fetch = ''
	json = request.json
	email = json['email']
	password = json['password']
	conn = sqlite3.connect('./knowledgebase/project.db')
	cursor = conn.execute("SELECT password from accounts where name ='"+email+"'")
	for row in cursor:
		password_fetch = row[0]
		break
	if password==password_fetch:
		return "SUCCESS"
	else:
		return "FAIL"


if __name__ == "__main__":
    app.run(debug=True)
