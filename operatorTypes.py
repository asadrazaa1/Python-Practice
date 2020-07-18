#arithmetic operators
print(2+3)
print(2-3)
print(2*3)
print(2/3)
print(2%3)
print(2**3)
#floor division
print(2//3)

#comparison operators
if(2>3):
	print("greater operator")
if(2<3):
	print("less than operator")
if(2!=3):
	print("not equal to  operator")
if(2<=3):
	print("less than and equal to operator")
if(2>=3):
	print("greater than and equal to operator")
#assignment operators
a = 10
b = 10
if (a==b):
	print("equal to operator")
a+=b
a-=b
a*=b
a/=b
a%=b
a**=b
a//=b
#logical operators
#assume ab = 60 and bc=13, ab=0011 1100, bc=0000 1101
ab = 60
bc = 13
#bitwise operations
#AND operation
print(ab&bc)
#OR operation
print(ab|bc)
#XOR operation
print(ab^bc)
#binary ones complement
print(~ab)
#printing binary of a number
print(bin(ab))
#binary left shift
cd = ab<<2
#binary right shift
dc = ab>>2

#membership operators are "in" and "not in"
temp_list = [20, 40, 60, 90]
var_1 = 20
var_2 = 100
if (a in temp_list):
	print("a is found in the list")
if (b not in temp_list):
	print("b is not found in the list")
#identity operators are "is" and "not is"
blah = 20
blahblah = 20
print(id(blah))
print(id(blahblah))
if(blah is blahblah):
	print("both variables have same identity")
if (blah is not blahblah):
	print("both variables do not have same identity")
	
	
#if else statements, nested if else statements

car1 = 11
car2 = 12
if (car1==car2):
	print("both cars are equal")
	if (car1>car2):
		print("standing inside if else statement")
	else:
		print("standing inside else statement")
elif (car1>car2):
	print("car1 is greater than car2")
else:
	print("both cars are not equal")





