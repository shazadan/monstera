__author__ = 'shazada nawaz'

from monstera import MLObject

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
              "databases/undocumented/connectionist-bench/sonar/sonar.all-data")

# Instantiate class
ml = MLObject(target_url)

# output summary statistics
ml.summarize()

# split the data into traning and test datasets
train, test = ml.train_test_split(percentage=0.4)



