def read_line(satz):
	count=0
	while True:
		for komma in satz:
			if komma == ',':
				count += 1
		if count == 2:
			format= satz.split(',')
			tup = tuple(format)
			return tup
		else:	
			break

satz=input('Zeichenkette eingebe: ')
print(read_line(satz))

def read_file(datei):
	data= open(datei,'r')
	zeile = data.read()
	wort = zeile.split('\n')
	liste = []
	for i in range(len(wort)):
		spalten = tuple(wort[i].split(','))
		liste.append(spalten)
	liste.pop()
	data.close()
	return liste
	
datei = input('Bitte Dateiname eingeben: ')
print(read_file(datei))

def has_actor(movie,name):
	v=[]
	has= False
	for i in movie:
		for x in i:
			v.append(x)
			r=v[1:len(v):3]
			if name in r:
				has = True
			else:
				has = False
	return has
				
movie= read_file(datei)
name= input('Zeichenkette eingeben: ')
print(has_actor(movie,name))

def actor_collaboration(titel,actor):
	l=[]
	for item in titel:
		if actor in item:
			film=item[0]
			for char in titel:
				if film in char:
					schauspieler=char[1]
					if schauspieler != actor:
						l.append(schauspieler)
	return l
titel=read_file(datei)
actor=input('Schauspieler eingeben: ')
print(actor_collaboration(titel,actor))

def insert():
