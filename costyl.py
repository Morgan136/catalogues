from pathlib import Path

q = ""
with open("output.txt", "r") as r:
	q += r.readline()
	print("\nroot file: " + q)
words = [w for w in Path("output.txt").read_text().replace("\n", " ").split("C:\\")]

f = open("output.txt")	
w = words [1]
print("str for deleting: " + w)

for i in words:

	i.replace(w, "", 1)

for i in words:
	print (i)
#for z in words:
#	print(z)
