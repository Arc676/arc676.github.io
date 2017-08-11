#6: Functions

#6.1
def greet(name):
	print "Hello,", name

def getName():
	return raw_input("Enter your name: ")

name = getName()
greet(name)
greet(name)

#6.2
def getArea(width, height):
	return width * height

w = float(raw_input("Enter width: "))
h = float(raw_input("Enter height: "))
print "Rectangle area:", getArea(w, h)
