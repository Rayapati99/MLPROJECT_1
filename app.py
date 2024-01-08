
import pandas as pd
import numpy as np
from flask import Flask,render_template,request
from src.logger import logging
from src.exception import logging
import dill
from src.utills import save_object,load_object
import sys

application=Flask(__name__)
app=application

@app.route('/')
def index():
    return "Welcome home page"

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)
    
        
    