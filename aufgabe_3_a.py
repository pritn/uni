x = int(input("Geben Sie die Stunden der Uhrzeit an: "))
y = int(input("Geben Sie die Minuten der Uhrzeit an: "))
z = int(input("Geben Sie die bereits geflogene Zeit an: "))


z = ((z * (z < 1440)) + ((z%1440) * (z > 1440)))
std = z//60
minu = z%60

x = (((x - 1)*(y < minu)) + (x * (y > minu)))
y = (((y - minu) * (y > minu)) + ((60 - (minu - y)) * (y < minu)))
x = (((x - std) * (x > std)) + ((24 - (std - x)) * (x < std)))

print(str(x) + ":" + str(y))



x = (((x - 1)*(y < minu)) + (x * (y > minu)))
y = (((y - 30) * (y > 30)) + ((60 - (30 - y)) * (y < 30)))
x = (x * (x > 0 ) + ((24 + x) * (x < 0)))

print(str(x) + ":" + str(y))
