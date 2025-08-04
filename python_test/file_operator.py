# to write to a file in Python
# open the file in write mode it will create the file if it does not exist
# and if it exists it will overwrite the file

f = open("myfile.txt","w")


str = input("Enter text:")

f.write(str)

f.close()

# # to read from a file in Python
# # open the file in read mode
# # it will throw an error if the file does not exist
f = open("myfile.txt","r")
# read the file
str=f.read()
print(str)
f.close()

# to append to a file in Python
# open the file in append mode it will create the file if it does not exist
# and if it exists it will append to the file
f = open("myfile.txt","a")
str = input("Enter text:")
f.write(str + "\n")
f.close()

f = open("myfile.txt","r")
# read the file
str=f.read()
print(str)
f.close()

# to write and read from a file in Python
# open the file in write mode it will create the file if it does not exist
# and if it exists it will overwrite the file
# then we will read from the file
f = open("myfile.txt","w+")
str = input("Enter text:")
f.write(str + "\n")
f.seek(0)  # Move the cursor to the beginning of the file
str = f.read()
print(str)
f.close()

# to read and write from a file in Python
# throws error the file if it does not exist
# if data is present in file it wil append to the begining file
f = open("myfile.txt","r+")
str = input("Enter text:")
f.write(str + "\n")
str = f.read()
f.seek(0)
print(str)
f.close()


# to append and read from a file in Python
# open the file in append mode it will create the file if it does not exist
# and if it exists it will append to the file
f = open("myfile.txt","a+")
str = input("Enter text:")
f.write(str + "\n")
f.seek(0)  # Move the cursor to the beginning of the file
str1 = f.read()
print(str1)
f.close()

# to create a file in Python
# open the file in exclusive creation mode it will create the file if it does not exist
# and if it exists it will throw an error
# this is useful to create a file only if it does not exist and it is naot readable
f = open("myfile1.txt","x")
str = input("Enter text:")
f.write(str)
f.close()
