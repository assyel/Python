#Functions. Operator return 
# 3 
# def square(x):
#     # print x во второй степени
#     print(x**2)
    # первая строчка к рая вызывается это 6. 
    # передаем ей значение 6, она идет в 
    # переменную x, x в квадрате будет 36 и выходим из функции. 
    # после выхода  выводим значение переменную а.  
    # получаем значение None. Откуда это значение None 
    # взялось? - Любая функция в Python возвращает какое л 
    # значение при помощи команды return. Но если return не указан, 
    # то наша функция возвращает None.
# a = square(6)
# print(a)
# 4 вообще с оператором return она выглядит так:
def square(x):
    print(x**2)
    return None
a = square(7)
print(a)
# 5 чтобы получить желаемый результат 
# напишем следующий код без print внутри функции:
# def square(x):
#     return x ** 2
# a = square(6)
# print(a)
# 6 
def example():
    print(1)
    print(2)
    # как только мы добавили команду return, 
    # выход автоматически получится из функции.
    # выодятся значения стоящие до первого return. 
    # 'hello' сам не вывелось, так как мы ничего не 
    # сделали, п ч мы ничего не сделали со значением, 
    # к рое возвращает функцию. чтобы вызвать, 
    # мы должны обернуть example в команду print.
    return 'hello'
    return 3
    print(3)
    print(4)
#example()
# после первого return ничего не выводится
print(example())
# 1 встроенные функции. abs это absolut возвращает модуль числа
# a = abs(-7)
# 2 также внутри функции можем 
# вызвать другие функции. Как в математике, 
# сперва будут вызывать функции в скобках, соответственно 
# первая функция, к рая вызовется это abs(-90).
#это пример на возвращаемое значение, к рое 
# подставляется на место вызова функции
# b = max(4, abs(-90), 4, min(100, 200))
# print(a)
# print(b)
# 7 новый код с функцией и опреатором return
# def even(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
# короткий вариант написания кода:
def even(x):
    return x % 2 == 0
        
for i in range(1, 11):
    print(i, even(i))

# 8 новый код
def factorial(x):
    # показываем что надо от одного???
    pr = 1
    for i in range(2, x+1):
        pr = pr*i
    # убрали эту строчку print(pr)
    return pr
# 9 давайте проверим. найдем 
# факториал от 1 до 7 включительно
for i in range(1, 8):
    # выводим переменную i, и 
    # вызываем функцию factorial и 
    # передаем ей эту переменную i
    print(i, factorial(i))
# 10 при помощи функции factorial(), 
# легко можем создать функцию сочетание
def sochet(n, k):
    # формула сочетания числа C(n,k) = n!/k!(n-k)!.
    # здесь factorial 5 = 120, factorial 3 = 6, 
    # и 5-3=2 и тогда factorial 2. 120/(6*2)=10
    return factorial(n)/(factorial(k)*factorial(n - k))
#print(sochet(5, 3))
sochet(5, 3)

# 11 новый код. наша функция должна вызвать площадь и периметр
def sqAndPer(a,b):
    # пишем нахождение площади, то есть стороны переумножаем, 
    # и пишем формулу нахождения периметра
    return a*b, 2*(a+b)
# вызываем нашу функцию и передадим значения. результат возвращается в 
# виде кортежа tuples.
#sqAndPer(3, 6)
print(sqAndPer(3, 6), type(sqAndPer(3, 6)))

# 12 если вспомнить множественное присвоение, так как первым у нас возвращается 
# площадь return a*b (жоғарыда), создадим переменную square
square, perimetr = sqAndPer(2, 5)
#и давайте выведем эти переменные. запускаем. результат 10 и 14
print(square, perimetr)
# 13 из функции можно вывести любое значение
def sqAndPer(a, b):
    # создадим список
    mas = []
    # в список поместим нашу площадь 
    mas.append(a*b)
    # и еще в список поместим наш периметр
    mas.append(2*(a+b))
    # и возвращать будем только одно значение. это наш список
    return mas
# результат [12, 16] площадь и периметр
sqAndPer(2, 6)






    

