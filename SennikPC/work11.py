#96
list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]

#97
list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
row = int(input("выбор строки: "))
col = int(input("выбор столбца: "))
print(list[row][col])

#98
list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
row = int(input("выбор строки: "))
col = int(input("выбор столбца: "))
print(list[row][col])

#99
list = [[2 ,5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
row = int(input("выбор строки: "))
print(list[row])
col = int(input("выбор столбца: "))
print(list[row][col])
change = input("хочет ли пользователь изменить значение? (y/n)")
if change == "y":
    newvalue = int(input("ввести новое значение: "))
    list[row][col] = newvalue
print(list[row])

#100
sales = {"John":{"N":3056, "S":8463, "E":8441, "W":2694},
"Tom":{"N":4832, "S":6786, "E":4737, "W":3612},
"Anne":{"N":5239, "S":4802, "E":5820, "W":1859},
"Fiona":{"N":3904, "S":3645, "E":8821, "W":2451}}