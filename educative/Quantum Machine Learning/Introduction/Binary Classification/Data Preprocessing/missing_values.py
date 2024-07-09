import pandas as pd
from colors import bcolors as bc

train = pd.read_csv('train.csv')

# Dataset Shape
print("train.csv has {} {} rows {} and {} {} columns {}".format(bc.BLUE, train.shape[0], bc.ENDC, bc.PURPLE, train.shape[1], bc.ENDC))
print()
train.info()

#1 Missing Values
# option 1
# You only have two passengers without an "Embarked" location. This is acceptable
train = train.dropna(subset=['Embarked'])
print("\n Now, train.csv has {} {} rows {} and {} {} columns {}".format(bc.BLUE, train.shape[0], bc.ENDC, bc.PURPLE, train.shape[1], bc.ENDC))

# option 2
# You have very little information about the cabin, so lets drop it
train = train.drop("Cabin", axis=1)
print("\n And now train.csv has {} {} rows {} and {} {} columns {}".format(bc.BLUE, train.shape[0], bc.ENDC, bc.PURPLE, train.shape[1], bc.ENDC))

# option 3
# The age category is omitted often. But intuition tells us it might be important.
mean = train["Age"].mean()
train["Age"] = train["Age"].fillna(mean)

print()
train.info()
