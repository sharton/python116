print "Vvedite vash vozrast"
age = int(raw_input("> "))
if age > 0 and age <= 6:
	print "Detsad"
elif age >= 7 and age <= 17:
	print "Shkola"
elif age >= 18 and age <= 65:
	print "Rabota"
elif age >= 66 and age <= 120:
	print "Pensiya"
else:
	print "lyudi stolko ne jivut"