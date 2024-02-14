import os,sys
from datetime import datetime

def get_current_time_strap():
    return f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}"

CURRENT_TIME_STRAP = get_current_time_strap()

ROOT_DIR_KEY = os.getcwd()
DATA_DIR ="data"
DATA_DIR_KEY = "finalTrain.csv"

ARTIFACT_DIR_KEY = "Artifact"

# DATA INGESION VARIABLES
DATA_INGESTION_KEY = "data_ingesion"
DATA_INGESTION_RAW_DATA_DIR = "raw_data_dir"
DATA_INGESTION_INGESTED_DATA_DIR_KEY = "ingested_dir"
RAW_DATA_DIR_KEY = "raw.csv"
TRAIN_DATA_DIR_KEY = "train.csv"
TEST_DATA_DIR_KEY = "test.csv"

#DATA TRANSFORMATION VARIABLES
DATA_TRANSFORMATION_ARTIFACT = "data_transformation"
DATA_PREPROCESSED_DIR = "processor"
DATA_TRANSFORMTION_PROCESSING_OBJ = "processor.pkl"
DATA_TRANSFORM_DIR = "transformation"
TRANSFORM_TRAIN_DIR_KEY = "train.csv"
TRANSFORM_TEST_DIR_KEY = "test.csv"