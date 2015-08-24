__author__ = 'shazada nawaz'

from monstera.core import MLObject
from monstera.examples import *


target = [1.5, 2.1, 3.3, -4.7, -2.3, 0.75]
prediction = [0.5, 1.5, 2.1, -2.2, 0.1, -0.5]


target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases"
              "/undocumented/connectionist-bench/sonar/sonar.all-data")

ml = MLObject(target_url)
ml.target = [1.5, 2.1, 3.3, -4.7, -2.3, 0.75]
ml.prediction = [0.5, 1.5, 2.1, -2.2, 0.1, -0.5]
ml.model_performance()