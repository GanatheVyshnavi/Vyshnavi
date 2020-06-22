#1.To check equal or nog from 2 inputs
a=10
b=10
if a==b:
	print("both are equal")
else:
	print("both are not equal") 


# 2 Take 3 inputsfrom user and check equal or not using and or
a=1
b=17
c=7
if a==b and b==c:
    print("all equal")
elif a==b or a==c or b==c:
    print("2 are equal")
else:
    print("not equal")
    
  #3.sum is greater or less or equal to   5
    a=2
b=6
c=a+b
print("sum is",c)
if c>5:
    print("sum is greater than 5")
elif c<5:
    print("sum is less than 5")
else:
    print("sum is equal two 5")

 #4.passing marks of a student
  passing_Marks=35
x=int(input("enter marks obtained"))
if x>passing_Marks:
    print("mrks obtained is greater than passing_Marks")
else:
    print("less than passing_Marks")

 #5.Max of 3 numbers
  x=22
y=11
z=2
if x>y and x>z:
    print("x is greater")
elif y>z:
    print("y is greater")
else:
    print("z is greater")