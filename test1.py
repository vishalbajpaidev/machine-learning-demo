import numpy as np

from sklearn import preprocessing
from sklearn import utils

#We imported a couple of packages. Let's create some sample data and add the line to this file:

input_data = np.array([[3, -1.5, 3, -6.4], [0, 3, -1.3, 4.1], [1, 2.3, -2.9, -4.3]]);
print(input_data)

print("-----")
print(input_data)

data_standardized = preprocessing.scale(input_data)

print(data_standardized)

print "\nMean = ", data_standardized.mean(axis = 0)
print "Std deviation = ", data_standardized.std(axis = 0)


data = np.array([6,2,3,1])
scaledData = preprocessing.scale(data)
print scaledData
print data -np.nanmean(data)
print (data -np.nanmean(data))/np.nanstd(np.array([6,2,3,1]))

# https://www.khanacademy.org/math/probability/data-distributions-a1/summarizing-spread-distributions/a/calculating-standard-deviation-step-by-step?utm_account=Grant&utm_campaignname=Grant_Math_Dynamic&gclid=CjwKCAjwgabeBRBuEiwACD4R5mJX52xUSkyxFXIMRHSRB_iUnQOsXBS-GxtGE8NIiGGFZ9nDDnFXIRoCnywQAvD_BwE