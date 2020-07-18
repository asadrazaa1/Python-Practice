import sys
#using iter(), next(), yield functions

temp_list = [1, 2, 3, 4, 5]
it = iter(temp_list)
print(next(it))

def fibonacci(n):
	a, b, counter = 0, 1, 0
	while True:
		if(counter > 0):
			return
		yield a
		a, b = b, a+b
		counter+=1
f = fibonacci(5)

while True:
	try:
		print(next(f), end = " ")
	except StopIteration:	
		sys.exit()
