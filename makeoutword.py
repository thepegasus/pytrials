#Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>". 

#make_out_word('<<>>', 'Yay') - '<<Yay>>'
#make_out_word('<<>>', 'WooHoo') - '<<WooHoo>>'
#make_out_word('[[]]', 'word')- '[[word]]'

def make_out_word(out, word):
  startw=out[0:2]
  endw=out[2:4]
  fullw=startw+word+endw
  return fullw
