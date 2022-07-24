from pathlib import Path

words = [w for w in Path("output.txt").read_text().replace("\n", " ").split("C:\\")]

for i in words:
	print(i)