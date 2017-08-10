#Task 5
#5.x: Dictionaries

#5.1
dict = {'bob':5, 'alice':4}
print dict

#5.3
scores = {}
while True:
	name = raw_input("Enter student name: ")
	if len(name) == 0:
		break
	score = float(raw_input("Enter student score: "))
	scores[name] = score
print scores
