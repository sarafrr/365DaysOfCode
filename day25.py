# python json
# string -> json
# json -> string

# json is a good file format for storing and exchanging data
# it is written with JavaScript Object Notation (JSON)
# in general, the module is contained by default in the standard
# installation of python
import json

# from json to python (dictionary)
x = '{ "name":"Bob", "age":29, "city":"Padua"}'
# parse x and the result is s python dictionary

y = json.loads(x)
print("json string: ",y, "\n")

print(y["name"])
print(y["age"])
print(y["city"],"\n")

# from python (dictionary) to json
# we define a dictionary
x = {"name" : "Bob", "age" : 29, "city" : "Padua"}

# convert into json
# we can use @indent@ parameter to set the number of indents
# , and space to separate each object and : and space to separate
# the values from keys (these are the default separators
# which are implemented, but we can change these as we want)
y = json.dumps(x, indent=3, separators=("; ", "= "))

# finally, we obtain a json string
print(y)
