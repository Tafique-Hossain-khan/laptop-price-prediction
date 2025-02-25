from src.components.data_transformation import DataTransformation,DataTransformationConfig
from src.components.model_traner import ModelTraner,ModelTranerConfig
from src.components.data_injection import DataInjection

from src.pipeline.prediction_pipeling import CustomInputLaptop,PredictPipeline 

from src.utils import load_object
from src.logger import logging
from src.exception import CustomException
import os
import sys


if __name__ == "__main__":

    try:
        di = DataInjection()
        raw_data_path,train_data_path,test_data_path = di.initai_data_injection()


        dt = DataTransformation()
        #obj_path = dt.get_data_transformation_obj()
        train_data ,test_data =dt.initiate_data_transformation(train_data_path,test_data_path)

        mr = ModelTraner()
        mr.model_traner(train_data,test_data)



        ci = CustomInputLaptop('Apple',	'Ultrabook',	8,	1.37,	0,	1	,226.983005,	'Intel Core i5',	0,	128,	'Intel',	'Mac')
        df = ci.custom_dataset()
        logging.info(df)
        '''
        pred = PredictPipeline()
        pred.predict(df)
        '''
        preprocessor = load_object('artifacts\preprocessor_laptop.pkl') 
    
        model = load_object('artifacts\model_laptop.pkl')

        scaled_data = preprocessor.transform(df)
        predtion = model.predict(scaled_data)
        
        

    except Exception as e:
        raise CustomException(e,sys)