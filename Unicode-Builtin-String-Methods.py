import base64
temp_str = "This is a sample string"
#capitalizing all the elements of string
print(temp_str.capitalize())

#returns a string will specified character filled at start and end of the original string
temp_str_2 = "This is second sample string..!"
print(temp_str_2.center(len(temp_str_2)+10, 'a'))

#return the number of occurances of substring sub inthe range[start,end]
#syntax str.count(sub, start=0, end=len(string))
temp_str_3 = "this is third sample string"
#print(temp_str_3.count('i', start=0, end=len(temp_str_3)))

#implemented encode() method too!
#decode() method decodes the string using the codec registed for the encoding, it defaults to the default string encoding
#syntax str.decode(encoding='UTF-8', errors='strict')
#temp_str_4 = "This is the fourth temp string"
#temp_str_4 = temp_str_4.encode('base64', 'strict')
#print("Encoded: " + temp_str_4)
#print("Decoded: " + temp_str_4.decode('base64', 'strict'))


#string endswith() method, returns either true or false
temp_str_5 = "This is fifth temp string..!!!"
suffix = "!!"
print(temp_str_5.endswith(suffix))
print(temp_str_5.endswith(suffix, 0, 20))

#string index() finder
#string find() method, return the index if found otherwise -1
temp_str_6 = "This is sixth sample string"
#print(temp_str_6.rfind('sam', beg=0, end=20))
print(temp_str_6.index('sam'))

#isalnum() method checks whether the stirng consists of alphanumberic characters 
print(temp_str_6.isalnum())

#isalpha() to check whether the sting consists of alphabets only
print(temp_str_6.isalpha())

#isdigit() checks whether the string consists of digits only
print(temp_str_6.isdigit())

#islower()
print(temp_str_6.islower())
#isnumeric()
print(temp_str_6.isnumeric())
#to check whether it is a space or not, returns either true or false
string_space = "        "
print(string_space.isspace())

#istitle()
temp_string_6 = "This is a temp string"
print(temp_string_6.istitle())
print(temp_string_6.isupper())
print(temp_string_6.islower())


#joining sequence
joiner = '-'
seq = ("a", "b", "c") 
print(joiner.join(seq))
print(len(temp_string_6))

#ljust()
print(temp_string_6.ljust(50, '*'))


#stripping specific characters from a beginning, if not specified, it will remove space in the start

temp_string_8 = "*****This is a sample string*********"
print(temp_string_8.lstrip('*'))


#The maketrans()methodreturns  a  translation  table  that  maps  each  character  in  the intabstring into the character at the same position in the outtab string. Then this table is passed to the translate() function.
#note both intab and outtab must have same length
intab = "aeiou"
outtab = "12345"
my_string = "A Quick brown fox jumped"
transition_table = my_string.maketrans(intab, outtab)
print(my_string.translate(transition_table))


#printing maximum and minimum character from a string
my_str = "A quick brown fox jumped over a lazy dog"
print(max(my_str))
print(min(my_str))

#usage of replace function
new_str = "This is a sample string = ---- this is really a sample string"
print(new_str.replace("is", "was"))
print(new_str.replace("is", "was", 3))


#using split function
new_str_1 = "This is a sample string...wow"
print(new_str_1.split( ))
print(new_str_1.split('i', 1))
print(new_str_1.split('w'))

#using split lines
tmp_str = "This is \nstring \nwith lines"
print(tmp_str.splitlines())

print(tmp_str.startswith('This'))

print(tmp_str.strip('s'))

#swapcase replace all the lower case alphabets into upper case and vice versa
print(tmp_str.swapcase())

#zerofiller
print(tmp_str.zfill(50))

print(tmp_str.isdecimal())


























print("Ending")
