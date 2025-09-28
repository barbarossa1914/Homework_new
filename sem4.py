'''
'Ex1'
import matplotlib.pyplot as plt
import numpy as np
import random

diap = int(input())
amount = int(input())
k = float(input())
sig = float(input())

X = np.linspace(0, diap, amount)
Y = k * X
Y_n = np.array([random.gauss(i, sig) for i in Y])

def mnk(x, y):
    k_m = (np.mean(x*y) - np.mean(x)*np.mean(y))/(np.mean(x**2)-np.mean(x)**2)
    b_m = np.mean(y) - k_m*np.mean(x)
    print(k_m, b_m)
    return k_m, b_m
a, b = mnk(X, Y_n)

plt.scatter(X, Y_n)
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.plot(X, a * X + b)

plt.xlabel('X')
plt.ylabel('Y')
plt.show()
'''

'''
'Ex2'
import matplotlib.pyplot as plt
import numpy as np
import random

a1 = np.random.randint(1, 7, 50)
b1= np.random.randint(1, 7, 50)
gis1 = a1 + b1

a3 = np.random.randint(1, 7, 250)
b3= np.random.randint(1, 7, 250)
gis3 = a3 + b3

a2 = np.random.randint(1, 7, 1000)
b2 = np.random.randint(1, 7, 1000)
gis2 = a2 + b2
plt.subplot(131)
plt.hist(gis1, label='50 tries', density=True)
plt.legend()
plt.xticks(np.arange(1, 13, 1))
plt.yticks(np.arange(0, 0.25, 0.05))
plt.subplot(133)
plt.hist(gis2, label='1000 tries', density=True)
plt.xticks(np.arange(1, 13, 1))
plt.yticks(np.arange(0, 0.25, 0.05))
plt.legend()
plt.subplot(132)
plt.hist(gis3, label='250 tries', density=True)
plt.xticks(np.arange(1, 13, 1))
plt.yticks(np.arange(0, 0.25, 0.05))
plt.legend()
plt.show()
'''

'''
'Ex3'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv()
species_am = data['Species'].value_counts()
species = data['Species'].unique()

petal1 = (data['PetalLengthCm'] < 1.2).sum()
petal2 = ((data['PetalLengthCm'] < 1.5)&(data['PetalLengthCm'] > 1.2)).sum()
petal3 = (data['PetalLengthCm'] > 1.5).sum()
vals = [petal1, petal2, petal3]
plt.subplot(121)
plt.pie(species_am, labels=species)
plt.legend()
plt.subplot(122)
plt.pie(vals, labels=['less than 1.2', 'between 1.2 and 1.5', 'more than 1.5'])
plt.legend()
plt.show()
'''

'''
'Ex4'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(r'iris_data.csv')
SepalLength = data['SepalLengthCm']
SepalWidth = data['SepalWidthCm']
PetalLength = data['PetalLengthCm']
PetalWidth = data['PetalWidthCm']

def mnk(x, y):
    k_m = (np.mean(x*y) - np.mean(x)*np.mean(y))/(np.mean(x**2)-np.mean(x)**2)
    b_m = np.mean(y) - k_m*np.mean(x)
    return k_m, b_m

a1, b1 = mnk(SepalLength, PetalLength)
a2, b2 = mnk(SepalLength, PetalWidth)
a3, b3 = mnk(PetalLength, PetalWidth)

plt.subplot(331)
plt.scatter(SepalLength, SepalWidth)
plt.subplot(332)
plt.plot(SepalLength, a1 * SepalLength + b1, color='red')
plt.scatter(SepalLength, PetalLength)
plt.subplot(333)
plt.plot(SepalLength, a2 * SepalLength + b2, color='red')
plt.scatter(SepalLength, PetalWidth)
plt.subplot(334)
plt.scatter(SepalWidth, PetalLength)
plt.subplot(335)
plt.scatter(SepalWidth, PetalWidth)
plt.subplot(337)
plt.plot(PetalLength, a3 * PetalLength + b3, color='red')
plt.scatter(PetalLength, PetalWidth)
plt.show()
'''

'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv(r'BTC_data.csv')
price = data['close']
date = pd.to_datetime(data['time'])
date1 = date[::100]
plt.plot(date, price, label='price of btc')
plt.xticks(date1)
plt.show()
'''


'Ex6'
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv(r'BTC_data.csv')
price = data['close']
a = range(0, 1457)
date = pd.to_datetime(data['time'])
date1 = date[::100]
plt.plot(date, price, label='price of btc')
plt.xticks(date1)
z = np.polyfit(a, price, 10)
p1 = np.poly1d(z)
plt.plot(date, p1(range(0, 1457)))
plt.show()
'''
'''
'Ex8'
import random

a = [random.randint(0, 10) for i in range(5)]
b = [random.randint(0, 10) for i in range(5)]
a, b = set(a), set(b)
print(a, b)
print(a-b)
print(b-a)
print(a.union(b))
print(a&b)
'''
'Ex7'
import string

file = open('terms.txt', 'r')
text = str(file.read())
text = text.lower()
for el in string.punctuation:
    text = text.replace(el, '')
for el in [0,1,2,3,4,5,6,7,8,9]:
    text = text.replace(str(el), '')
text = text.split()
dic = {}
for el in text:
    dic[el] = text.count(el)
s_dic = sorted(dic.items(), key=lambda item: item[1], reverse=True)
top = s_dic[0:10]
print(top)