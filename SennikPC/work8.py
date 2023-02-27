#69
country_tuple = ("Китай", "Япония", "Италия", "Германия", "Дания")
print(country_tuple)
print()
country = input("ввести название одной из этих стран: ")
print(country, " индекс ", country_tuple.index(country))

#70
country_tuple = ("Китай", "Япония", "Италия", "Германия", "Дания")
print(country_tuple)
print()
country = input("ввести название одной из этих стран: ")
print(country, " индекс ", country_tuple.index(country))
print()
num = int(input("ввести число между 0 и 4: "))
print(country_tuple[num])

#71
sports_list = ["Футболл", "Волейболл"]
sports_list.append(input("ввести свой любимый вид спорта "))
sports_list.sort()
print(sports_list)

#72
subject_list = ["математика", "английский", "информатика", "история", "физика"]
print(subject_list)
dislike = input("какие из этих предметов ему не нравятся? ")
getrid = subject_list.index(dislike)
del subject_list[getrid]
print(subject_list)

