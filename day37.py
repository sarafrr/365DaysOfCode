# pandas is a python library for working with datasets
# panel data (econometrics term for multidimensional structured
# data sets)
import pandas as pd

mydata = {
    'cats' : ['siberian', 'main coon', 'norwegian'],
    'maxLength' : [46, 81, 46]
}

mydf = pd.DataFrame(mydata)
print(mydf)

# a pandas series is as a column in a table
# it is created a list and it is transformed into a Series
# or it can be created from any kind of hashable dataset
# (lists and datasets)
maxLenght = [46, 81, 46]

labels = ["sibLen", "mainCLen", "norwLen"]
maxLengthSeries = pd.Series(maxLenght, index=labels)

# a Serie has a label for each entry which is
# the index, if it is not specified (not our case)

print(maxLengthSeries['mainCLen'])
print(maxLengthSeries)

# it is possible to create a Series from a dictionary (hashable type)
# so the key values are used as label of the specific entry
# of the Seires and the values as values
catMaxLengths = {'sibLen':64, 'mainCLen':81, 'norwLen':64}

catMaxLengthsSeries = pd.Series(catMaxLengths)
print(catMaxLengthsSeries)

# to include only specific samples/keys in the Series
# it is possible to use the parameter @index@ in the Series' creation
catMaxLengthsSeries = pd.Series(catMaxLengths, index=['sibLen', 'mainCLen'])
print(catMaxLengthsSeries)

