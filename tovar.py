tovar = raw_input("Vvedite tovar: ")
cena = raw_input("Vvedite cenu: ")
kolvo = raw_input("Vvedite kolichestvo: ")

summ = int(cena) * int(kolvo)

print "-----------------------------------------------"
print "Vi kupili " + tovar + " na summu - " + str(summ) + " som."
print "-----------------------------------------------"

print "Spasibo za pokupku!"