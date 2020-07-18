diction_1 = {"Name" : "Asad", "Age":45, "Class":"10"}
diction_2 = {"Name" : "Raza", "Age":45, "Class":"Ms"}
diction_3 = {"Name" : "Jaferi", "Age":45, "Class":"Bs"}

#acessing values in the dictionaries
print(diction_1["Name"])
print(diction_1["Age"])

#updating dictionaries
diction_1["Age"] = 50
diction_1["Class"] = "Mathematics"

#deleting elements from the dictionaries
diction_1.clear() #remove all the elements within the dictionary
del diction_1

#keys cannot be duplicated within the dictionaries and keys are immutable
print(len(diction_2))


#this method returns string representation of the dictionary
print("Dictionary is : %s " % str(diction_2))

#dictionary type method, this method
print(type(diction_2))

#to remove all the elements from the dictionary
diction_2.clear()

#return the shallow copy of the dictionary
diction_4 = diction_3.copy()

#getting keys from a tuple
seq = ('name', 'age', 'sex')
dict_9 = dict.fromkeys(seq)
print ("New Dictionary : %s" %  str(dict_9))
dict_9 = dict_9.fromkeys(seq, 10)
print ("New Dictionary : %s" %  str(dict_9))


#returns the value for the key
print(diction_2.get('name'))
print(diction_2.get('sex', 'blah'))

#returns the value and key in the form of tuple pairs
print(diction_3.items())

#return all the keys of the dictionary
print(diction_.ke3ys())

#adding new keys in the dictionary, if the key alreay exists in the dictionary, then it will return the value of the key within the function
print(diction_3.setdefault('city', None))

#dictionary update method
diction_7 = {"name":'asad', 'age':56}
diction_8 = {'sex':"male"}
diction_7.update(diction_8)
print(diction_7)

#values() function return all the values within the dictionary
print(list(diction_7.values()))