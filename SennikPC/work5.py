#35
name = input("ввести имя ")
for i in range(0, 3):
    print(name)

#36
name = input("ввести имя: ")
num =  int(input("ввести число: "))
for i in range(0, num):
    print(name)

#37
name = input("ввести имя: ")
for i in name:
    print(i)

#38
num = int(input("ввести число: "))
name = input("ввести имя: ")
for i in range(0, num):
 for a in name:
     print(a)

#39
num = int(input("ввести число от 1 до 12: "))
for i in range(1, 13):
 ravno = i * num
 print(i, "x", num, "=", ravno)

#40
num = int(input("ввести число до 50: "))
for i in range(50, num-1, -1):
 print(i)

#41
name = input("ввести имя:  ")
num = int(input("ввести число: "))
if num < 10:
 for i in range(0, num):
 print(name)
else:
 for i in range(0, 3):
 print("Too high")