x = int(input('Geschätzte Ankunft in Stunden: '))
y = int(input('Geschätzte Ankunft Minuten: '))

diff = 7 * 60
sim = x * 60					#sim= stunden in minuten
minuten = sim - diff

if minuten < 0:
	s = minuten // 60
	stunden = 24 + s
	stunden=str(stunden)
	y=str(y)
	if len(stunden)<2:
		stunden='0'+stunden
	if len(y)<2:
		y='0'+y
	print('Voraussätzliche Ankunft',stunden,':',y)
else:
	S = minuten // 60
	S=str(S)
	y=str(y)
	if len(S)<2:
		S='0'+S
	if len(y)<2:
		y='0'+y
	print('Voraussätzliche Ankunft',S,':',y)