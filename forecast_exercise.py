#Learned a lot but can't make it work
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


test_set = pd.read_csv('C:/Users/barkin/test_set.csv')
train = pd.read_csv('C:/Users/barkin/train.csv')

#copying
test=test_set.copy()
data=train.copy()

#Delete SEKTOR because we already have id
test.pop("SEKTOR")
data.pop("SEKTOR")

# islem turu one hot yapılcak 

#test
# Get one hot encoding of column
one_hot = pd.get_dummies(test['ISLEM_TURU'])
# Drop column  as it is now encoded
test = test.drop('ISLEM_TURU',axis = 1)
# Join the encoded 
test = test.join(one_hot)
# Drop dummy column  as it is now encoded
test = test.drop('TAKSITLI',axis = 1)

#data
# Get one hot encoding of columns 
one_hot = pd.get_dummies(data['ISLEM_TURU'])
# Drop column  as it is now encoded
data = data.drop('ISLEM_TURU',axis = 1)
# Join the encoded 
data = data.join(one_hot)
# Drop dummy column  as it is now encoded
data = data.drop('TAKSITLI',axis = 1)

# Drop NaN column
test = test.drop('ISLEM_TUTARI',axis = 1)
#add new column full of zeros
test['ISLEM_TUTARI'] = 0
#change the place of the zero column to first index
cols = test.columns.tolist()
cols = cols[-1:] + cols[:-1]
test = test[cols]
# I must  have consist number of rows
data.shape
test.shape

data = data[data.index < 219666]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data, test, test_size=0.33, random_state=42)

#fit model
from sklearn.linear_model import  LinearRegression
regressor=LinearRegression()
y_pred = regressor.fit(X_train,y_train)
print(y_pred)
prediction = y_pred.predict(X_test)
print(prediction)

#My prediction is meaningless so i quit here

# make a new dataframe
# in that dataframe there will be 2 columns
# one for id one for guess
# id should sum the guesses
