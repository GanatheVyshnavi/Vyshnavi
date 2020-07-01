 f=open("filename1.txt","w")
f.write("line number is 1\n")
f.write("line number is 2\n")
f.write("line number is 3\n")
f.write("line number is 4\n")
f.write("line number is 5\n")
f.write("line number is 6\n")
f.write("line number is 7\n")
f.close()
a_file=open("filename1.txt")
number_of_lines=3
for i in range(number_of_lines):
    line=a_file.readline()
    print(line)

O/p:line number is 1
line number is 2
line number is 3


#def file_read(fname):
    from itertools import islice
    with open(fname,"w") as myfile:
        myfile.write("python exercises\n")
        myfile.write("java exercises")
    txt=open(fname)
    print(txt.read())
file_read('abc.txt')


O/p:python exercises
java exercises


#L = ["Geeks\n", "for\n", "Geeks\n"] 
file1 = open('myfile.txt', 'w') 
file1.writelines(L) 
file1.close() 
file1 = open('myfile.txt', 'r') 
Lines = file1.readlines() 
count = 0
for line in Lines: 
    print("Line{}: {}".format(count, line.strip()))

O/p:Line0: Geeks
Line0: for
Line0: Geeks


#file=open("gfg.txt","r")
count=0
content=file.read()
colist=content.split("\n")
for i in colist:
        if i:
            counter+=1
print("this is number of lines in the file")
print(count)

#def file_size(fname):
    import os
    startinfo=os.start(fname)
    return startinfo.st_size
print("file size in bytes of a plain file:", file_size("test.txt"))


#with open("hello.txt")as f:
with open("copy.txt","w") as f1:
    for line in f:
        f1.write(line)