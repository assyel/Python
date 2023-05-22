#Decorators
# 1. Functions are objects
def add_five(num):
    print(num + 5)
add_five(2)
# if we print out without parenthesis, we actually get results 
# мынандай <function add_five at 0x10cd45cf0>. Basically 
# this function is OBJECT, яғни string, number, list тб болуы мүмкін
print( add_five )
# енді parenthesis пен жасасақ
print( add_five(5) )

# 2. Functions within functions
def add_five(num):
    def add_two(num):
        return num + 2
    num_plus_two = add_two(num)
    print(num_plus_two + 3)
add_five(10)
# if we try to call add_two it gives us an error. NameError: name 'add_two' is not defined
# add_two(7)

# 3. Returning functions from functions
def get_math_function(operation): # + or - we are gonna define 2 functions
    def add(n1, n2):
        return n1 + n2
    def sub(n1, n2):
        return n1 - n2
    if operation == '+':
        return add
    elif operation == '-':
        return sub
add_function = get_math_function('+') # call get_math_function with 
### plus. get_math_function creates inside two functions. if we print 
### out add_function it should be function because we return a function.
print( add_function(4, 6) ) # результат 4+6=10
sub_function = get_math_function('-')
print( sub_function(4, 6) ) # результат 4-6=-2

### 4. Decorating a function
#def print_my_name(): # this function is gonna print my name
    #print('Assel')
#print_my_name() 
### We can make it more powerful using Decorator. Decorator is basically a 
### function. We'll add some functionality.
def title_decorator(print_name_function):
    def wrapper():    # this will wrap below codes
        print('Miss:')
        print_name_function()
    return wrapper
def print_my_name(): ### this function is gonna print my name
    print('Assel')
def print_joes_name():
    print('Joe')
#decorated_function = title_decorator(print_my_name) ### мұнда титул мен атым тұр
decorated_function = title_decorator(print_joes_name)
#print_my_name()
decorated_function()

# 5. Decorators
def title_decorator(print_name_function):
    def wrapper():    # this will wrap below codes
        print('Doctor:')
        print_name_function()
    return wrapper
@title_decorator
def print_my_name(): ### this function is gonna print my name
    print('Assel')
@title_decorator
def print_joes_name():
    print('Joe')

print_my_name() ### или
print_joes_name()
### Through *args, **kwargs we can add names to our decorator as many arguemtns as we want
def title_decorator(print_name_function):
    def wrapper(*args, **kwargs):    
        print('Doctor:')
        print_name_function(*args, **kwargs)
    return wrapper
@title_decorator
def print_my_name(name): 
    print(name)

print_my_name('Shelby') 

###as many arguemtns as we want with *args, **kwargs
def title_decorator(print_name_function):
    def wrapper(*args, **kwargs):    
        print('Doctor:')
        print_name_function(*args, **kwargs)
    return wrapper
@title_decorator
def print_my_name(name, age): 
    print(name + ' you are ' + str(age))

print_my_name('Shelby', 50) 



