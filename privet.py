print "Hello, World!"
name = raw_input("Vvedite imya > ")
print "Hello, " + name
print "Hello, %s" % name

if name == "Max":
	print "privet drug"
elif name == "Vasya":
	print "Salut"
else:
	print "privet neznakomec"