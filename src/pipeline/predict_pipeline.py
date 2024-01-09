import dill
import sys
from src.logger import logging
from src.exception import CustomException
from src.utills import load_object,save_object
import pandas as pd
import os

class Predictpipeline:
    def __init__(self):
        pass
    def predict(self,features):
        try:
            
            model_path=os.path.join("artifacts","model.pkl")
            processor_path=os.path.join("artifacts","processor.pkl")
            model=load_object(file_path=model_path)
            processor=load_object(file_path=processor_path)
            scaled_df=processor.transform(features)
            pred=model.predict(scaled_df)
            return pred
        except Exception as e:
            logging.info('Exception occured in prediction pipeline')
            raise CustomException(e,sys)

class CustomData:
        def __init__(self,
                    gender:str,
                    race_ethnicity:str,
                    parental_level_of_education:str,
                    lunch:str,
                    test_preparation_course:str,
                    reading_score:int,
                    writing_score:int):
            
            
            self.gender=gender
            self.race_ethnicity=race_ethnicity
            self.parental_level_of_education=parental_level_of_education
            self.lunch=lunch
            self.test_preparation_course=test_preparation_course
            self.reading_score=reading_score
            self.writing_score=writing_score
            
        def get_data_as_dataframe(self):
            try:
                
                custom_data_input_dict={
                    'gender':[self.gender],
                    'race_ethnicity':[self.race_ethnicity],
                    'parental_level_of_education':[self.parental_level_of_education],
                    'lunch':[self.lunch],
                    'test_preparation_course':[self.test_preparation_course],
                    "reading_score":[self.reading_score],
                    'writing_score':[self.writing_score]
                }
                
                data=pd.DataFrame(custom_data_input_dict)
                print(data)
                logging.info('Data Frame gathered')
                return data
            except Exception as e:
                raise CustomException(e,sys)
            
            
        
            
    
    