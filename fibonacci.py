#!/usr/bin/python
#Filename:fibonacci.py

def fibonacci(max):
    n, a, b, = 0, 0, 1
    while n < max:
        print(b)
        a, b=b, a+b
        n = n+1
    return 'done'

num = int(input('please enter the number of Fibonacci function:'))
if num > 0:
    fibonacci(num)
else:
    print('please give me a correct number')



