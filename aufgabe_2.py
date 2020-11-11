w= input('Zeichenkette eingeben:')
l= len(w)
t= type(w)

print(l ,t)

if l>=10:
	if l<100:
		A= l/10
		B= l%10

		BA= B*10+A
		print(int(BA))

		Summe= print('A + B =',int(A+B))
		Subtraktion = print('A - B =',int(A-B))
		Produkt= print('A * B =',int(A * B))
		Division = print('B / A =',B/A)
	else:
		print('Zeichenkette zu lang')
else:
	print('Zeichenkette zu Kurz')

