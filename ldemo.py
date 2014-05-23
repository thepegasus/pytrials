#!/usr/bin/python3
#Find the sum of numbers from 1 to 10 except 5 and 6. If 5 or 6 is encountered,print the message Hello Five and Hello Six respectively 

def addnums():
    sumval=0
    for num in range(1,11):
        print("Making decision on :"+str(num))
        if(num!=5 and num!=6):
            sumval+=num
            print("Adding "+str(num)+" to sum. Now sum is "+str(sumval))
        elif(num==5):
            print("Hello Five")
        else:
            print("Hello Six")
        
        
    print("The total of numbers from 1 to 10  except 5 and 6 is "+str(sumval))

addnums()
