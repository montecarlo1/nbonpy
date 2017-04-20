import matplotlib as mpl
import datetime as mytime
from datetime import datetime
import numpy as np
import pandas as pd
import time
from pytz import timezone
from pytz import all_timezones
mpl.use('Agg')
import matplotlib.pyplot as plt

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print s
dates = pd.date_range('2017-01-01', periods=8)
print dates
df = pd.DataFrame({'A': 8,
                   'B': pd.Timestamp('20170102'),
                   'C': pd.Series(1, index=list(range(12))),
                   'D': np.array([3] * 12, dtype='int64'),
                   'E': pd.Categorical(["test1", "abc", "test2", "def","test3","ghi","test4","jkl","test5","mno","test6","pqr"]),
                   'F': 'Foo',
                   'G': 'Google',
                   'I':  12,
                   'II': 13,
                   'III': 14,
                   'IV': 15,
                   'V': 16,
                   'VI': 17,
                   'VII': 18,
                   'VIII': 19
                   })
print df
print df.dtypes
print df.head(2)
print df.tail(3)
print df.index
print df.columns
print df.values
print df.describe()

print df.T
print df.sort_index(axis=1, ascending=False)
print df.sort_values(by='E')
print df['G']
print df[0:4]

df2 = df.copy()

print(df2)
print df2[df2['G'].isin(['two', 'four'])]
print df2.T
print df.mean()
# print df.apply(lambda x:x.max() - x.min())

df.to_csv('foo.csv')
pd.read_csv('foo.csv')

df.to_excel('foo2.xlsx',sheet_name='mysheet2')
#pd.read_excel('foo.xlsx','mysheet')
print pd.Series([False, True, False])

# function f(x)=x
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(range(10))
fig.savefig("temp.png")
# all of the above are talking about pandas
# how to use numpy, time series, for example

# ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2017',periods=1000))
# ts = ts.cumsum()
# ts.plot(range(100))

# try time series
dates = np.array(["2017-04-05", "2017-04-06", "2017-04-07", "2017-04-08", "2017-04-09"],dtype='datetime64')
data = np.array([1, 2, 3, 4, 5])
plt.plot_date(dates, data)
plt.show()

#show the date
#today_date = datetime.date.today
date_time = datetime.strptime("2017-04-05 00:08", '%Y-%m-%d %H:%M')
print date_time
now = datetime.now()
print now.utcnow().tzinfo

#print all the time zones in the list
print len(all_timezones)
for zone in all_timezones:
    if 'US' in zone:
        print zone
    elif 'Asia' in zone:
        print zone
#transform timezone to US/Eastern
tzchina = timezone('US/Arizona')
print tzchina
utc = timezone('UTC')
#local time
print now.utcnow().replace(tzinfo=utc).astimezone(tzchina)
#wall clock time, unit:second
print time.time()
#processor clock time, unit:second
print time.clock()
print time.localtime()
# GMT time
print now.utcnow().strftime('%Y-%m-%d %H:%M:%S')
# try another one
