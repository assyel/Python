# 1.1
#     1) Установите Python и PyCharm
#     2) Напишите и запустите программу. которая выводит строку  "Hello world!" 
print('Hello, world')
#     3) Напишите программу, которая на входе получает имя пользователя, cохраняет его в переменную user_name и выводит строку  "Hello {user_name}!" 
user_name = input('Please, enter your name: ')
print(f'Hello, {user_name}!')


# 4) Напишите программу, которая на входе получает 2 числа, производит с ними арифметическую операцию(на ваше усмотрение), и выводит “Результат = {результат}”.
num1 = int(input('Please, enter first number: '))
num2 = int(input('Please, enter second number: '))
result = num1 * num2
print(f'Результат = {result}')

# 1.2
#     1) Напишите программу, чтобы вывести:
      
# *********
# *            *
# *            *
# *********
#Option 1:
       print(‘*********’)
       print(‘*       *’)
       print(‘*       *’)
       print(‘*********’)
       
#Option 2:
      print('*********\n*       *\n*       *\n*********')

#Option 3:
      print("""
      *********
       *       *
       *       *
      *********
     """)
