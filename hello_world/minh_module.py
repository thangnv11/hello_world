"""
This module is to compute some basic statistics
"""
import pandas as pd
from IPython.core.display import display


def minh_load(ten_file: str, *args):
    """
    This function is to load csv
    :param ten_file: ten_file
    :param args: list of args
    :return: df
    """
    df = pd.read_csv(ten_file)
    display("Du lieu da duoc load xong:")
    display(df.head(5))
    return df


def minh_stat(file_name: str, *args):
    """
    This function is to summarize some basic statistics
    :return: summary
    """
    df = minh_load(file_name)
    summary_statistic = display(df.discribe())
    summary_info = display(df.info())
    return summary_statistic, summary_info


if __name__ == "__main__":
    output = minh_load(ten_file = "credit.csv")