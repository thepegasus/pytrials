#!/usr/bin/python3
#Return True if the string "cat" and "dog" appear the same number of times in the given string.

#cat_dog('catdog') - True
#cat_dog('catcat') - False
#cat_dog('1cat1cadodog') - True

def cat_dog(strng):
    if(strng.count("cat")==strng.count("dog")):
           print("True")
    else:
           print("False")
cat_dog('catdog')
cat_dog('catcat') 
cat_dog('1cat1cadodog')
