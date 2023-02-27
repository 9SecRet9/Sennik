#88
from array import *
nums = array(i, [])
for i in range(0, 5):
 num = int(input("ввести число: "))
 nums.append(num)
nums = sorted(nums)
nums.reverse()
print(nums)

#89
from array import *
import random
 nums = array(‘i’, [])
for i in range (0, 5):
 num = random.randint(1, 100)
 nums.append(num)
for i in nums:
 print(i)

 #90
 from array import *

 nums = array(‘i’, [])
 while len(nums) < 5:
  num = int(input("ввести число от 10 и 20: "))
  if num >= 10 and num <= 20:
   nums.append(num)
  else:
   print("Outside the range")
 for i in nums:
  print(i)

#91
from array import *
nums = array(‘i’, [5, 7, 9, 2, 9])
for i in nums:
 print(i)
num = int(input("ввести число: "))
if nums.count(num) == 1:
 print(num, "в листе")
else:
 print(num, "в листе ", nums.count(num))