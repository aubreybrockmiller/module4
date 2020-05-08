# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from time import gmtime, strftime
print(strftime("%H:%M:%S", gmtime()))

import datetime
old_time = datetime.datetime.now()
new_time = old_time - datetime.timedelta(hours=2, minutes=10)
print(new_time - old_time)

answer = input("Please enter a word ")
print(answer)

import enchant
d = enchant.Dict("en_US")
d.check(input("Please enter a word "))
if (d) is True:
    print(d)

if (d) is False:
    d.check(input("Please enter a word ")) 


n = input("Enter some word ")
g = input("Enter some word ")
print(n,g)




