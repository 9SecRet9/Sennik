#45
total = 0
while total <= 50:
 num = int(input("ввести число: "))
 total = total + num
 print("The total is...", total)

 #46
 num = 0
 while num <= 5:
     num = int(input("ввести числ: "))
 print("The last number you entered was a ", num)

 #47
 num1 = int(input("ввести число: "))
 total = num1
 a = "y"
 while a == "y":
     num2 = int(input("ввести другое число: "))
     total = total + num2
     a = input("хотители вести ? (y/n) ")
 print("сумма всех чисел ", total)

 #48
 a = "y"
 c = 0
 while a == "y":
     name = input("ввести имя человека, которого пользователь хочет пригласить на вечеринку: ")
     print(name, " приглашение отправленно")
     c = c + 1
     a = input("хочет ли пользователь пригласить кого-то еще? (y/n) ")
 print( c, " придут на вечеринку")
