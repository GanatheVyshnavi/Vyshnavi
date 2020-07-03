 Dictionary in python:

        A dictionary is an assosiative array. Every key of the dictonary is associated to a value. The values of a dictionary can be of any Python type. So dictionaries are unordered key-value-pairs. Like lists dictionaries can easily be changed, can be shrunk and grown at run time. Theybshrink and grow withoutbthe necessity of making copies.
        Dictionaries can contain lists nd vice versa. The items in dictionaries are accessed via keys not by their position. Dictionaries don't support the sequence operation of the sequence data types like strings, tuples and lists. Dictionaries belongs to the built-in mapping type. So dictionaries are unordered key-value-pairs.

Example:
1. empty dictionary
>>> e = {}
>>> print(e)
{}

2. non-empty dictionary
>>> d = {"ham" : "yes", "ben" : "no", "klen" : "yes"}
>>> print(d)
{"ham" : "yes", "ben" : "no", "klen" : "yes"}


# program to sum all the items in list
n=int(input('Enter number of items in the list: '))
l=[]
for i in range(0,n):
    e=float(input('Enter a number: '))
    l.append(e)
def multi(items):
    t=0
    for x in items:
        t=t+x
    return t
print("The sum of items in list is",multi(l))


Enter number of items in the list: 7
Enter a number: 2
Enter a number: -5
Enter a number: 4
Enter a number: 6
Enter a number: 8
Enter a number: -3
Enter a number: 1
The sum of items in list is 13.0


#program to create a list of empty dictionaries
n=int(input('Enter no of dictionaries to create'))
l=[{} for i in range(n)]
print(l)

Enter no of dictionaries to create6
[{}, {}, {}, {}, {}, {}]


# program to access dictionary keys element by index
d= {'maths': 95,'physics': 75, 'chemistry': 65}
print(list(d)[0])

maths


# program to iterate over dictionaries using for loops
d= {'Green': 1, 'Black': 2, 'Red': 3, 'Blue': 4}
for key,val in d.items():
    print(key, 'is', d[key])
    
Green is 1
Black is 2
Red is 3
Blue is 4


# program to concatenate following dictionaries to create a new one
d1={1:10,2:20}
d2={3:30,4:40}
d3={5:50,6:60}
d4={}
for d in (d1,d2,d3):
    d4.update(d)
print(d4)

{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


# program to create a tuple
t=('hi', 'hello', 'bye')
print(t)

('hi', 'hello', 'bye')


# program to create a tuple with different data types
t=(3, 5.9, "Good Morning")
print(t)

 (3, 5.9, 'Good Morning')
 
 
# program to convert a tuple to a string
def con(t):
    str=''.join(t)
    return str
t=('h', 'e', 'l', 'l', 'o')
str=con(t)
print(str)

hello


# program to slice a tuple
t=(5,2,4,3,1,6,9,8)
slice = t[3:5]
print(slice)

 (3, 1)
 
 
# program to find length of the tuple
t= tuple('Hii Good Morning')
print(t)
print(len(t))

('H', 'i', 'i', ' ', 'G', 'o', 'o', 'd', ' ', 'M', 'o', 'r', 'n', 'i', 'n', 'g')
16