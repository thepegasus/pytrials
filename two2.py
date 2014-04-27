#!/usr/bin/python
#Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

#has22([1, 2, 2])  True
#has22([1, 2, 1, 2]) - False
#has22([2, 1, 2]) - False

def has22(intar):
    prevar = None
    flag = False
    for currentvar in intar:
        if(currentvar == prevar):
            flag = True
        prevar = currentvar
    if(flag == True):
        print "True"
    else:
        print "False"
        
has22([1, 2, 2])
has22([1, 2, 1, 2])
has22([2, 1, 2, 2])
