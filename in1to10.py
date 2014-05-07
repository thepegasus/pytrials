#!/usr/bin/python3
#Given a number n, return True if n is in the range 1..10, inclusive. Unless "outsideMode" is True, in which case return True if the number is less or equal to 1, or greater or equal to 10. 

#in1to10(5, False) - True
#in1to10(11, False) -False
#in1to10(11, True) -True

def in1to10(num, outsidemode):
    if(((num>=1 and num<=10) and outsidemode==False) or ((num<=1 or num>=10) and outsidemode==True)):
        print("True")
    else:
        print("False");
    

in1to10(5, False)
in1to10(11, False)
in1to10(11, True)
