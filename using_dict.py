#!/usr/bin/python
#Filename:using_dict.py

#add is short for address book

add={'Swaroop':'swaroopch@byteofpython.info',
     'Larry':'larry@wall.org',
     'Matsumoto':'matz@ruby-lang.org',
     'Spammer':'spammer@hotmail.com'}
print("\n Swaroop's address is:", add['Swaroop'])

#Adding a key/value pair

add['Guido']='guido@python.org'

#Delete a key/vvalue pair

add.pop('Spammer')

print('The new address book is:\n')
for name,address in add.items():
     print('Contact:', name, ',', 'address:', address, '\n')





