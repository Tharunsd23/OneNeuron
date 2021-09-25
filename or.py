from utils.model import Perceptron
from utils.all_utils import prepare_data,save_plot,save_model
import pandas as pd
import numpy as np
import logging
import os
logging_str = "[%(asctime)s: %(levelname)s: %(module)s] %(message)s"
logging.basicConfig(level=logging.INFO,format=logging_str)
log_dir = "logss"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename= os.path.join(log_dir,"running_logs.log"),level=logging.INFO, format=logging_str, filemode="a")

def main(data,eta, modelName, epochs,plotName):

    df= pd.DataFrame(data)
    logging.info(f"This is actual dataframe{df}")

    X,y = prepare_data(df)
   

    model = Perceptron(eta,epochs)
    model.fit(X,y)
    _= model.total_loss()

    save_model(model,filename=modelName)
    save_plot(df,plotName,model)

if __name__ == '__main__':
   
    OR= {
        "x1": [0,0,1,1],
        "x2": [0,1,0,1],
        "y": [0,1,1,1],
    }
    ETA = 0.3
    EPOCHS = 10
    try:
        logging.info(">>>>> starting training >>>>>")
        main(data=OR, modelName="or.model", plotName="or.png", eta=ETA, epochs=EPOCHS)
        logging.info("<<<<< training done successfully<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e
   