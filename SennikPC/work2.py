num1 = int(input("первое число: "))
num2 = int(input("второе число: "))
if num1 > num2:
    print(num2, num1)
else:
    print(num1, num2)


num1 = int(input("введите число меньше 20: "))
if num1 > 20:
    print("Too high ")
else:
    print("Thank you")

num1 = int(input("введите число от 10 до 20: "))
if num1 >= 10 and num1 <= 20:
    print("Thank you ")
else:
    print("Incorrect answer ")

color = str(input("введите любимый цвет: "))
if color == "red" or color == "Red" or color == "RED":
    print("I like red too ")
else:
    print("«I don’t like", color, "I prefer red ")

num = int(input("введите свой возраст "))
if num >= 18 :
    print("You can vote")
elif num == 17 :
    print("You can learn to drive")
elif num == 16 :
    print("You can buy a lottery ticke")
else:
    print("You can go Trick-or-Treating")

num = int(input("введите число "))
if num < 10 :
    print("Too low")
elif num >= 10 and num <= 20 :
    print("Correct")
else:
    print("Too high")

num = input("Введите 1, 2 или 3: "))
if num == "1":
    print("Thank you")
elif num == "2":
    print("Well done")
elif num == "3":
    print("Correct")
else:
    print("Error message")




