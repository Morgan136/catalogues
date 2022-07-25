from pathlib import Path

q = ""

with open("output.txt", "r") as r:
	q += r.readline()

words = [w for w in Path(r"output.txt").read_text().replace("\n", " ").split("C:\\")]

z = open("output2.txt", "w")
z.write(q)

for i in words:
	z.write(i.replace(words[1][:-1], "\n"))
	
z.close()