zahl = input('Bitte zwei Zahlen zwischen 0 und 9 eingeben: ')

if len(zahl)!=2:
	print('Nicht genau zwei Zahlen!')
else:
	zahl = int(zahl)
	x1 = zahl//10
	x2 = zahl%10
	t = x1+x2
	print(str(t)*t)