# Sets
# Set is a collection of items. Let me take you back to your elementary or high school 
# Mathematics lesson. The Mathematics definition of a set can be applied also in Python. 
# Set is a collection of unordered and un-indexed distinct elements. In Python set is used to store unique items, 
# and it is possible to find the union, intersection, difference, symmetric difference, subset, suSets
# Set is a collection of items. Let me take you back to your elementary or high school Mathematics lesson. The Mathematics definition of a set can be applied also in Python. Set is a collection of unordered and un-indexed distinct elements. In Python set is used to store unique items, and it is possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.per set and disjoint set among sets.


st=set()
#or
st={1,2,3,4,5}

print(len(st))

print(1 in st)

st.add(6)

print(st)

st.update([7,8,9])

print(st)

st.pop()

print(st)

del st

print(st) # This will raise an error because the set has been deleted