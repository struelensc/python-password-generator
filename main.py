import random

#shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

uppercaseLetter1=chr(random.randint(65,90)) #generate random uppercase letter
uppercaseLetter2=chr(random.randint(65,90)) #generate random uppercase letter
lowercaseLetter1=chr(random.randint(97,122)) #generate random lowercase letter
lowercaseLetter2=chr(random.randint(97,122)) #generate random lowercase letter
number1=chr(random.randint(48,57)) #generate random number
number2=chr(random.randint(48,57)) #generate random number
special1=chr(random.randint(33,64)) #generate random special character
special2=chr(random.randint(33,64)) #generate random special character

password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + number1 + number2 + special1 + special2
password = shuffle(password)

#ouput
print(password)