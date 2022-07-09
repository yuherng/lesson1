from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from joblib import load
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    request_type_str = request.method
    if request_type_str == 'GET':
        return render_template('index.html', href2='static/none.png', href3='')
    else:
        myage = request.form['age']
        mygender = request.form['gender']
        mybread = ''
        if str(myage) =='' or str(mygender) =='':
            return render_template('index.html', href2='static/none.png', href3='Please insert your age and gender.')
        else:
            model = load('app/bread-recommender.joblib')
            np_arr = np.array([myage, mygender])
            predictions = model.predict([np_arr])  
            predictions_to_str = str(predictions)
            
            if 'donut' in predictions_to_str:
                mybread = 'static/donut.png'
            elif 'croissant' in predictions_to_str:
                mybread = 'static/croissant.png'
            elif 'whole grain' in predictions_to_str:
                mybread = 'static/wholegrain.png'
            elif 'wheat bread' in predictions_to_str:
                mybread = 'static/wheatbread.png'
            elif 'swiss roll' in predictions_to_str:
                mybread = 'static/swissroll.png'
            elif 'sandwich' in predictions_to_str:
                mybread = 'static/sandwich.png'
            else:
                mybread = 'static/none.png' 
                
            return render_template('index.html', href2=str(mybread), href3='The suitable bread for you (age:'+str(myage)+' ,gender:'+str(mygender)+') is:'+predictions_to_str)
        

