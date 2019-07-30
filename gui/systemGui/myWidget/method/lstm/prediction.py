from keras.models import load_model
from pandas import DataFrame,concat,read_csv
from sklearn.preprocessing import MinMaxScaler
from numpy import concatenate
from lstm_series import series_to_supervised
import numpy as np


# returns a compiled model
# identical to the previous one
class ModelLSTM():

    @classmethod
    def pred(cls,dataset):
        model = load_model(r'D:\chaos\jobless\keras\Forcast_Fault\model\lstm_1.h5')
        D = np.load(r"D:\chaos\jobless\keras\Forcast_Fault\model\D_1.npy")

        # load dataset
        values = dataset.values

        # ensure all data is float
        values = values.astype('float32')

        # split 10var and nset to scale
        values_y = values[:,0].reshape(-1,1)
        values_x = values[:,1:]
        # print(pd.DataFrame(values_x),'\n\n',pd.DataFrame(values_y))

        # use the normal D narry to normalize 10var
        scaler = MinMaxScaler(feature_range=(0, 1))
        scaler.fit(D)
        scaled_x = scaler.transform(values_x)
        scaled = concatenate((values_y,scaled_x), axis= 1)

        # frame as supervised learning
        reframed = series_to_supervised(scaled, 1, 1)
        drop = [i for i in range(13,24)]
        reframed.drop(reframed.columns[drop], axis=1, inplace=True)


        # split into train and test sets, values格式为 [时序]
        predict = reframed.values
        predict_X, real_y = predict[:, :-1], predict[:, -1]
        predict_X = predict_X.reshape((predict_X.shape[0], 1, predict_X.shape[1]))

        y_pred = model.predict(predict_X)
        return y_pred,real_y