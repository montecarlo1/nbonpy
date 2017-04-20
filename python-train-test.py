import matplotlib as mpl
import datetime as mytime
from datetime import datetime
import numpy as np
import pandas as pd

import random
from sklearn.model_selection import train_test_split as mysk
import time
from pytz import timezone
from pytz import all_timezones
df = pd.DataFrame(np.random.randn(1000000,200))
msk=np.random.rand(len(df)) < 0.8
train = df[msk]
test = df[~msk]
print len(test)
print len(train)

#=========================================
#train data && test data
with open("foo2.xlsx","rb") as f:
    data = f.read().split('\n')

#data cleaning
random.shuffle(data)

train_data = data[:50]
test_data = data[50:]
#=========================================
csv = pd.read_csv('foo.csv')
train, test = mysk(csv, train_size=0.2)
print train_data
print test_data
print ('------total data------')
print csv
print ('------train data------')
print train
print ('------test data-------')
print test