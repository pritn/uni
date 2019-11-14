def kubikwurzel(w,e):
	try:float(w) and float(e)
	except ValueError:
		if type(w) != float or type(e)!= float:
			print('Wert muss ein Float sein!')
	
	for i in range(1,6):
		wert = ((3-1)*wert+w/(wert**(3-1)))/3
		while abs(wert**3-w)>=epsilon:
			if wert**3<w:
				links=wert
			else:
				rechts=wert
			wert=(links+rechts)/2.0
			rate_anzahl+=1
	return wert
		
w = input('Bitte Float-Zahl eingeben:')
e = input('Bitte Fehlertoleranz eingeben:')

epsilon=0.01
links=0
rechts =float(w)
rate_anzahl=0
wert=links+rechts/2

print("Wir haben ",rate_anzahl ," mal geraten")
print(wert, " ist nah an der Kubikwurzel von" , w) 


