real_number = 2
decimal_number = 2.3
string = "this is string"
string_real_number = "2"
string_decimal_number = "2.2"
calculating = "2+3"
char = 'A'
s = [2,3,4]
s_temp = [21,31,41]
s_b = (1,2,3)
dictionary={1:"asad", 2:"raza"}
#string to integer conversion
print(int(string_real_number))

#string to float conversion
print(float(string_decimal_number))

#creating a complex number
print(complex(real_number, real_number)) 

#integer, float to string conversion
print(str(real_number))
print(str(decimal_number))

#converting an object to expression string
print(repr(string))

#evaluating a string
print(eval(calculating))

#converting to a tuple
print(tuple(s))

#converting to a list
print(list(s_b))

#converting to a set
print(set(s_temp))

#creating a dictionary, d must be sequence of keys and values
#print(dict(d))

#converting an integer to a character
print(chr(real_number))

#converting integer to a unicode
#print(unichr(real_number))

#converting a string character to a its integer value
print(ord(char))

#converting an integer to its hexadeciaml form
print(hex(real_number))

#converting an integer to its octal state
print(oct(real_number))




















