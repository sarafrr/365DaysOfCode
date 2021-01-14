# set and frozenset
# set: set of unique objects (the objects have to be ashables)
# frozen set: a set in which the objects cannot be changed

set0 = {1,2,3,4}
print("The set is made of not ordinate elements")

# the null set cannot be defined with the curly brackets,
# for it is already the definition of the null dictionary.
# It is possible to use @set()@
set1 = set()
print('Empty set: ', set1)
# to create a frozenset we have to use @frozenset()@

set2 = {1,1,1}
print('Duplicate elements are automatically removed in a set: ', set2)

print("Dimension of the set0: ", len(set0))
print("Minimum in the elements of the set0: ", min(set0))
print("Maximum in the elements of the set0: ", max(set0))
tmp = (0 in set0)
print('The element "0" is in the set0? ', tmp)

set0.add(0)
set3 = set0.copy()
print('Set3: ', set3)
set3.remove(0)
print('Set3: ', set3)
set3.discard(0) # does not launch an exception if there isn't in the set the element
                # which we want to remove
print('Set3: ', set3)
# set3.remove(0) # launch an exception if the element is not present
set3.clear()
print('Set3: ', set3)

print('set0 and set1 are disjoint?', set0.isdisjoint(set1))

print('set0 is a subset of set1?', set0.issubset(set1))
# many other operations on the subsets

setf = frozenset(set0.copy())
# setf.add(0) # it launches an exception because a frozenset cannot be changed

