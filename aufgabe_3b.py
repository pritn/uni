x = int(input('Geschätzte Ankunft in Stunden(berreich von 1-24): '))
y = int(input('Geschätzte Ankunft Minuten: '))

z = 7 * 60
s = x * 60
m = s - z

if m < 0:
	b = m // 60
	a = 24 + b
	print('Voraussätzliche Ankunft',a,':',y)
else:
	b = m // 60
	print('Voraussätzliche Ankunft',b,':',y)