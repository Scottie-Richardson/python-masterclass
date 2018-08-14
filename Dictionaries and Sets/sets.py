# To create a set you use {} just like with dictionaries except
#   you do not give it a key-value pair, you only seperate the
#   values with a comma. You can also create a set from any
#   iterable data type i.e. lists, ranges, tuples etc. using the
#   set() constructor. However to initialize an empty set you
#   have to use the constructor instead of the {}. You can also
#   add elements to a set using the .add() method
letter_set = {'a', 'b', 'c', 'd', 'e'}
empty_set = set()
print("Letter set:", end=" ")
print(letter_set)
print("Empty set:", end=" ")
print(empty_set)

empty_set.add('new_element')
print("Empty set with element added:", end=" ")
print(empty_set)

example_tuple = (1, 3, 5, 7, 9)
set_from_tuple = set(example_tuple)
print("Set created from a tuple:", end=" ")
print(set_from_tuple)

# Set operation methods:
#   To return the combination of two sets
#           x.union(y)

#   To return only the elements that appear in both x and y
#           x.intersection(y)
#               or x & y

#    To return the elements that only appear in x and not y
#           x.difference(y)
#               or x - y

#    To return all elements from both sets minus the elements that
#        appeared in both sets
#           x.symmetric_difference(y)

#    To update a set instead of creating a new one
#           x.union_update(y)
#           x.intersection_update(y)
#           x.difference_update(y)
#           x.symmetric_difference_update(y)

#   To remove an element from a set there are two methods:
#           Method 1: x.remove(target_element)
#           Method 2: x.discard(target_element)
#               Method 1 will cause an error if the target_element
#               did not already exist within the set where Method 2
#               will not cause an error

#   To test if a set is a subset or a superset of another
#           x.issubset(y)
#           x.issuperset(y)

#   To create an inmutable set
#           unchangable_set = frozenset(range(0, 100, 2))