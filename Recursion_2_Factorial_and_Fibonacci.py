# Recursion_нахождение факториала
#1 Разберем самую классическую задачу на рекурсии - это 
# нахождение факториала.
    # как находить факториал на примере 5! - это последовательное 
    # произведение всех чисел от 1 до 5. Но если приглядеться, то 
    # 5! включает в себя нахождение 4!, умноженное на 
    # число 5: 4! * 5, то есть 5! = 1*2*3*4*5=4!5 (4*5). В свою очередь 
    # 4! - это последовательное произведение всех чисел от 1 
    # до 4, в которого входит факториал 3!*4=1*2*3*4 (3*4). Дальше 
    # 2!*3=1*2*3 (2*3) и так когда дойдет до 1, то он выйдет из 
    # рекурсии. А когда факториал не равен 1, то мы его ищем последующей 
    # формуле: n! = (n-1)!n. И вот в левой крайне и правой крайней мы 
    # видим факториал. 
    # В этом примере мы можем разобрать вторую составляющую 
    # рекурсию. Если у вас есть какая то большая задача, как, например, найти 
    # n факториал, вы можете рекурсивно свести ее к поиску более 
    # меньшей подзадачи, в которых будет сводится еще более мелкие и тд. 
    # и стремится к выходу. В нашем случае чтобы найти 5! мы 
    # должны найти 4! и умножить его на 5, 4! будет просить нас найти 
    # 3!, который будет просить 2!, дальше 1! и мы выйдем из рекурсии. 
    # а потом обратно также будем возвращаться.
def fact(x):
    # и значит внутри функции мы сперва проверяем на выход, если x == 1, то 
    # мы возвращаем значение 1!, а в противном случае мы вызываем нашу 
    # функцию fact() и передаем ей аргумент на единичку меньше и это 
    # значение по формуле мы должны умножить на x
    if x ==1:
        return 1 
    return fact(x-1)*x
# и вызовем эту функцию и получаем результат 24.
print(fact(4))
# обьясняем. мы вызываем f(4) = f(4-1=3)*4. в свою очередь f(3) будет 
# равна f(2)*3, f(2) тоже вызывает f(1)*2, а f(1) возвращает 
# единицу 1. и соответственно мы возвращаемся здесь назад: 1*2=2, 
# полученное 2*3=6 вышестоящее, и 6*4=24

#2 классическая задача No2 Fibonacci 
# Числа Fibonacci представляют собой ряд числе, в к ром есть начальнЫЕ 
# значенИЯ и они равны 0 и 1. А далее каждое следующее число надо найти 
# путем сложения двух предыдущих, то есть это число путем сложения 0+1=1, 
# далее последние стоящие еднерки сложим: 1+1=2, затем последние стоячие 
# 1+2=3, затем 2+3=5, затем 3+5=8, затем 5+8=13 и тд можно продолжать 
# бесконечно: 0, 1, 1, 2, 3, 5, 8, 13. у каждого полученного числа есть 
# свой порядковый номер от 1 до 8 в данном случае. Если мы обозначим за 
# функцию f() наше число fibonacci как f(7), в скобках указан порядковый 
# номер fibonacci, то чтобы найти 7ое число мы предыдущее число 6 сложим 
# с 5ым числом: f(7)=f(6)+f(5), так как 6-ое число нам неизвестно, оно нас 
# попросит найти 5-ое число и сложить его 4-ым, а рядом стоящая f(5) 5 попросит 
# найти предыдущее число и тогда сложим предыдущее число с еще ранее стоящим 
# числом: f(5)=f(4)+f(3), и так далее будем рекурентно находить, пока не 
# найдем наш базовый ответ. f(4)=f(3)+f(2). Нашим базовым ответом являются 
# 0, 1, эти числа являются числами fibonacci. и значит формула f(n)=0, n = 1 
# или f(n) = 1, n = 2, а в остальных случаях мы должны складывать предыдущее 
# число с пред предыдущим: f(n-1) + f(n-2), то есть этой формулой мы пользуемся для n > 2.
# назовем нашу функцию fib(n), которая принимает порядковый номер n
def fib(n):
    # делаем условие на выход на порядковый номер единица, то число равно 0
    if n == 1:
        return 0
    # если порядковый номер равен к двум, возвращаем 1
    if n == 2:
        return 1
    # а во всех остальных случаях мы рекурентно вызываем эту же самую 
    # функцию но от параметра на единичку меньше и складываем с этой 
    # же функцией от параметра на 2 меньше
    return fib(n-1)+fib(n-2)
# и здесь вызываем функцию от 5, получим 3
print(fib(5))
# если вызывать от 6 и 7, то получим соответственно 5 и 8
print(fib(6))
print(fib(7))
# yj здесь важно понимать как происходит вызовы внутри этой 
# функции: на примере f5 по определению мы должны сложить 4 с 
# 3, но по формуле рекурсии мы СПЕРВА вызовем f4ое число, а 
# 4ое вызовет нам f3, а f3 вызовет f2, а f2 у нас ровно единице 1. 
# но здесь 3ье еще параллельно вызовет первое, которые равняется 
# нулю. Эти значения складываются и подставляется вместо f3, то есть 
# обратно назад идет. но оно вызовет f2, а f2 равно единице 1. f3 нам 
# вернул 1 и f2 вернул 1, тогда 1+1=2, оно вернется к f5. а f5 еще 
# должно было вызвать f3. а f3 вызывает параллельно f2, которое равно 1 
# и f1, которое равно 0, отсюда 1+0 складываем и это значение возвращает 
# нам 1. и значит 2+1=3.

