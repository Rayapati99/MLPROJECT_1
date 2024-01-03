import pandas as pd
import numpy as np
import os
import sys
import dill
from src.exception import CustomException
from src.logger import logging
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV



def save_object(file_path,obj):
    try:
        dir_name=os.path.dirname(file_path)
        os.makedirs(dir_name,exist_ok=True)
        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)
    except CustomException as e:
        raise CustomException(e,sys)
    
    
def evaluate_models(X_train,y_train,X_test,y_test,models,params):
    try:
        report={}
        for i in range(len(list(models))):
            model=list(models.values())[i]
            para=params[list(models.keys())[i]]
            #model.fit(X_train,y_train) ## train model
            gs=GridSearchCV(model,para,cv=5)
            gs.fit(X_train,y_train)
            model.set_params(**gs.best_params_)
            logging.info('best parameters'.format(**gs.best_params_))
            model.fit(X_train,y_train)
            y_train_predict=model.predict(X_train)
            y_test_predict=model.predict(X_test)
            train_model_scores=r2_score(y_train,y_train_predict)
            test_model_scores=r2_score(y_test,y_test_predict)
            report[list(models.keys())[i]]=test_model_scores
        return report
    
            
    except Exception as e:
        raise CustomException(e,sys)
