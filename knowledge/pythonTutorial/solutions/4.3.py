#Task 4.3

print "Enter your name: "
name = raw_input()
file = open("file.txt", "w")
file.write("Hello, " + name)
file.close()

file = open("file.txt", "r")
print file.read()
file.close()

#Extension
print "Enter filename: "
filename = raw_input()
file = open(filename, "w")
line = " "
while len(line) > 0:
	line = raw_input()
	file.write(line + "\n")
file.close()
