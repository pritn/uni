wort = input('Wort eingeben:')
duden = open('dictionary.txt','r')
zeilennummer=1

while True:	
	zeile = duden.readline()
	for i in zeile:
		if i != wort:
			zeilennummer+=1
			print('Wort ist nicht vorhanden')
		elif i == wort:
			print('Wort ist in Zeile', zeilennummer)
			break
			
duden.close()