#!/usr/bin/python
#Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".

#make_abba('Hi', 'Bye') - 'HiByeByeHi'
#make_abba('Yo', 'Alice') - 'YoAliceAliceYo'
#make_abba('What', 'Up') - 'WhatUpUpWhat'
def make_abba(str1,str2):
    print str1+str2+str2+str1
make_abba('Hi','Bye')
make_abba('Yo','Alice')
make_abba('What','Up')
