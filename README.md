# monstera
A python library to handle boilerplate machine learning tasks that I encounter.

## Dependencies

This library depends on the following:
1. Python 2.7+
2. SciPy
3. NumPy
4. Pandas
5. scikit-learn

Due to cross-dependency issues associated with the above packages I reccomend
using Anaconda (free) from
<a href="http://continuum.io">Continuum Analytics</a>. It's pretty cool.

## Quickstart

The below code snippet gives a high-level overview of how this library works:

<pre>
# import machine learning object
from monstera.core import MLObject

# get some data
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
                  "databases/undocumented/connectionist-bench/sonar/sonar.all-data")

# instantiate class
ml = MLObject(target_url)

# output summary statistics
ml.data_summary()
</pre>






