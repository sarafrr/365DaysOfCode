# modules
# if we quit from the python interpreter and we re-enter all the definitions
# we have made are lost.
# So if we want to write a longer program, it is better
# to make a file that is the input for the interpreter

# in general such files are created if we have multiple definitions
# which can be useful.
# Such file can be IMPORTED into other modules or into the main module:
# in another file we can use @import day32@ and so we can use
# the functions which are present in this file

# we can import all the names the modules define with the *
# @from day32 import *@,
# but it is not suggested. It is suggested
# to give an alias name @import module as md@


def sum_numbers(x,y):
    return x + y


def print_fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a)
        a,b = b,a+b
