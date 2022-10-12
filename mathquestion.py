import random
import time
import math
x = random.randrange(1,10)
numb = random.randrange(1,10)
print("hello, welcome to Upset's math!")
time.sleep(1)
print(numb, "+ x =", x + numb)
answer = input("what is x? ")
if answer == x:
  print("correct")
else:
  print("incorrect")


