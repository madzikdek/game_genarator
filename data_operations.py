import numpy as np
from pandas import DataFrame
import pandas as pd
import random


def import_csv(path: str) -> DataFrame:
    df=pd.read_csv('data.csv')
    #df.interpolate(method='pad')

    df_length = df.shape[0]
    # random_dict = {}
    #---------
    for column in df.columns:
        for count, single_index in enumerate(df[column]):
            if single_index==np.NaN:
                index = random.randint(0, count-2)
                df[column][count]=df[column][index]

        # random_dict[column] = df[column][index]

    return df
