from random import shuffle
import random
from pytz import all_timezones
import operator


somelist=[(1,5,8),(6,2,4),(9,7,5)]
somelist.sort(key=operator.itemgetter(0))
print somelist
somelist.sort(key=operator.itemgetter(1))
print somelist
somelist.sort(key=operator.itemgetter(2))
print somelist
x = [[i] for i in range(20)]
print x
print('\n')
shuffle(x)
print('after cleaning the random data:')
print x

s = list(range(20))
random.shuffle(s)
print(s)


def foo1():
    print 'foo1',


def foo2():
    print 'foo2',


def foo3():
    print 'foo3',

A=[foo1,foo2,foo3]
for x in A:
    x()

print "\r\n"
shuffle(A)
for y in A:
    y()

iteration = random.randint(2,100)
for k in all_timezones:
    print k;

while iteration > 0:
    for i in range(0,len(all_timezones)-1):
        for j in range(0,len(all_timezones)-i-1):
            if(all_timezones[i]>all_timezones[j]):
                temp = 0
                temp = all_timezones[i]
                all_timezones[i]=all_timezones[j]
                all_timezones[j] = temp
        iteration -=1
print('--------------------')
for m in all_timezones:
    print m;