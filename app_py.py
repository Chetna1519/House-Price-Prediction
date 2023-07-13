# -*- coding: utf-8 -*-
"""app.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1itcqoBXNMjW4YuAjESSnl_F317W_e21Q
"""

from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
import datetime as dt

app = Flask(__name__, template_folder = 'templates')

data = pd.read_csv("/content/Dataset of House Price Prediction.csv")

model = pickle.load(open("model_rf.pkl",'rb'))

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/predict", methods = ['POST','GET'])
def predict():
   Sqft_living = request.form.get('sqft_living')
   Sqft_Area = request.form.get("sqft_lot")
   Sqft_above = request.form.get('sqft_above')
   Sqft_basement = request.form.get('sqft_basement')
   No_of_floors = request.form.get("floors")
   No_of_Bedrooms = request.form.get('bedrooms')
   waterfront = request.form.get('waterfront')
   view = int(2)
   condition = int(3)
   year_build = request.form.get('yr_built')
   year_renovated = request.form.get('yr_renovated')
   city = int(35)
   zip = int(98103)
   year = datetime.datetime.now().year

   features = np.array([Sqft_living,Sqft_Area, Sqft_above, Sqft_basement, No_of_floors, No_of_Bedrooms,waterfront,view, condition, year, city, zip, year_build, year_renovated]).reshape(1,-1)
   prediction = model.predict(features)
   price = prediction * 345.6

   return render_template('index.html', result = np.round(price,2))

if __name__  ==  '__main__':
  app.run(host = "0.0.0.0", port = 8008, debug = True)