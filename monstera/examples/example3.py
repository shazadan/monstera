__author__ = 'shazada nawaz'

import datetime

from monstera.utils.data import get_market_data

symbol = "^FTSE"
start = datetime.datetime(2014, 1, 1)
end = datetime.datetime(2014, 1, 27)

get_market_data(symbol=symbol, start=start, end=end )
