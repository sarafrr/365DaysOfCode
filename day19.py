# data structures - lists

names = ['bob', 'alice', 'peter', 'sarah', 'alice', 'bob']
print('N. times of "alice" in the list: ', names.count('alice'))
print('index fo the next realization of "alice"', names.index('alice',2))
# we can choose a part of a list where to search the index of
# the first realization of an item of the list
print('index fo the first realization of "alice"', names.index('alice',1,4))
# to reverse the list sequence, @reverse()@ is used
names.reverse()
print(names)
# to append a name at the end of the list, @append()@ is used
names.append('john')
# names[len(names):]=['john'] # raw append
print(names)
# to sort the names in an alphabetical order, @sort()@ is used
names.sort()
print(names)
# to remove the last element of the list and to return it, @pop()@ is used
print(names.pop())
print(names)
# we can remove a specific item from the list at a certain index
# and it is returned as well
print(names.pop(1))
print(names)
# to remove the first realization of an item
# from the list
names.remove('bob')
print(names)
# @insert()@ has as first parameter the index before which
# we want to insert the item
# So, to insert at the front of the list 0 is the index used
# and len(list) is the index used to insert at the end of the list
# which is the index just after the last element
names.insert(0,'tatiana')
print(names)
names.insert(len(names),'carl')
print(names)
# @copy()@ gives a shallow copy of the list
names2 = names.copy()
names3 = names.copy()
names.extend(names2)
names3[len(names3):] = names2
print('Extended list: ', names)
print('Extended list using a "raw extension": ', names3)
# to clear all the items of a list
names.clear()
print(names)
