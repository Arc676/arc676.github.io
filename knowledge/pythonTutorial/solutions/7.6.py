#Task 7.6
#7.6: Error handling

import math

try:
	num = float(raw_input("Enter a positive number: "))
	print math.sqrt(num)
except ValueError:
	print "Not a positive number"

try:
	s = raw_input("Enter a string: ")
	i1 = int(raw_input("Enter an index: "))
	i2 = int(raw_input("Enter an index: "))
	print s[i1:i2]
except ValueError:
	print "Not a number"
except IndexError:
	print "Index out of bounds"

try:
	arr = []
	while True:
		n = raw_input("Enter a number: ")
		if len(n) == 0:
			break
		arr.append(int(n))
	index = int(raw_input("Enter n: "))
	print "The nth number was", arr[index - 1]
except ValueError:
	print "Not a number"
except IndexError:
	print "Invalid index"
