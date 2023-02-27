#52
import random
num = random.randint(1, 100)
print(num)

#53
import random
fruit = random.choice(["яблоко", "банан", "груша", "клубника", "саша"])
print(fruit)

#54
import random
coin = random.choice(["h", "t"])
guess = input("введите (h) или (t): ")
if guess == coin:
 print("ты выиграл")
else:
 print("не повезло")
if coin == "h":
 print("это (h)")
else:
 print("это (t)")

 #55


 #56
 import random

 num = random.randint(1, 10)
 correct = False
 while correct == False:
  guess = int(input("ввести число: "))
  if guess == num:
   correct = True

#57


#58


#59