import pandas as pd
from colors import bcolors as bc

train = pd.read_csv('train.csv')

# Dataset Shape
print("train.csv has {} {} rows {} and {} {} columns {}".format(bc.BLUE, train.shape[0], bc.ENDC, bc.PURPLE, train.shape[1], bc.ENDC))
print()
train.info()

#1 - Missing Values
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

# 2 - Identifiers
# perfect identifiers
print("\n There are {} {} {} different (unique) PassengerIds in the data"
      .format(bc.OKGREEN, train["PassengerId"].nunique(), bc.ENDC))

print("\n There are {} {} {} different (unique) names in the data"
      .format(bc.OKGREEN, train["Name"].nunique(), bc.ENDC))

# imperfect identifier
print("\n There are {} {} {} different (unique) ticket numbers in the data"
  .format(bc.OKGREEN, train["Ticket"].nunique(), bc.ENDC))

train = train.drop("PassengerId", axis=1)
train = train.drop("Name", axis=1)
train = train.drop("Ticket", axis=1)

print()
train.info()

# Handling Text and Categorial Attributes
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

for col in ['Sex', 'Embarked']:
  le.fit(train[col])
  train[col] = le.transform(train[col])

print()
print(train.head())

# 4-Feature Scaling
print("\n The maximum age is {} {} {}".format(bc.OKCYAN, train["Age"].max(), bc.ENDC))
print("\n The maximum fare is {} {} {}".format(bc.OKCYAN, train["Fare"].max(), bc.ENDC))

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(train)  # The scaler returns a NumPy-array instead of a Pandas DataFrame!
train = scaler.transform(train)

print("\n The minimum value is {} {} {} and the maximum value is {} {} {}"
     .format(bc.OKCYAN, train.min(), bc.ENDC, bc.OKCYAN, train.max(), bc.ENDC))

print()
print(train)

# 5 - Training and Testing
from sklearn.model_selection import train_test_split
input_data = train[:, 1:8]
labels = train[:, 0]

train_input, test_input, train_labels, test_labels = train_test_split(input_data, labels, test_size = 0.2) 
print('\n We have {} {} training {} and {} {} testing rows {}'
     .format(bc.BLUE, train_input.shape[0], bc.ENDC, bc.BLUE, test_input.shape[0], bc.ENDC))
print('\n There are {} {} input columns {}'
     .format(bc.PURPLE, train_input.shape[1], bc.ENDC))


#Save the data to the filesystem
import numpy as np

with open('train.npy', 'wb') as f:
  np.save(f, train_input)
  np.save(f, train_labels)

with open('test.npy', 'wb') as f:
  np.save(f, test_input)
  np.save(f, train_labels)
  
