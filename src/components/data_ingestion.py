from src.exception import CustomException
from src.logger import logging
import os
import sys
import pandas as pd
from dataclasses import dataclass

from sklearn.model_selection import train_test_split
from src.components.data_transformation import datatransformationconfig,getting_datatransformation_object

from src.components.model_trainer import modeltrainer
@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train_data')
    test_data_path:str=os.path.join('artifacts','test_data')
    raw_data_path:str=os.path.join('artifacts','data')
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    
    def DataIngestionInitiated(self):
        logging.info('DataIngestionInitiated just now!')
        try:
             
             df=pd.read_csv('notebook\data\stud.csv')
             logging.info('Read the dataset as data frame')
             os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
             
             df.to_csv(self.ingestion_config.raw_data_path,header=True,index=False)
             logging.info('Spliting Dataset into Train data,test data  just now initiated!')
             train_data,test_data=train_test_split(df,test_size=0.2,random_state=42)
             train_data.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
             test_data.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
             logging.info('Data ingestion stage just now completed')
             return(
                 self.ingestion_config.train_data_path,
                 self.ingestion_config.test_data_path
                 )
        except Exception as e:
            raise CustomException(e,sys)
        
        
            
       
    
    
if __name__=="__main__":
    obj=DataIngestion()
    train_path,test_path=obj.DataIngestionInitiated()
    object2=getting_datatransformation_object()
    train_arr,test_arr,_=object2.intiative_data_transformation(train_path,test_path)
    
    object3=modeltrainer()
    object3.initative_modeltrainer(train_arr,test_arr)