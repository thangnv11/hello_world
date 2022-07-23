"""
This module is to provide descriptive statistics
authored: chibq
dated: July 23, 2022
"""

import pandas as pd
from IPython.core.display import display

#dt = pd.read_csv('credit.csv')
#display(dt.describe())
#display(dt.info())
#display(dt.head())
#display(dt.tail())


def chi_load2(file_name: str, *args):
    """
    This function is to load a CSV file
    :param file_name: name of csv file
    :param args: list of args
    :return: pandas dataframe
    """
    dt = pd.read_csv(file_name)
    return dt


def chi_stats(file_name: str, *args):
    """
    This function is to provide descriptive stats for the loaded CSV file
    :param file_name: name of csv file
    :param args: list of args
    :return: descriptive stats
    """
    dt = chi_load2(file_name)
    info = display(dt.info())
    desc = display(dt.describe())
    return desc


if __name__ == '__main__':
    desc = chi_stats('credit.csv')

