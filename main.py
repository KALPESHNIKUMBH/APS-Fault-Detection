#1
from sensor.logger import logging
from sensor.exception import SensorException
from sensor.utils.__init__ import get_collection_as_dataframe
import sys,os
'''
def test_logger_and_exception():
    try:
        logging.info("starting the test logger and exception")
        result = 3/0
        print(result)
        logging.info("stoping the test logger and exception")
    except Exception as e:
        logging.debug("stoping the test logger and exception")
        raise SensorException(e, sys)
'''

if __name__ == "__main__":
    try:
        get_collection_as_dataframe(database_name="aps",collection_name="sensor")
    except Exception as e:
        print(e)






'''
import os,sys
from sensor.exception import SensorException
from sensor.logger import logging
from datetime import datetime
from sensor.utils import get_collection_as_dataframe
from sensor.entity.config_entity import DataIngestionConfig
from sensor.entity import config_entity
from sensor.components import data_ingestion



if __name__=="__main__":
    try:
        training_pipeline_config = config_entity.TrainingPipelineConfig()
        data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        print(data_ingestion_config.to_dict())
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        print(data_ingestion.initiate_data_ingestion())
    except Exception as e:
        print(e)
'''