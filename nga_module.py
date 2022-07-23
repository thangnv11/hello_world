
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
    return dt


def summary(file_name: str, *args):
    """
    This function is to summary data
    :param file_name: name of csv file
    :param args: list of other arguments
    :return:
    """
    dt = chi_load(file_name)
    display(dt.head(10))
    display(dt.tail(10))
    display(dt.info())
    display(dt.describe())


def csv_summary(file_name:str, *args):
    """
    This function is to load n summary data
    :param file_name: name of csv file
    :param args: list of other arguments
    :return:
    """
    summary(file_name)
    chi_load(file_name)

if __name__ == "__main__":
    csv_summary('C:\Users\Nga Mai\PycharmProjects\hello_world\hello_world\credit.csv')


#
# dt = pd.read_csv('hello_world/credit.csv')
# display(dt.info())



# mean = dt.mean()
# median = dt.median()
#
# final = pd.concat([mean, median], axis = 1)
#final = final.rename(columns={"0": "mean", "1": "median"}, axis = 0)



# final=final.rename({'mean': 0, 'median':1})



