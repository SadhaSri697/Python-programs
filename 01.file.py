# file is used to write and read program and store it 
# RAM is random access Memory which is temporary for example c compiler we write the program which Can't be stored
# So to store the program we use file example vs code
# And also there are other files where we can store different things for example 
# to store a songs we will use MP3 files and also we can use other files to store them
# RAM - Volatile (can store temporary)
# HDD - Non Volatile (it is perminate) Ex: Pen Drive
# So HOW TO READ PROGRAM
# i created a file named 02.file.txt now to read it
# to read file 
f = open("file.txt") #open is built in function
data = f.read()
print(data)
f.close()            # we SHOULD close file