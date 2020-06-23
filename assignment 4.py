#1 program to find max of 3 numbers using functions
def max(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=c:
        return b
    else:
        return c
x=float(input('Enter 1st value: '))
y=float(input('Enter 2nd value: '))
z=float(input('Enter 3rd value: '))
print("The max of three numbers is:",max(x,y,z))

# 2 program to reverse a string using functions
def rev(r_str):
    s=""
    for ch in r_str:
        s=ch+s
    return s
a=str(input('Enter a string: '))
print("Reverse of the string is:",rev(a))

#3 program to check a number is even or not
def even(x):
    if x%2==0:
        print(x,"is an even number")
    else:
        print(x,"is not an even number")
a=int(input('Enter a number: '))
even(a)

# 4 program check a string is palindrome or not
def palindrome():
    try:
        num=int(input("enter a number"))
    except  exception as ValueError:
        print("invalid input enter a integer")
    else:
        temp=num
        rev=0
        while(num>0):
            dig=num%10
            rev=rev*10+dig
            num=num//10
        if(temp==rev):
            print("the number is palindrome")
        else:
            print("not a palindrome")
    finally:
        print("program executed")
palindrome()


# program for sum of squares of 1st n natural numbers
def sum_sq(x):
    if x==0:
        return x
    else:
        return((x*x)+sum_sq(x-1))
n=int(input('Enter a number: '))
print("Sum of squares of",n,"natural numbers is:",sum_sq(n))