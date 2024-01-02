import os
import sys
import pandas as pd
import numpy as np
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from src.utills import save_object

@dataclass
class datatransformationconfig:
    processing_obj_file_path=os.path.join('artifacts','processor.pkl')
    
class getting_datatransformation_object:
    def __init__(self):
        self.data_preprocessing_obj=datatransformationconfig()
        
    def getting_data_trsformation(self):
        "This function is responsible for getting transformation object"
        try:
            
            numeric_columns=['reading_score', 'writing_score']
            categorical_columns=[
                'gender',
                'race_ethnicity', 
                'parental_level_of_education', 
                'lunch',
                'test_preparation_course'
                             ]
            numeric_pipeline=Pipeline(
                steps=[
                    ('scaler',SimpleImputer(strategy='median')),
                    ('standardscaler',StandardScaler(with_mean=False))
                    ]
                )
            categorical_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('encoding',OneHotEncoder()),
                    ('scaling',StandardScaler(with_mean=False))
                    ]
                )
            logging.info(f"categorical_columns: {categorical_columns}")
            logging.info('numeric_columns: {}'.format(numeric_columns))
            preprocessor=ColumnTransformer(
                transformers=[
                    ('num_pipeline',numeric_pipeline,numeric_columns),
                    ('cat_pipeline',categorical_pipeline,categorical_columns)
                ]
        
                )
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
        
    def intiative_data_transformation(self,train_path,test_path):
        logging.info('applying proprocessing object')
        
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            logging.info('Read train and test data is completed')
            logging.info('obtaining processing object')
            preprocessing_obj=self.getting_data_trsformation()
            target_column=['math_score']
            numeric_columns=['reading_score', 'writing_score']
            categorical_columns=[
                'gender',
                'race_ethnicity', 
                'parental_level_of_education', 
                'lunch',
                'test_preparation_course'
                ]
            input_train_df=train_df.drop(columns=['math_score'],axis=1)
            input_train_target_df=train_df['math_score']
            input_test_df=test_df.drop(columns=["math_score"],axis=1)
            input_test_target_df=test_df['math_score']
            input_train_arr=preprocessing_obj.fit_transform(input_train_df)
            input_test_arr=preprocessing_obj.transform(input_test_df)
            
            train_arr=np.c_[input_train_arr,np.array(input_train_target_df)]
            test_arr=np.c_[input_test_arr,np.array(input_test_target_df)]
            
            logging.info('processing.pkl file got saved!')
            save_object(
                file_path=self.data_preprocessing_obj.processing_obj_file_path,
                obj=preprocessing_obj
            )
            return(
                train_arr,
                test_arr,
                self.data_preprocessing_obj.processing_obj_file_path
            )
            
            
        except Exception as e:
            raise CustomException(e,sys)
    
 
        
        
        
        