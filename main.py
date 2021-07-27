from stringCalculatorFile import *
from random import random


print('starting')
ciscoCalculator = StringCalculator();

for i in range(0,1):
    x=random()
    print(x)
    x=int(x*10000)
    print(int(x))

    y=random()
    print(y)
    y=int(y*10000)
    print(int(y))

    mrString='+,'
    mrString=mrString+str(x)+','+str(y)
    print(mrString)
    results=ciscoCalculator.parse(mrString)
    print(ciscoCalculator.parse(mrString))
    print(results[1]=='NUMBER' , print(results[2]=='NUMBER'))





print('ending')
