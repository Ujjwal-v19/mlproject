import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"   #strftime stands for "string format time".
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)              # it create a path  by joining all like :C/mlprojects/logs/26_Jan_2025.log 
os.makedirs(logs_path,exist_ok=True)                             # it create a directory acc to path given 

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


# if __name__ == "__main__":
#     logging.info("Logging has Started")