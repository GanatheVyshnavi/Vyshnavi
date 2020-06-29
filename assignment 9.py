# program to get smallest and largest numbers from the list
n=int(input('Enter number of items in the list: '))
l=[]
for i in range(0,n):
    e=float(input('Enter a number: '))
    l.append(e)
print("The smallest number in the list is",min(l))
print("The largest number in the list is",max(l))

  # program to multiply all the items in list
n=int(input('Enter number of items to multiply: '))
l=[]
for i in range(0,n):
    e=float(input('Enter a number: '))
    l.append(e)
def multi(items):
    t=1
    for x in items:
        t=t*x
    return t
print("The product of items in list is",multi(l))

# program to remove duplicates from the list
def rem(d):
    x=[]
    for n in d:
        if n not in x:
            x.append(n)
    return x
n=int(input('Enter number of items in the list: '))
l=[]
for i in range(0,n):
    e=float(input('Enter a number: '))
    l.append(e)
print("After removing duplicates:\n",rem(l))

# program to shuffle and print a specified list
from random import shuffle
n=int(input('Enter number of items in the list: '))
l=[]
for i in range(0,n):
    e=str(input('Enter an element: '))
    l.append(e)
shuffle(l)
print(l)

# program to check a list is empty or not
def check(l):
    if len(l)==0:
        return 0
    else:
        return 1
l=[1,-4,7,3] #l=[] for empty list
if check(l):
    print("The list is not empty!")
else:
    print("The list is empty")

# program to find difference between two lists
# Using set() function
def d(a,b):
    print("Difference of two lists is:")
    return (list(set(A)-set(B)))
A=list()
n1=int(input('Enter no.of elements in list 1: '))
print("Enter elements of 1st list:")
for i in range(n1):
    e=float(input("Enter an element: "))
    A.append(e)
B=list()
n2=int(input('Enter no.of elements in list 2: '))
print("Enter elements of 2nd list:")
for i in range(n2):
    e=float(input("Enter an element: "))
    B.append(e)
print(d(A,B))