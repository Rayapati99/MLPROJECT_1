
import pandas as pd
import numpy as np
from flask import Flask,render_template,request,jsonify
from src.logger import logging
import dill
from src.utills import save_object,load_object
from src.pipeline.predict_pipeline import Predictpipeline,CustomData
from src.pipeline import train_pipeline
import sys
from src.exception import CustomException

application=Flask(__name__)
app=application

@app.route('/')
def index():
    return "Welcome home page"

@app.route('/predict',methods=['GET','POST'])
def predict_data():
    try:
        if request.method=='GET':
            return render_template('home.html')
        else:
            
            data=CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('race_ethnicity'),
                reading_score=request.form.get('reading_score'),
                writing_score=request.form.get('writing_score'),
                lunch=request.form.get('lunch'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                test_preparation_course=request.form.get('test_preparation_course')
                )
            df=data.get_data_as_dataframe()
            processor=Predictpipeline()
            results=processor.predict(df)
            return render_template('home.html',results=round(results[0],2))
    except Exception as e:
        raise CustomException(e,sys)
    
@app.route('/predict_API',methods=['POST'])
def predict_api():
    try:
        if request.method=='POST':
            data=CustomData(
                gender=request.json['gender'],
                race_ethnicity=request.json['race_ethnicity'],
                reading_score=float(request.json['reading_score']),
                writing_score=float(request.json['writing_score']),
                lunch=request.json['lunch'],
                parental_level_of_education=request.json['parental_level_of_education'],
                test_preparation_course=request.json['test_preparation_course']
                )
            df=data.get_data_as_dataframe()
            processor=Predictpipeline()
            pred_score=processor.predict(df)
            dct = {'price':round(pred_score[0],2)}
            return jsonify(dct)

        
            
    except Exception as e:
        raise CustomException(e,sys)
        
    
    




if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)
    
        
    