list_1 = ["Physics", "Chemistry", 1990, 2001]
list_2 = [1, 2, 3, 4, 5]
list_3 = [1, 2, 3, 4, 5]
print("List 1: ", list_1[0])
print("list_2: ", list_2[1:5])

#delete any element from the list
print("Before deleting : ", list_1)
del list_1[0]
print("After deleting : ", list_1)

#basic list operations
print(len(list_1))
print(list_2 + list_3)
print(list_1*2)
print(3 in list_2)


#indexing
print(list_1[:3])
print(list_1[2])
print(list_1[-2])
print(list_1[1:])


#built in functions and methods
print(len(list_1))
#print(max(list_1))
#print(min(list_1))

#creating a list using range function
list_4 = list(range(10))
print(len(list_4))

#methods
#appending a list
list_2.append(12)
print(list_2)
#counting an element from the list or frequency of any element from the list
list_1.count(1)
print(list_2.extend(list_4))

#printing the index of any element from the list
print("Index of 3 in list_2 is: ", list_2.index(3))

#inserting any element at any index
print(list_2.insert(1, 45))

#pop operations on the list, this method returns the removed element
new_list = [11, 22, 33, 44]
print(new_list)
new_list.pop()
print("After pop operation without specified index: ", new_list)
new_list.pop(2)
print("Pop at a specific index: ", new_list)


#remove() function works the same as the pop, the only difference is that it doesnot return any thing.
new_list_1 = ["Physics", "Chemistry", "Biology", "Maths"]
(new_list_1.reverse())
print(new_list_1)

#hash tag sorting in a single line
(new_list_1.sort())
print(new_list_1)
