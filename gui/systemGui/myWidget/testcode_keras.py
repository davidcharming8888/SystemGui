import pandas as pd
from method.lstm.prediction import ModelLSTM
from numpy import concatenate
import numpy as np
df = pd.read_csv(r'D:\chaos\jobless\keras\Forcast_Fault\data\4year\seldata1_nset_4year.csv', index_col=0)
df = df.iloc[1000:1005, :]


pred = ModelLSTM.pred(df)
pred = concatenate((pred,np.array([[0]]))   )
df['pred'] = pred
print(df.head())
