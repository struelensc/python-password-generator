import random

#shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

password = None # combine random chars
password = shuffle(password)

#ouput
print(password)