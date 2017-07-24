#!/usr/bin/python
#Filename:using_list.py

#This is my shopping list
shoplist=['apple', 'mango', 'carrot', 'banana']

print('i have', len(shoplist), 'items need to buy')

print("These items are:",)
for item in shoplist:
    print(item)

print('\n i also have to buy rice.')
shoplist.append('rice')
print('new shoplist is:', shoplist)

print('\n The first item I will buy is:', shoplist[0])

print('\n I brought the', shoplist[0])
del shoplist[0]
print('\n My shopping list is now', shoplist)


