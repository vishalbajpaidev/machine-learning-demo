import matplotlib as plot
import numpy as np
from sklearn import datasets

diabetes = datasets.load_diabetes()

print(diabetes.keys())
print(diabetes.DESCR)

print((diabetes.target.shape))
print((diabetes.data.shape))