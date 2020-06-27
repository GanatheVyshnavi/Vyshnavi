#1  program to remove a new line

string="Python Exercises\n module 3\n assignment 3"
print("After removing new lines\n")
print(string.rstrip())

#2. count occurrences of a substring in a string

string = "Python is awesome, isn't it?"
substring = "is"
count = string.count(substring)
print("The count is:", count)


#3. convert a string in a list

def Convert(string): 
   a= list(string.split(" ")) 
   return a
str1 = "my name is xxxx" 
print(Convert(str1)) 

#4. program to perform Deletion of a character
def rem(string,i):
    a=string[ : i]
    b=string[i+1: ]
    return a+b
if __name__ == '__main__':
    string=str(input("Enter a string: "))
    i=int(input('Enter the index of which element to delete:'))
    print(rem(string, i))


#5. program to every character of a string in new line
string=str(input("Enter a string: "))
for index,letter in enumerate(string,1):
    print(letter)

#6. program to find length of the string without using len function

string="refrigerator"
count=0
for i in string:
    count+=1
print("The length of string is",count)
