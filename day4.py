# lambda expressions
# small anonymous functions can be created thanks to lambda expressions
# It is necessary to use a single expression

def make_incrementer(n: int) -> int:
    return lambda x: x+n


f = make_incrementer(10)
print(f(0))
print(f(1))

# Documenting strings
# first line has to be always a summary of the
# object purpose
# Start with a capital letter
# After the first row of summary use a blank line
# Then, do paragraphs to document the function

def my_function():
    """Do nothing, but document it.

    It does not do anything!
    """
    pass

print(my_function.__doc__)

# Function annotations are optional metadata
# we use a semicolon after the name of the parameters and then the type
# and for the returned value we use an arrow and then the type
# see the function make_incrementor

print(make_incrementer.__annotations__)
