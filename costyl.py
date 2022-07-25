from pathlib import Path

a = []
q = ""

with open("output.txt", "r") as r:
	q += r.readline()
	print("\nroot file: " + q)
words = [w for w in Path(r"output.txt").read_text().replace("\n", " ").split("C:\\")]

w = words [1]

for i in words:
	z = i.replace(w, "")
	a.append(z)
	print(i.replace(w[:-1], ""))
