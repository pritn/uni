def find_pos(Text,Buchstabe):
	zahl=0
	for i in Text:
		if i!= Buchstabe:
			zahl+=1
		else:
			return zahl
	return -1	
	
text=input('Zeichenkette eingeben: ')
buchstabe=input('Buchstabe eingeben:')
print(find_pos(text,buchstabe))


wörterbuch = open('de_DE_frami.txt', 'r')		
neueswb = open('dictionary.txt', 'w')
for zeichen in wörterbuch.readline():
	if '#' not in zeichen and '/' not in zeichen:
		neueswb.write(i)
	if '/' in zeichen:
		w = zeichen.split('/')
		neueswb.write(w +'\n')
		
wörterbuch.close()
neueswb.close()