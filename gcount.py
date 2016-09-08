def gcount(slovo):

	cnt = 0
	glasn = ["a", "e", "i", "o", "u"]

	for l in slovo:
		if l in glasn:
			cnt += 1
	return cnt

s = raw_input("Vvedite slovo >>")
while s != "1":
    print gcount(s)
