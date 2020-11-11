x=float(input('Zahl eingeben: '))
y=float(input('Zahl eingeben: '))
z=float(input('Zahl eingeben: '))

aM=print('Arithmetische Mittel: ', (x+y+z)/3)


länge= abs((x+y)/2)
breite= z**2
Fläche= print('Flaeche: ', breite * länge)

maxi=float((x*(x>y)) + (y*(y>x)))
print('Maximum: ',maxi)