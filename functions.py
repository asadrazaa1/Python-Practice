#without parameters
def funct_1():
	"function docs string" #one line after each function can be description of the function
	print("This is function 1")

#without parameters, function does have local variables
def funct_2(string_1):
	print(string_1)
	return

#keyword arguments
#required arguments
def printme(string_2):
	print(string_2)
	return

#default arguments
def printinfo(name, age = 40):
	print(name + " " + str(age))
#variable length arguments
def printdouble(arg1, *vartuple):
	for var in vartuple:
		print(var)
	return
#anonymous functions
addition = lambda arg1, arg2 : arg1 + arg2



if __name__ == '__main__':
	funct_1()
	funct_2(string_1 = "This is second function")
	printme("This is third function")
	printinfo(name = "asad", age = 50)
	printdouble(10, 20, 30)
	print(addition(40,20))


#i know the concept of local variables and global variables
