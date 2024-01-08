from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import getting_datatransformation_object
from src.components.model_trainer import modeltrainer
from src.utills import save_object,load_object

# if __name__=="__main__":
#     obj=DataIngestion()
#     train_path,test_path=obj.DataIngestionInitiated()
#     object2=getting_datatransformation_object()
#     train_arr,test_arr,_=object2.intiative_data_transformation(train_path,test_path)
    
#     object3=modeltrainer()
#     object3.initative_modeltrainer(train_arr,test_arr)