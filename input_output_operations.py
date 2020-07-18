import os
#reading and writing operating on a text document
file = open("text.txt", "r+")
print("File name: ", file.name)
print("File mode: ", file.mode)
print("Closed or not: ", file.closed)


string_temp = file.read(10)
print("Text within file: ", string_temp)
postion = file.tell()
print("Position inside the file ", postion)

rest_postition = file.seek(0,0)
print("New postion is : ", rest_postition)
print(dir(os))
	








#closing opened file
file.close()