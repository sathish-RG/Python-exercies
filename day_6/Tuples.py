
# A tuple is a collection of different data types which is ordered and unchangeable (immutable). Tuples are written with round brackets, (). Once a tuple is created, we cannot change its values. We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable). Unlike list, tuple has few methods. Methods related to tuples:

# tuple(): to create an empty tuple
# count(): to count the number of a specified item in a tuple
# index(): to find the index of a specified item in a tuple
# + operator: to join two or more tuples and to create a new tuple

empty_tuple=()
#or
empty_tuple=tuple()

fruits=('banana','orange','mango','lemon')
print(len(fruits))

print(fruits[1])

fruits=list(fruits)
fruits[0]='apple'
print(fruits)

print('orange' in fruits)