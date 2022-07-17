"""
This module is to load data with the csv format
authored: phuongnv
dated: July 17, 2022
"""
import pandas as pd
from IPython.core.display import display

def chi_load(file_name: str, *args):
    """
    This function is to load a CSV file
    :param file_name: name of csv file
    :param args: list of other arguments
    :return dt: pandas dataframe
    """
    dt = pd.read_csv(file_name)
    display(dt.head(5))
    return dt

if __name__ == "__main__":
    dt = chi_load(file_name='credit.csv')