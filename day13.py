# dictionars
# 2 elements for an item: key and value
# they are implemented using the hash tables
# for they are very efficient in giving the respective value
# of a key in a very efficient way, independently by the number
# of elements in the dictionary

d = {'a': 1, 'b': 2, 'c': 3}
print(d)
print(type(d))

# the keys in general are strings, but we can use other
# types of data if they are "hashable"
# which means that they have a value which does not change during
# its lifetime

# to have the value identified by its key
print(d['a'])

print("The key 'd' is present? ", ('d' in d))
print("The key 'd' is not present? ", ('d'not in d))

# add a couple key and value
d['d'] = 10
print("The key 'd' is present? ",('d' in d))

# overwrite a value referred with a key
d['d'] = 11
print("New value of 'd': ", d['d'])

# remove a couple key and value
del d['d']
print("The key 'd' is not present? ", ('d'not in d))
print("Items of the dictionary: ", d.items())
print("Keys in the dictionary: ", d.keys())
print("Values in the dictionary: ", d.values())

tmp = d.get('a')
print("Element with key 'a': ", tmp)

# we remove the couple with key value 'a' and it is returned by @pop()@
tmp = d.pop('a')
# we remove a couple chosen randomly and it is returned by @popitem()@
tmp = d.popitem()

d2 = d.copy()
# we add the elements of a dictionary to another dictionary
d.update(d2)
print("Items of the new dictionary: ", d2.items())
d.clear()
