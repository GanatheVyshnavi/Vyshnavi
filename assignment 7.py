1) #to print the pattern
n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,5):
    for j in range(i):
        print('* ', end="")
    print('')


O/p:
* 
* * 
* * * 
* * * *


2) #to print 0-6 except 3 and 6
for x in range(6):
    if (x == 3 or x==6):
        continue
    print(x,end=' ')
print("\n")


O/p:
0 1 2 4 5


3) #to find the string length
def string_length(str1):
    count = 0
    for char in str1:
        count += 1
    return count
print(string_length('python programming'))


O/p:18


4) # to calculate the character frequency
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('google.com'))


O/p:{'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}


5) #to get a  single string from two given strings
def chars_mix_up(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz'))


O/p:xyc abz

6)#displays in upper and lower casses
user_input = input("What's your favourite language? ")
print("My favourite language is ", user_input.upper())
print("My favourite language is ", user_input.lower())


O/p:What's your favourite language? english
My favourite language is  ENGLISH
My favourite language is  english