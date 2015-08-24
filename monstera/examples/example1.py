__author__ = 'shazada nawaz'

from monstera.core import MLObject

def example1():
    target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
                  "databases/undocumented/connectionist-bench/sonar/sonar.all-data")

    # Instantiate class
    ml = MLObject(target_url)

    # output summary statistics
    ml.data_summary()



