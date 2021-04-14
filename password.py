import string
import secrets

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

passwd = input('enter a password ')

dataset = string.ascii_lowercase + string.digits + string.punctuation

error1 = ('password is too short, must be at least 8 characters long')
error2 = ('password is too long, max 64 characters')
error3 = ('password is 8 or more characters but does not meet all the requirements(at least one uppercaste character, 1 number and 1 symbol')

def gener():
  print(error3)
  gen = input('would you like us to generate a pswword for you instead?:')

  if gen == ('yes'):
    passwod = ''.join(secrets.choice(dataset) for i in range(8, 64))
    print(passwod)
  elif gen == ('no'):
    exit()

lCount = 0
uCount = 0
nCount = 0
sCount = 0

for i in passwd:
  if i in lowercase:
    lCount += 1
  elif i in uppercase:
    uCount += 1
  elif i in numbers:
    nCount += 1
  elif i in symbols:
    sCount += 1

if len(passwd) >= 8 and len(passwd) <= 64 and sCount == 0:
  gener()
elif len(passwd) >= 8 and len(passwd) <= 64 and nCount == 0:
  gener()
elif len(passwd) >= 8 and len(passwd) <= 64 and uCount == 0:
  gener()
elif len(passwd) < 8:
    print(error1)
elif len(passwd) > 64:
    print(error2)
else:
  print('password good')
