def round_sum(a, b, c):

    return round10(a)+round10(b)+round10(c)


def round10(num):
   k=num%10
   rnum=num
   if(k>=5):
        rnum+=k
   else:   
        rnum-=k
   print(str(num)+" Rounded to -> "+str(rnum))
   return rnum



round_sum(6, 4, 4)
round_sum(0, 9, 0)
round_sum(24, 36, 32)