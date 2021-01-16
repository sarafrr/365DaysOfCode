# the classes in Python are defined in CamelCase
# attributes in snake_case
class Test:
    # class attributes
    n_students = 10
    # methods are properties of a class.
    # They have always at least one parameter which is @self@
    # which has to be the first argument

    # pay attention that the method __init__ is called
    # each time an object of its class is created.
    # It is only a method for initializatiion,
    # not for creation
    def __init__(self,name='default_name'):
        print('The object as been created!')
        self.name = name

    def get_info(self):
        print('The instance is: ', self)

    def print_name(self):
        print(self.name)



# we can create different objects of the class Test,
# indeed they refer to different areas of memory
t = Test()
print(t)
print(t.name)

t2 = Test('alice')
print(t2)
print(t2.name)

t.get_info()
t.print_name()
# we modify the attribute name of the instance
t.name = 'bob'
t.print_name()

# we can add out of the declaration of the class
# other attributes, but we advise against this usage
# for we can have instances of the same class with different
# attributes

print(dir(t), "\n")
t.level = '1rst year student'
print(dir(t), "\n")

# the class attributes are independent from
# the realization of the class (they are independent
# from the instances)
print('Number of students: ', Test.n_students)