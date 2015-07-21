__author__ = 'shazada nawaz'
import pandas as pd


def summarize(csv_file_path, header_yn=None, prefix='V'):
    ''' Output most common summary statistics on variables in a csv file '''

    #read csv into pandas data frame
    dataframe = pd.read_csv(csv_file_path, header=header_yn, prefix=prefix)

    #print head and tail of data frame
    print("\nDATAFRAME HEAD")
    print(dataframe.head())
    print("\nDATAFRAME TAIL")
    print(dataframe.tail())

    #print summary of data frame
    print("\nSUMMARY STATISTICS")
    summary = dataframe.describe()
    print(summary)

