import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import MultiLabelBinarizer
testdata = pd.DataFrame({
    'pet':['cat','dog','dog','fish','donkey','horse'],
    'age':[2,4,5,8,6,7],
    'salary':[3,4,5,6,7,8]
})
#binary, one-hot code
#print (OneHotEncoder(sparse=False).fit_transform(testdata[['age']]))
a = OneHotEncoder(sparse=False).fit_transform(testdata[['age']])
print a
b = OneHotEncoder(sparse=False).fit_transform(testdata[['salary']])
print b
#final_output = pd.hstack(a, b)
c = MultiLabelBinarizer().fit_transform(testdata[['age','salary']].values)
print c

d = LabelEncoder().fit_transform(testdata[['pet']])
e = OneHotEncoder(sparse=False).fit_transform(d.reshape(-1,1))
print e
f = LabelBinarizer().fit_transform(testdata['pet'])
print f

g = pd.get_dummies(testdata, columns=pd)
print g