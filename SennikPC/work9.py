#80
name1 = input("ввести свое имя: ")
print("всего ", len(name1), " букв")
name2 = input("ввести свое фамилию: ")
print("всего ", len(name2), " букв")
name = name1 + " " + name2
print("твое полное имя", name)
print("всего ", len(name), " букв")

#81
name = input("ввести его любимый школьный предмет: ")
for i in name:
 print( i, end = "-")

#82
poem = "Беги, сокройся от очей, Цитеры слабая царица! "
print(poem)
s = int(input("ввести начальную поэзию: "))
e = int(input("ввести конечную позицию: "))
print(poem[s:e])

#83
msg = input("Введите сообщение заглавными буквами: ")
tryagain = False
while tryagain == False:
 if msg.isupper():
  print("Спасибо")
 tryagain = True
else:
 print("Попробуй снова")
 msg = input("Введите сообщение заглавными буквами: ")

#84
code = input("ввести почтовый индекс: ")
start = code[0:2]
print(start.upper())