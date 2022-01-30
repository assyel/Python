

#[Forwarded from Vadim_QA_Padawans_Channel]
#Python. HW_1

#1) Создать переменную типа String
a = 'kartoshka '
b = 'morkovka'
c = a + b
print('morkar ', c, type(c))


#2) Создать переменную типа Integer
a = 8
b = 9
c = a + b
print('integer', c, type(c))


#3) Создать переменную типа Float
c = 8 / 9
print('float', c, type(c))


#4) Создать переменную типа Bytes
plie = bytes(11)
print(plie,type(plie))


#5) Создать переменную типа List. Тип данных list, в отличие от массива, может иметь разного рода данных:
my_list = ['balet', 1, 5+3j, 8.08]
print('my_list', my_list, type(my_list))


#6) Создать переменную типа Tuple. It cant be modified as list. Tuple is immutable but list is mutable.
#List notation is [] but tuple notation is (). Some benefits of tuple:
#Light-weighted
#Work as constant
#Can be useful to make key for dictionary
#Single container etc.
jo = tuple('Assel')
print ('jo', jo, type(jo))

#7) Создать переменную типа Set. Set is an un-ordered and immutable data structure in python. This data-type can perform mathematical operation like set theory. The common mathematical operation of Set is Union, Intersection, difference etc.
set={'serotonin', 'Kazakh', 'beshbarmak'}
print('set =',  set, type(set))

#8. Создать переменную типа Frozen set. After creating a frozen set it cant be modified. This is immutable data structure.
simple_set = {'alma', 'shie'}
simple_set.add('Kazakh')
print('simple_set =', simple_set)
frozen_set = frozenset(['alma', 'shie', 'Kazakh'])
print('Frozen Set =', frozen_set)
simple_set.add('orik')
print('Updated Frozen Set =', frozen_set, type(frozen_set))
frozenset(['alma', 'shie', 'Kazakh'])

#9) Создать переменную типа Dict
di={
'Key':'value',
'name':'Kiki',
'age':'hundred'
}
di['Key']=0
#Add new Key to dict:
di['Location']='Kazakh'

print('dictionary', di['age'], type(di))
print(di)


#10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
# Уже выведены!!!)))


#11) Создать 2 переменные String, создать переменную в которой суммируете эти переменные. Вывести в консоль.
# Уже созданы!!!


#12) Создать 2 переменные Integer, создать переменную в которой суммируете эти переменные. Вывести в консоль.
# Уже созданы!!!


#13) Создать переменную в которой Разделите эти переменные Int. Вывести в консоль.
z = 15
y = 5
g = 5 / 15
print('razdelit =',  g)


#14) Создать переменную в которой Умножите эти переменные Int. Вывести в консоль.
f = 15 * 5
print('umnojit =',  f)


#15) Создать переменную в которой Разделите без остатка эти переменные Int. Вывести в консоль.
n = 15 // 5
print('razdelit bez ostatka = ',  n)


#16) Создать переменную в которой надо присвоить остаток от деления этих переменные Int. Вывести в консоль.
g = 5 % 15
print('ostatok ot deleniya = ', g)


#17) (7 + 12)  3 + 7 * 4 - 44 / 2  4 расставить точки так чтобы получилось 6884.25. Вывести в консоль.
w = (7 + 12)**3 + 7 * 4 - 44 / 2**4
print('w =', w)


#Выгрузить файл в Git репозиторий.

