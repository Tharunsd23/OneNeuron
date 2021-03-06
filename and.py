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
def main(data,eta, epochs,filename):

    df= pd.DataFrame(data)
    logging.info(f"This is actual dataframe{df}")

    X,y = prepare_data(df)
   

    model = Perceptron(eta,epochs)
    model.fit(X,y)
    _= model.total_loss()

    save_model(model,filename)
    save_plot(df,"and.png",model)

if __name__ == '__main__':
   
    AND = {
        "x1": [0,0,1,1],
        "x2": [0,1,0,1],
        "y": [0,0,0,1],
    }
    ETA = 0.3
    EPOCHS = 10
    main(data=AND,eta=ETA,epochs=EPOCHS,filename="and.model")
