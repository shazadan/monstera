__author__ = 'shazada nawaz'

import datetime
import pandas.io.data as web

def get_market_data(symbol=None, start=datetime.datetime.now(), end=datetime.datetime.now()):

    source='yahoo'
    #start = datetime.datetime(2010, 1, 1)
    #end = datetime.datetime(2013, 1, 27)

    f = web.DataReader(symbol, source, start, end)
    print f
