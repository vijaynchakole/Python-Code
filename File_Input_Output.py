# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 00:14:53 2020

@author: hp


Modes	Description
"r" 	 Open a file for read only
"w" 	 Open a file for writing. If file already exists its data will be cleared before opening. Otherwise new file will be created
"a" 	 Opens a file in append mode i.e to write a data to the end of the file
"wb" 	 Open a file to write in binary mode
"rb" 	 Open a file to read in binary mode


read([number]) 	Return specified number of characters from the file. if omitted it will read the entire contents of the file.
readline() 	Return the next line of the file.
readlines() 	Read all the lines as a list of strings in the file

close()	Close an open file. It has no effect if the file is already closed.
detach()	Separate the underlying binary buffer from the TextIOBase and return it.
fileno()	Return an integer number (file descriptor) of the file.
flush()	Flush the write buffer of the file stream.
isatty()	Return True if the file stream is interactive.
read(n)	Read atmost n characters form the file. Reads till end of file if it is negative or None.
readable()	Returns True if the file stream can be read from.
readline(n=-1)	Read and return one line from the file. Reads in at most n bytes if specified.
readlines(n=-1)	Read and return a list of lines from the file. Reads in at most n bytes/characters if specified.
seek(offset,from=SEEK_SET)	Change the file position to offset bytes, in reference to from (start, current, end).
seekable()	Returns True if the file stream supports random access.
tell()	Returns the current file location.
truncate(size=None)	Resize the file stream to size bytes. If size is not specified, resize to current location.
writable()	Returns True if the file stream can be written to.
write(s)	Write string s to the file and return the number of characters written.
writelines(lines)	Write a list of lines to the file.

'r'	Open a file for reading. (default)
'w'	Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
'x'	Open a file for exclusive creation. If the file already exists, the operation fails.
'a'	Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
't'	Open in text mode. (default)
'b'	Open in binary mode.
'+'	Open a file for updating (reading and writing)


"""
#"C:\Users\hp\PycharmProjects\python important programs\New Text Document.txt"

fd = open("New Text Document.txt", 'r', encoding = 'utf-8')
fd.read(10)


fd.read()

# file descriptor location 
fd.tell()

#change fd location to zeroth index

fd.seek(0)

fd.read()

fd.close()

# writing data into file

fd = open("New Text Document.txt", 'a+', encoding = 'utf-8')
fd
no = fd.write("tuesday is coming\n")
no
fd.close()

new_fd = open("append.txt",'a', encoding = 'utf-8')

new_fd.write("demo file for file handling program")
# it will not reflect written data unless and until we close that file by calling close() 
# after this now it will show written data in file
new_fd.close()
