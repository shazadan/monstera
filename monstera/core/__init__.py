__author__ = 'shazada nawaz'

from math import sqrt

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
        self.target = []
        self.prediction = []

    def data_summary(self):
        ''' Output summary statistics on data in the csv file '''

        # print head and tail of data frame
        print(self.dataframe.head())
        print(self.dataframe.tail())

        # print summary of attributes in data frame - both numerical and categorical
        summary = self.dataframe.describe(include='all',
                                          percentiles=[.05, .25, .75, .95])
        print(summary)

    def model_performance(self):
        self._regression_performance()

    def _regression_performance(self):

        error = []

        for i in range(len(self.target)):
            error.append(self.target[i] - self.prediction[i])

        squared_error = []
        abs_error = []

        for val in error:
            squared_error.append(pow(val, 2))
            abs_error.append(abs(val))

        # calc MSE
        mse = sum(squared_error) / len(squared_error)
        rmse = sqrt(mse)
        mae = sum(abs_error) / len(abs_error)

        target_deviation = []
        target_mean = sum(self.target) / len(self.target)

        for val in self.target:
            target_deviation.append(pow(val - target_mean, 2))

        target_variance = sum(target_deviation) / len(target_deviation)
        target_std_dev = sqrt(target_variance)

        print "MSE: ", round(mse, 4)
        print "Target Variance (TV): ", round(target_variance, 4)
        print
        print "MAE: ", round(mae, 4)
        print "RMSE: ", round(rmse, 4)
        print "Target Standard Deviation (TSD): ", round(target_std_dev, 4)
        print
        if rmse < target_std_dev:
            print "Prediction model performing well (RMSE < TSD)"
        else:
            print "Prediction model not performing well (RMSE >= TSD)"

    def _classifier_performance(self):
        pass

    def train_test_split(self, percentage=1):
        '''
        Randomly split data into training data and test data based on passed percentage value
        :return:
        '''
        return cross_validation.train_test_split(self.dataframe, test_size=0.4,
                                                 random_state=0)
