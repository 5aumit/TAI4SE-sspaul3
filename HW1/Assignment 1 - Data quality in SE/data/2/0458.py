import typing as t
import typing_extensions as te

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import datetime
import os
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import TimeSeriesSplit, cross_validate
from sklearn.base import BaseEstimator, TransformerMixin, RegressorMixin
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.model_selection import TimeSeriesSplit, cross_validate
from sklearn.metrics import make_scorer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV

class DatasetReader(te.Protocol):
      def __call__(self) -> pd.DataFrame:
          ...


SplitName = te.Literal["train", "test"]


def get_dataset(reader: DatasetReader, splits: t.Iterable[SplitName]):
    df = reader()
    df = clean_dataset(df)
    y = df["cnt"]
    X = df[['season', 'holiday', 'weekday', 'workingday', 'weathersit','temp', 
    'atemp', 'hum', 'windspeed', 'Yesterday', 'diff']]
    
    X_train = df[:'2011'].drop(['cnt'], axis=1)
    y_train = df.loc[:'2011','cnt']
    X_test = df['2012'].drop(['cnt'], axis=1)
    y_test = df.loc['2012','cnt']

    split_mapping = {"train": (X_train, y_train), "test": (X_test, y_test)}
    return {k: split_mapping[k] for k in splits}


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
     cleaning_fn = _chain(
         [
             _fix_drop_instant,
             _fix_datetime,
             _fix_dias_faltantes,
             _fix_organize_by_days,
             _fix_add_yesterday

         ]
     )
     df = cleaning_fn(df)
     return df


def _chain(functions: t.List[t.Callable[[pd.DataFrame], pd.DataFrame]]):
     def helper(df):
         for fn in functions:
             df = fn(df)
         return df

     return helper


def _fix_drop_instant(df):
    df = df.drop(columns='instant', axis=1)
    return df

def _fix_datetime(df):
    df['dteday'] = df['dteday'].astype('str')
    df['hour'] = df['hr'].astype('str')+':00'
    df['Datetime'] = df['dteday']+' '+df['hour']
    df['Datetime'] = pd.to_datetime(df['Datetime'])
    df = df.set_index('Datetime')
    return df


def _fix_dias_faltantes(df):
    df = df.asfreq(freq='60min', method='ffill')
    return df

def _fix_organize_by_days(df):
    df['day'] = df.index.day_name()
    feature_columns_1 = ['day','season', 'holiday', 'weekday',
         'workingday', 'weathersit', 'temp', 'atemp', 'hum', 'windspeed','cnt'
          ]
    df = df[feature_columns_1].resample('D').mean()
    return df

def _fix_add_yesterday(df):
    df = df[['cnt','season', 'holiday', 'weekday',
         'workingday', 'weathersit', 'temp', 'atemp', 'hum', 'windspeed']]
    df.loc[:,'Yesterday'] = df.loc[:,'cnt'].shift()
    df.loc[:,'diff'] = df.loc[:,'Yesterday'].diff()
    df = df.dropna()
    return df

