hoehe=int(input("Höhe "))
breite=int(input("Breite "))
print(" " + "-"*breite)
for i in range(0, hoehe):
    print("|"+" "*breite + "|")
print(" " + "-"*breite)