"""data import and preprocessing"""
from __future__ import absolute_import

import os
import time

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

from data.download_data import download_data


# Constant variable
PATH = 'src/titanic.csv'

# Function definition
def get_data(path: str=PATH, graph: bool=False) -> pd.DataFrame:
    """Import (or download & import if not exist) the titanic data from local path

    Args:
        path (str, optional): The path to the csv file. Defaults to 'src/titanic.csv'.
        graph (bool, optional): Show the graphs or not. Defaults to False.

    Returns:
        pd.DataFrame: The ready to use DataFrame
    """
    start = time.time()
    print('# Retreiving data ...')

    if not os.path.exists(path):
        print(' - File not found. Downloading ...\n')
        download_data()

    # Data import
    print(' - Importing ...', end='\t')
    data = pd.read_csv(
        path,
        sep=';'
    )
    print('Done !')

    # Columns selection
    print(' - Columns selection ...', end='\t')
    data = data.drop(['Name', 'Ticket', 'Cabin'], axis=1)
    print('Done!')

    # Filling NAN
    print(' - Filling NaN ...', end='\t')
    if graph:
        data.Age.plot.hist()
        plt.show()

        data.Embarked.hist()
        plt.show()

    data['Age'] = data.Age.fillna(value=data.Age.median())
    data['Embarked'] = data.Embarked.fillna(value='S')
    print('Done !')

    # Dummies
    print(' - Convert to dummies ...', end='\t')
    data = pd.get_dummies(data, drop_first=True)
    print('Done !')

    print(f'### Import data: Done! Elapsed: {time.time() - start}')

    return data


def data_prep(data: pd.DataFrame) -> pd.DataFrame:
    """Split the whole data set into taget & feature and split into train & test set

    Args:
        data (pd.DataFrame): The whole dataset

    Returns:
        pd.DataFrame: The test and train datasets & the test and train targets
    """
    x_data = data.drop('Survived_Yes', axis=1)
    y_data = data.Survived_Yes

    x_train, x_test, y_train, y_test = train_test_split(
        x_data,
        y_data,
        test_size=0.3,
        random_state=42
    )

    return x_train, x_test, y_train, y_test


if __name__ == '__main__':
    get_data()
