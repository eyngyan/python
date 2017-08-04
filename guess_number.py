#!/usr/bin/python
#Filename: guess_number.py
import random

number = random.randint(1,6)
print(number)
print('There is a number in my hand, guess 3 times!')
time=3
while time>0:
    time=time-1
    guess=int(input('The number is: '))
    if guess is number:
        print('哎呀我去，猜对啦')
        break
    elif guess < number:
        print('你还有', time, '次机会')
        print('小了')
    else:
        print('你还有', time, '次机会')
        print('大了')
print('GAME OVER')
print('正确答案就是: ', number)
