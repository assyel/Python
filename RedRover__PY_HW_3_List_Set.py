
# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
my_list = ['a', 'b', [1, 2, 3], 'd']
# впереди звездочка раскрывает скобки списка в выведении
print(*my_list[-2])
Almost out of storage … If you run out, you can't create or edit files, send or receive email on Gmail, or back up to Google Photos.
3.1. 
#Solutions from RedRover
#Option 1
print(my_list[2][0])
print(my_list[2][1])
print(my_list[2][2])

# Option 2. Using deconstruction
my_list = ['a', 'b', [1, 2, 3], 'd']
list1 = my_list[2]
print(*list1, sep='\n')

# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
res = list([i for i in list_1 if isinstance(i, int)])
print(f'Sum is: {sum(res)}')
#    - распечатайте все строки, где есть буква 'a'
result = [x for x in list_1 if isinstance(x, str) and 'a' in x]
print(result)
# без comprehension
list_1 = ['Hi', 'berry', 2, None, 75, 'pizza', 36, 100]
for item in list_1:
    if isinstance(item, str) and 'a' in item:
        print(item)

#Solutions from RedRover
#a) Using filter get sum of all integers
print(sum(filter(lambda x: isinstance(x, int), list_1)))
#b) Using list comprehension print string which contain 'a'
print([x for x in list_1 if isinstance(x, str) and 'a' in x])

print(tuple(['cat', 'dog', 'horse', 'cow']))


# 3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж
animals_list = ['cat', 'dog', 'horse', 'cow']
animals_tuple = tuple(animals_list)
print(animals_tuple)
# 3.4. Напишите программу, которая определяет, какая семья больше. 
#       1) Программа имеет два input() - например, family_1, family_2. 
#       2) Членов семьи нужно перечислить через запятую. 
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
members_1 = input("Введите членов первой семьи через запятую: ").split(',')
members_2 = input("Введите членов второй семьи через запятую: ").split(',')
members_1 = 'mama, papa, ja'
members_2 = 'uncle', 'aunt'
if len(members_1) > len(members_2):
    print(f" {members_1}")
elif len(members_2) > len(members_1):
    print(f" {members_2} ")
else:
    print("Equal")
# или второе решение от однокурсника
family_1 = list(input('Введите членов первой семьи через запятую: '))
family_2 = tuple(input('Введите членов второй семьи через запятую: '))
family_1 = 'mama, papa, ja'
family_2 = 'uncle', 'aunt'
print(type(family_1))
l_1 = len(family_1)
print(l_1)
print(family_1.split(', '))
print(type(family_2))
l_1 = len(family_2)
print(l_1)

#Solutions from RedRover
family_1 = tuple(input('Введите текст через запятую: ').split(','))
family_2 = tuple(input('Введите текст через запятую: ').split(','))
if len(family_1) == len(family_2):
    print('Equal')
elif len(family_1) > len(family_2):
    print('family_1')
else:
    print('family_2')

# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме. 
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение
dict = {'title': 'Qyz_Zhibek', 'director': 'Smailov', 'year': '1970', 'budget': '5', 
'main_actor': 'Utekeshova', 'slogan': 'Tolegen'}
print(dict.keys())
print(dict.values())
print(dict.items())

# 3.6. Найдите сумму всех значений в словаре  
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
total_sum = 0
for value in my_dictionary.values():
    total_sum += value
print(total_sum)

#Solutions from RedRover
# Option 1
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
result = 0
for x in my_dictionary:
    result += my_dictionary[x]
print(result)
# Option 2
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
print(sum(my_dictionary.values()))

# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
my_list = [1, 2, 3, 4, 5, 3, 2, 1]
unique_list = list(set(my_list))
print(unique_list)

#Solutions from RedRover
new_list = set([1, 2, 3, 4, 5, 3, 2, 1])
print(new_list)

# 3.8. Даны два множества: 
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах      
common_values = set1 & set2
print(common_values)
#     - найдите значения, которые не встречаются в обоих множествах  
diff_set1 = set1 - set2
diff_set2 = set2 - set1
result_set = diff_set1.union(diff_set2)
print(result_set)
#     - проверьте являются ли эти множества подмножествами друг друга
set1.issubset(set2)
set2.issubset(set1)

#Solutions from RedRover
# Option 1
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
print(set1.intersection(set2))
print(set1.symmetric_difference(set2))
print(set1.issubset(set2))
print(set2.issubset(set1))
# Option 2
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
print(sum(my_dictionary.values()))
