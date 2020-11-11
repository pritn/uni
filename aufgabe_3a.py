x = int(input('Momentane Uhrzeit, Stunden: '))
y = int(input('Momentane Uhrzeit, minuten: '))
z = int(input('Minuten im Flugzeug: '))

NZ = (x*60)+y		# Momentane Uhrzeit in Minuten /NZ= Neuezeit
AF = NZ - z			#Uhrzeit minus Flugzeit/ Af= Abflug

if x==00:
	x=24
	NZ=(x*60)+y
	AF= NZ - z
				
if AF < 0:
	af = (24*60)+AF
	s = af //60				#stunden Abflug
	m = af%60				#minuten Abflug
	s=str(s)
	m=str(m)
	if len(s)<2:
		s='0'+s
	if len(m)<2:
		m='0'+m
	print('i)',s,':',m)
else:
	S= AF//60
	M= AF%60
	S=str(S)
	M=str(M)
	if len(S)<2:
		S='0'+S
	if len(M)<2:
		M='0'+M
	print('i)',S,':',M)

Zeit= z+30
boarding= NZ-Zeit
if boarding < 0:
	bf = (24*60)+boarding
	stunden = bf //60
	minuten = bf%60
	stunden=str(stunden)
	minuten=str(minuten)
	if len(stunden)<2:
		stunden='0'+stunden
	if len(minuten)<2:
		minuten='0'+minuten
	print('ii)',stunden,':',minuten)
else:
	Stunden= boarding//60
	Minuten= boarding%60
	Stunden=str(Stunden)
	Minuten=str(Minuten)
	if len(Stunden)<2:
		Stunden='0'+Stunden
	if len(Minuten)<2:
		Minuten='0'+Minuten
	print('ii)',Stunden,':',Minuten)


''' Alte Idee
Stunden= z//60
minuten= z%60

AS = x - Stunden
AM = y - minuten
if AS < 0:
	NS= 23+AS	
	if AM<0:
		NM=60+AM
		print(NS,':',NM)
	else:
		print(NS,':',AM)
else:
	print(AS,':',AM)
'''