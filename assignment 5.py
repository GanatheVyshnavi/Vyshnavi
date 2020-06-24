#import math
r = float(input('Enter the radius of the circle :'))
area = math.pi * r * r
print("Area of the circle is : %.2f" %area)

O/p:Enter the radius of the circle :3.5
Area of the circle is : 38.48


#from math import tan, pi
n_sides = int(input("Input number of sides: "))
s_length = float(input("Input the length of a side: "))
p_area = n_sides * (s_length ** 2) / (4 * tan(pi / n_sides))
print("The area of the polygon is: ",p_area)


O/p:Input number of sides: 4
        Input the length of a side: 20
        The area of the polygon is:  400.00000000000006



#import math
pi=3.142
def segmentarea(r,angle):
    areaofsector = pi * (r * r) * (angle / 360) 
    areaoftriangle = 1 / 2 *(r * r) *math.sin((angle * pi) / 180) 
  
    return areaofsector - areaoftriangle; 
r=int(input("enter the radius"))
angle=int(input("enter the angle"))
print("area of minor segment=",segmentarea(r,angle))
print("area of major segment=",segmentarea(r,(360-angle)))


O/p:enter the radius10
enter the angle90
area of minor segment= 28.550001037069357
area of major segment= 285.649990666376


#from random import shuffle
l1 = [100,1,2,3,30,40,"hai","hello"]
shuffle(l1)
print(l1)


O/p:[3, 2, 30, 'hello', 40, 'hai', 100, 1]


#import random 
def Rand(start, end, num): 
    res = [] 
    for j in range(num): 
        res.append(random.randint(start, end)) 
    return res
num = 50
start = 1
end = 10000
print(Rand(start, end, num)) 

O/p:[2465, 9330, 8440, 7688, 7543, 3492, 522, 3776, 9456, 9772, 5428, 5229, 1607, 3019, 8719, 9472, 5415, 4251, 7276, 1459, 8284, 6079, 7314, 4544, 2183, 4674, 2784, 2178, 9708, 8000, 9250, 274, 2405, 8590, 6707, 8586, 3188, 1954, 5118, 6397, 8856, 7331, 6147, 4582, 5119, 883, 5997, 4062, 2290, 1570]


#import math
sine=math.sin(60)
print(sine)
o/p:  -0.3048106211022167

import math
co=math.cos(pi)
print(co)
o/p:  -0.9999999170344522

import math
ta=math.tan(90)
print(ta)
o/p: -1.995200412208242

import math

print(math.sin((0.86602540378443860009)))
O/p:0.7617599814162892

print(5**8)
o/p:390625


print(400**0.5)
o/p:20.0

import math
print(5*(math.e))
o/p:13.591409142295225

import math
print(math.log2(1024))
o/p:10.0

import math
print(math.log10(1024))
o/p:3.010299956639812


import math
print(math.floor(23.56))
print(math.ceil(23.56))
o/p:23
24