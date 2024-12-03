from decimal import *
import pandas as pd
import numpy as np


def create_df(init_data):
    df = pd.DataFrame(init_data)
    print(df)
    return df


def df_to_list():
    data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
            'year': [2000, 2001, 2002, 2001, 2002, 2003],
            'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
    frame = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'])
    frame = frame.reset_index(drop=True)

    print(frame)
    df = frame.drop(columns=['debt', 'year', 'a'], errors='ignore')
    print(df)
    print(frame.columns.values.tolist())
    print(frame.to_numpy().tolist())


if __name__ == '__main__':

    ...

