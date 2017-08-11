#Task 2.5
#2.5: Iteration

#2.5.1
for i in range(int(raw_input("How many stars? "))):
	print "*",
print

#Extension
rows = int(raw_input("How many rows? "))
for r in range(rows):
	for i in range(r + 1):
		print "*",
	print
print

#Alternative solution
for r in range(rows):
	print "*" * (r + 1)

#2.5.2
print "lel"
while raw_input() != "stop":
	print "lel"

#2.5.3, Task 1
for i in range(1, 101):
	if i % 3 == 0 or i % 4 == 0:
		continue
	print i

#2.5.3, Task 2
while True:
	print "lel"
	if raw_input() == "stop":
		break
