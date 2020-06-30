 # program to clone or copy a list
def clone(l1):
    l_cpy = list(l1)
    return l_cpy
n=int(input('Enter number of items in the list: '))
l1=[]
for i in range(0,n):
    e=float(input('Enter a number: '))
    l1.append(e)
l2=clone(l1)
print("Before cloning:",l1)
print("After cloning:",l2)

O/P:
  Enter number of items in the list: 6
Enter a number: 2
Enter a number: 5.6
Enter a number: 4
Enter a number: 7
Enter a number: 2.7
Enter a number: 9
Before cloning: [2.0, 5.6, 4.0, 7.0, 2.7, 9.0]
After cloning: [2.0, 5.6, 4.0, 7.0, 2.7, 9.0]


  # program to print a list after removing 0th,4th and 5th elements
n=int(input('Enter number of items in the list: '))
l=[]
for i in range(0,n):
    e=float(input('Enter a number: '))
    l.append(e)
l=[x for (i,x) in enumerate (l) if i not in(0,4,5)]
print("After removing 0th,4th and 5th elements:",l)

O/p:
 Enter number of items in the list: 5
Enter a number: 2
Enter a number: 4
Enter a number: 6
Enter a number: 8
Enter a number: 5
After removing 0th,4th and 5th elements: [4.0, 6.0, 8.0]


# program to print the numbers of a list after removing even numbers
n=int(input('Enter number of items in the list: '))
l=[]
for i in range(0,n):
    e=float(input('Enter a number: '))
    l.append(e)
l=[x for x in l if x%2!=0]
print("After removing even numbers:",l)

O/p:
  Enter number of items in the list: 7
Enter a number: 3
Enter a number: 4
Enter a number: 6
Enter a number: 1
Enter a number: 8
Enter a number: 5
Enter a number: 6
After removing even numbers: [3.0, 1.0, 5.0]


# program to find unique elements from the list
def unq(l1):
    unq_l=[]
    for x in l1:
        if x not in unq_l:
            unq_l.append(x)
    for x in unq_l:
        print(x,)
n1=int(input('Enter number of items in the lis1t: '))
l1=[]
for i in range(0,n1):
    e=float(input('Enter a number: '))
    l1.append(e)
n2=int(input('Enter number of items in the list: '))
l2=[]
for i in range(0,n2):
    e=float(input('Enter a number: '))
    l2.append(e)
print("The unique values from list1 is")
unq(l1)
print("The unique values from list2 is")
unq(l2)

O/p:
Enter number of items in the lis1t: 5
Enter a number: 2
Enter a number: 4
Enter a number: 2
Enter a number: 5
Enter a number: 4
Enter number of items in the list: 6
Enter a number: 3
Enter a number: 6
Enter a number: 9
Enter a number: 6
Enter a number: 2
Enter a number: 3
The unique values from list1 is
2.0
4.0
5.0
The unique values from list2 is
3.0
6.0
9.0
2.0


# program to check whether a number is in a given range or not
def ch_range(n):
    if n in range(2,9):
        print(" %s is in the given range!"%str(n))
    else:
        print(" %s is outside the given range!"%str(n))
ch_range(26)

o/p:
 26 is outside the given range!
 
 
# program that calculates no.of upper case and lower case letters
string=str(input("Enter a string: "))
c1=c2=0
for i in string:
    if(i.isupper()):
        c1+=1
    elif(i.islower()):
        c2+=1
print("The no of uppercase letters are:",c1)
print("The no of lowercase letters are:",c2)

o/p:
Enter a string: Python Programs are easier to Understand
The no of uppercase letters are: 3
The no of lowercase letters are: 32