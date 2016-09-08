# -*- coding: utf-8 -*-
print u"Введите первое число"
n1 = int(raw_input("> "))

print u"Введите второе число"
n2 = int(raw_input("> "))

print u"Выберите что искать min - 1  или max - 2?"
mm = raw_input("> ") # vvod min ili max
if mm == "1":
	if n1<n2:
		print u"Минимальное число %d" % n1
	elif n2<n1:
		print u"Минимальное число %d" % n2	
if mm == "2":
	if n1>n2:
		print u"Максимальное число %d" % n1
	elif n2>n1:
		print u"Максимальное число %d" % n2
else:
	print u"Числа равны"