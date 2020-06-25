# fibbonaci sereies using while loop
n = int(input("Enter the value of 'n': "))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series: ", end = " ")
while(count <= n):
  print(sum, end = " ")
  count += 1
  a = b
  b = sum
  sum = a + b

O/p:Enter the value of 'n': 6
Fibonacci Series:  0 1 1 2 3 5

# To display the multiplication table
num = int(input("Display multiplication table of? "))
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)

O/p:Display multiplication table of? 7
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70

# converting from binary to decimal
b_num = list(input("Input a binary number: "))
value = 0

for i in range(len(b_num)):
	digit = b_num.pop()
	if digit == '1':
		value = value + pow(2, i)
print("The decimal value of the number is", value)

O/p:Input a binary number: 1000001
The decimal value of the number is 65

  # def reverse(s): 
    if len(s) == 0: 
        return s 
    else: 
        return reverse(s[1:]) + s[0] 
  
s = "hello"
  
print ("The original string  is : ",end="") 
print (s) 
  
print ("The reversed string(using recursion) is : ",end="") 
print (reverse(s)) 

O/p:The original string  is : hello
The reversed string(using recursion) is : olleh

  # finding gcd of two numbers
def gcd(a,b): 
    if (a == 0): 
        return b 
    if (b == 0): 
        return a 
    if (a == b): 
        return b 
    if (a > b): 
        return gcd(a-b, b) 
    return gcd(a, b-a)
a = 98
b = 56
if(gcd(a, b)): 
    print('GCD of', a, 'and', b, 'is', gcd(a, b)) 
else: 
    print('not found')

o/p:GCD of 98 and 56 is 14 

numbers = (1, 2, 3, 4, 5, 6, 7)
 # Declaring the tuple
count_odd = 0
count_even = 0
for x in numbers:
        if not x % 2:
    	     count_even+=1
        else:
    	     count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)

O/p:Number of even numbers : 3
Number of odd numbers : 4