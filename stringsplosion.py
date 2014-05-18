#Given a non-empty string like "Code" return a string like "CCoCodCode".

#string_splosion('Code') - 'CCoCodCode'
#string_splosion('abc') - 'aababc'
#string_splosion('ab') -'aab'

def string_splosion(str):
  i=0
  fstr=''
  while i<=len(str):
    tempstr=str[:i]
    fstr+=tempstr
    i+=1
  return fstr