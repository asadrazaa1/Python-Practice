tup1 = ("11", "12", "13", "14", "15")
tup2 = (1, 2, 3, 4, 5)
tup3 = 'a', 'b', 'c', 'd', 'e'

#empty tuple is written with empty parantheses tuple = ()
#for a single valued tuple, you have to add a comma after the element
tup4 = (20, )

#acessing values within the tuple
print(tup1[0])
print(tup1[1:4])
print(tup1[:3])

#updating values within the tuple is not possible, tuple are solid state object
tup5 = tup1 + tup2

#deleting any element from the tuple
del tup1

print(max(tup2))
print(min(tup2))
print(len(tup2))