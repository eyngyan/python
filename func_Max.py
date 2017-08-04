#!/usr/bin/python
#Filename:func_Max.py

import math

def funcMax(a,b):
    if a>b:
        print(a, 'is maximum')
    elif b>a:
        print(b, 'is maximum')
    else:
        print(a, 'is equal to', b)

def area_Circle(r):
    return float(math.pi*r*r)



x=float(input('Please enter X: '))
y=float(input('Please enter Y: '))

funcMax(x,y)

print('以x为半径的圆面积为：', area_Circle(x))

