#Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo". 

#string_bits('Hello') - 'Hlo'
#string_bits('Hi') - 'H'
#string_bits('Heeololeo') - 'Hello'

def string_bits(strs):
  a=1
  retstr=''
  for i in strs:
   if((a%2)!=0):
     retstr+=i
     #print(str(a)+' the item is '+str(i))
   a+=1
  print(retstr)
  return retstr
string_bits('Hello')
string_bits('Hi')
string_bits('Heeololeo')
