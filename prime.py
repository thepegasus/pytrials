#!/usr/bin/python
#Next Prime Number - Have the program find prime numbers until the user chooses to stop asking for the next one.
def nextprime(lastprime):
    nextnum=lastprime
    cloop=True
    while(cloop==True):
        nextnum = nextnum+1
        if(checkprime(nextnum)==True):
            cloop=False
            return nextnum

def checkprime(num):
    for divisor in range(2,num):
        if(num%divisor==0):
            return False;
    return True

lastprime=1
input=0
while(input!="1"):
   lastprime= nextprime(lastprime);
   input=raw_input("The next prime is:"+`lastprime`+". Press 1 to exit or any other key to continue!")

