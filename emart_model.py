import datetime
import pandas as pd
import joblib
from keras.models import load_model
from db_manage import EMART_DB
import numpy as np

# import os
# SCALEPATH = os.environ['SCALEPATH']
# DI_ENCODER = os.environ['DI_ENCODER']
# LO_ENCODER = os.environ['LO_ENCODER']
# PRETRAINED = os.environ['PRETRAINED']


SCALEPATH="C:/EMART/fastml/pickles/minmaxscaler.pkl"
DI_ENCODER="C:/EMART/fastml/pickles/division_encoder.pkl"
LO_ENCODER="C:/EMART/fastml/pickles/location_encoder.pkl"
PRETRAINED="C:/EMART/fastml/pretrained/chkpoint.h5"

class EMART:
    def __init__(self):
        self.msgbox = dict(
            path = 'Please input the path, where\'s the model weight saved',
            model = 'please make the model first',
            data = 'input the data and follow the schema',
            maximum_date = 'Over the Maximum',
            pretrained_path = 'Wrong path to get a model parameter. please try again by using the method \'getmodel()\'',
            row_schema = 'please check the schema. the length of data should be 7'
            )
        self.year = 2021 # 어떤 년도부터
        self.days = 365 # 며칠 데이터를 가져올 건지
        self.__model = load_model(PRETRAINED)
        self.SEASON = None
        self.__SCALER = joblib.load(SCALEPATH)
        self.__DI_EN = joblib.load(DI_ENCODER)
        self.__LO_EN = joblib.load(LO_ENCODER)
        self.__DB = None
        SEASON = {}
        for i in range(1, 13):
            month = '%02d'%i
            SEASON[month] = (i)  // 3
        self.SEASON = SEASON


    def preprocessing(self, row):
        date, divi, loca = map(str, row[:3])
        year, month, day = int(date[:4]), int(date[4:6]), int(date[6:])
        if self.__DB == None:
            self.__DB = EMART_DB()
        db = self.__DB
        endtime = datetime.datetime(year = year, month = month, day = day)
        starttime = (endtime - datetime.timedelta(days = 7)).strftime('%Y%m%d')
        endtime = endtime.strftime('%Y%m%d')
        query = 'SELECT * FROM AIRINDEX WHERE DATE < %s and DATE > %s and DIVISION = \'%s\' and LOCATION = \'%s\''%(endtime, starttime, divi, loca)
        columns = ['MSRDT_DE','MSRRGN_NM','MSRSTE_NM','O3','NO2','CO','SO2']
        df = pd.DataFrame(db.select(query) + [row], columns= columns)
        df['MSRDT_DE'] = pd.to_datetime(df['MSRDT_DE'], format = '%Y%m%d')
        df['MONTH'] = df.MSRDT_DE.dt.strftime('%m')
        df['DAY'] = df.MSRDT_DE.dt.strftime('%d')
        df['WEEKDAY'] = df['MSRDT_DE'].dt.weekday
        
        df.drop('MSRDT_DE', axis = 1, inplace= True)
        df['SEASON'] = df['MONTH'].map(self.SEASON)
        df['MSRRGN_NM'] = self.__DI_EN.transform(df['MSRRGN_NM'])
        df['MSRSTE_NM'] = self.__LO_EN.transform(df['MSRSTE_NM'])
        scaler = self.__SCALER
        cs = ['W_0', 'W_1', 'W_2', 'W_3', 'W_4', 'W_5', 'W_6']
        df = pd.concat([df, pd.get_dummies(df.WEEKDAY, prefix='W')[cs]], axis = 1).drop('WEEKDAY', axis = 1)
        X = scaler.transform(df)
        
        return X

    def inference(self, row):
        assert len(row) == 7, self.msgbox['row_schema']
        model = self.__model
        X = self.preprocessing(row)
        y = model.predict(np.expand_dims(X, axis = 0))[0]
        return {'PM10' : str(y[0]), 'PM25' : str(y[1])}