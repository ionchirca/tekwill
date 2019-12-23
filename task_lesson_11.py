
'''1. Write a decorator that will print functions name and 
it’s attributes on call. Use func.__name__ attribute'''

# def funcName(func):
#     def wrap(*args, **kwargs):
#         func(*args, **kwargs)
#         print(func.__name__)   #retruneaza numele functiei chemate
#         print(*args, *kwargs) #retruneaza argumentele
#     return wrap

# @funcName
# def my_func(args):
#     pass

# my_func("None")


'''2. Create a decorator that will repeat function execution N times 
with X seconds delay. Use time.sleep() function.'''

# import time
# def repeat(n_times, x_delay):
#     def myDecor(func):
#         def wrap(*args, **kwargs):
#             for i in range(n_times):
#                 func(*args, **kwargs)
#                 time.sleep(x_delay)
#         return wrap
#     return myDecor

# #functia se executa de 5 ori cu un delay de 2 secunde intre fiecare executie
# @repeat(5,2)
# def my_func(name):                
#     print(f"My name is {name}")

# my_func("Ian")

'''3. Write a decorator for division function 
@zero_divisor_decorator
def divisor_function(number, divisor): 
return number / divisor
In case of ZeroDivisionError print a message that Division by 0 is not allowed.
'''
from functools import wraps

def zero_divisor_decorator(func):
    '''Acest decorator din functools ia careva atribute adaugatoatre din 
    functia decorata, spre exemplu documentatia si o asigneaza functie cu care
    decoram (spam).'''
    
    @wraps(func)
    def spam(number, divisor):
        '''Doc for func spam()'''
        try:
            print(f"Result is {number / divisor}")
        except ZeroDivisionError:
            print("Division by zero is not possible")
    return spam
    

@zero_divisor_decorator
def divisor_function(number, divisor):
    '''This func returns de result of division '''
    return number / divisor

divisor_function(4, 8)
divisor_function(4, 0)

#Fara @wraps la chemarea print(divisor_function.__doc__) => Doc for func spam()
#Cu @wraps la chemarea print(divisor_function.__doc__) => '''This func returns de result of division '''
print(divisor_function.__doc__)
