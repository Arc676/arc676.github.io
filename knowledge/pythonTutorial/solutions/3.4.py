#Task 3.4
#2D arrays

#3.4.2
seats = []
for rowNum in range(5):
	row = []
	for seatNum in range(5):
		row.append("")
	seats.append(row)
while True:
	name = raw_input("Enter your name: ")
	if len(name) == 0:
		break
	code = raw_input("Enter seat code: ")
	if len(code) != 2:
		print "Please enter a letter then a number like 'A5'"
		continue
	try:
		row = ['A','B','C','D','E'].index(code[0])
	except ValueError:
		print "Please enter a letter between A and E then a number"
	try:
		seat = int(code[1]) - 1
		if seat < 0 or seat > 4:
			raise ValueError
	except ValueError:
		print "Please enter a letter then a number between 1 and 5"
		continue
	if len(seats[row][seat]) == 0:
		seats[row][seat] = name
		print "Reserved seat", code, "for", name
	else:
		print "This seat is taken"
print seats
