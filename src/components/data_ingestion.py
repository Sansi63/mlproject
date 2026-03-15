import os 
import sys
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split




@dataclass
class Data_ingestion_config:
    raw_data_path:str=os.path.join("artifacts",'data.csv')
    test_data_path:str=os.path.join("artifacts",'test.csv')
    train_data_path:str=os.path.join("artifacts",'train.csv')


class Data_ingestion:
    def __init__(self):
        self.ingestion_config=Data_ingestion_config()
    def  initiate_data_ingestion(self): 
        logging.info("Entered the data Ingestion Method")  
        try:
            df=pd.read_csv('notebook/data/stud.csv')
            
            logging.info('Train test split initiated')
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            
            logging.info('Train Test Split initiated')
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            logging.info('Ingestion of Data is completed')
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
                
            )
        except Exception as e:
            raise CustomException(e,sys)
     
if __name__=='__main__':
    obj=Data_ingestion()
    train_data,test_data=obj.initiate_data_ingestion()