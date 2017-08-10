#2.3: Math

#2.3.1
a = int(raw_input("Enter a number: "))
b = int(raw_input("Enter another number: "))
print "The sum is", (a+b)
print "The difference is", (a-b)
print "The product is", (a*b)
print "The quotient is", (a/b)


#2.3.2
a = int(raw_input("Enter a number: "))
b = int(raw_input("Enter a number: "))
print "The remainder is", (a % b)

#2.3.3
a = int(raw_input("Enter a number: "))
b = int(raw_input("Enter a number: "))
print "The power is", (a ** b)

#2.3.4
import math
angle = float(raw_input("Enter an angle: "))
angle = math.radians(angle)
print "The sine is", math.sin(angle)
print "The cosine is", math.cos(angle)
print "The tangent is", math.tan(angle)
