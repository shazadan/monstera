__author__ = 'shazada nawaz'

import pandas as pd
from sklearn import cross_validation


class MLObject:

    def __init__(self, csv_file, header=None, prefix='V'):
        '''
        :param csv_file: path to csv file
        :param header: is there a header in the csv file
        :param prefix: if no header what literal to use for attribute names
        :return:
        '''
        self.dataframe = pd.read_csv(csv_file, header=header, prefix=prefix)

    def summarize(self):
        ''' Output summary statistics on data in the csv file '''

        #print head and tail of data frame
        print(self.dataframe.head())
        print(self.dataframe.tail())

        #print summary of attributes in data frame - both numerical and categorical
        summary = self.dataframe.describe(include='all', percentiles=[.05, .25, .75, .95])
        print(summary)

    def train_test_split(self, percentage=1):
        '''
        Randomly split data into training data and test data based on passed percentage value
        :return:
        '''
        return cross_validation.train_test_split(self.dataframe, test_size=0.4, random_state=0)
