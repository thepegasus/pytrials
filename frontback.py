 #Given a string, return a new string where the first and last chars have been exchanged.

#front_back('code') - 'eodc'
#front_back('a') - 'a'
#front_back('ab') - 'ba'

def front_back(str):
  l=len(str)
  if(l<=1):
      return str
     
  f=str[0]
  b=str[l-1]
  newstr=b+str[1:l-1]+f
  return newstr
