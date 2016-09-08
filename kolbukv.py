def kolbukv(s):
	dic = {}
	if s != "":
		for slovo in s.lower().split(" "):
			dic[slovo] = len(slovo)
		return dic
	else:
		return None	
print kolbukv(raw_input("Vvedite text >> "))