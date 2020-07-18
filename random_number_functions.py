import random
#random item from a tuple, list or a string
print(random.choice(range(100)))
#a randomly selected element from  a range(start, stop, step)
print(random.randrange(1, 100, 2))
#printing a floating number randomly between 0 and 1
print(random.random())


print(random.seed(10))
print(random.seed())
print(random.seed("gello", 2))

#randomizes the items of a list, returns nothing
temp_list = [1,3,4,5,6,7]
print(random.shuffle(temp_list))

print(random.uniform(5,10))
