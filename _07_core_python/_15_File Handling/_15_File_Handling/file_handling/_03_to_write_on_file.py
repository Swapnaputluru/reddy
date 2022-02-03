'''
Writing to file in Python
===========================

Opening a file
Closing a file
Writing to file
Appending to a file
With statement
Access mode
Access modes govern the type of operations possible in the opened file.
It refers to how the file will be used once it’s opened.
These modes also define the location of the File Handle in the file.
File handle is like a cursor, which defines from where the data has to be read or written
in the file. Different access modes for reading a file are –

Write Only (‘w’) : Open the file for writing. For an existing file, the data is truncated and over-written. The handle is positioned at the beginning of the file. Creates the file if the file does not exist.
Write and Read (‘w+’) : Open the file for reading and writing. For an existing file, data is truncated and over-written. The handle is positioned at the beginning of the file.
Append Only (‘a’) : Open the file for writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.
Note: To know more about access mode click here.

Opening a File
It is done using the open() function. No module is required to be imported for this function.

Syntax:

File_object = open(r"File_Name", "Access_Mode")
The file should exist in the same directory as the python program file else, full address of the file should be written on place of filename.

Note: The r is placed before filename to prevent the characters in filename string to be treated as special character. For example, if there is \temp in the file address, then \t is treated as the tab character and error is raised of invalid address. The r makes the string raw, that is, it tells that the string is without any special characters. The r can be ignored if the file is in same directory and address is not being placed.


# Open function to open the file "MyFile1.txt"
# (same directory) in read mode and
file1 = open("MyFile.txt", "w")

# store its reference in the variable file1
# and "MyFile2.txt" in D:\Text in file2
file2 = open(r"D:\Text\MyFile2.txt", "w+")
Here, file1 is created as object for MyFile1 and file2 as object for MyFile2.

Closing a file
close() function closes the file and frees the memory space acquired by that file. It is used at the time when the file is no longer needed or if it is to be opened in a different file mode.

Syntax:

File_object.close()

# Opening and Closing a file "MyFile.txt"
# for object name file1.
file1 = open("MyFile.txt", "w")
file1.close()
Writing to file
There are two ways to write in a file.



write() : Inserts the string str1 in a single line in the text file.
File_object.write(str1)

writelines() : For a list of string elements, each string is inserted in the text file.
Used to insert multiple strings at a single time.
File_object.writelines(L) for L = [str1, str2, str3]
Note: ‘\n’ is treated as a special character of two bytes.

'''


# Python program to demonstrate
# writing to file

# Opening a file
file1 = open('myfile.txt', 'w')
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
s = "Hello\n"

file1.write(s)  # Writing a string to file
file1.writelines(L)  # Writing multiple strings
# Closing file
file1.close()

# Checking if the data is
# written to file or not
file1 = open('myfile.txt', 'r')
print(file1.read())
file1.close()

'''
Output:

Hello
This is Delhi
This is Paris
This is London


With statement
with statement in Python is used in exception handling to make the code cleaner 
and much more readable. It simplifies the management of common resources like file streams. 
Unlike the above implementations, 
there is no need to call file.close() when using with statement. 
The with statement itself ensures proper acquisition and release of resources.

Syntax:

with open filename as file:
'''
# Program to show various ways to
# write data to a file using with statement

L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

# Writing to file
with open("myfile.txt", "w+") as file1:
    # Writing data to a file
    file1.write("Hello \n")
    file1.writelines(L)

