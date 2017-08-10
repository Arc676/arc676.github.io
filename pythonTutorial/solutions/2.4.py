#2.4: Selection

#2.4.1
num = int(raw_input("Enter a number: "))
if num == 5:
	print "num is 5"
if num > 2:
	print "num > 2"
if num <= 20:
	print "num <= 20"
if num != 15:
	print "num is not 15"

#2.4.2
num = int(raw_input("Enter a number: "))
if num >= 0 and num <= 10:
	print "between 0 and 10"
elif num >= 65 and num <= 290:
	if num == 256:
		print "between 65 and 290"
	else:
		print "it's 256"
else:
	print "it's just some number"

#2.4.3
#AND takes precedence over OR

#2.4.4
False or True and (True and (False or True)) or False and True and False
	or True
=> True
