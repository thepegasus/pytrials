#You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases. 

#caught_speeding(60, False) - 0
#caught_speeding(65, False) - 1
#caught_speeding(65, True) - 0

def caught_speeding(speed, isbirthday):

   l1speedlimit=60
   l2speedlimit=80
   if(isbirthday==True):
       l1speedlimit+=5
       l2speedlimit+=5
   if(speed<=l1speedlimit):
       print("No ticket - 0")
   elif(speed>l1speedlimit and speed<=80):
       print("Small ticket - 1")
   else:
       print("Big ticket - 2")


caught_speeding(60, False)
caught_speeding(95, False)
caught_speeding(65, True)
caught_speeding(75, True)
