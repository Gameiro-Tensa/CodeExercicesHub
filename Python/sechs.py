# Ecrire un Programme qui permet d'afficher le plus grand de trois entiers saisis au clavier

zahl1 = int(input("Bitte eine Zahl eingeben: "))
zahl2 = int(input("Bitte eine Zahl eingeben: "))
zahl3 = int(input("Bitte eine Zahl eingeben: "))

if (zahl1 > zahl2 and zahl1 > zahl3) :
    print(f"Der großte Zahl ist zahl1 {zahl1}")
elif( zahl2 > zahl1 and zahl2 > zahl3):
    print(f"Der großte Zahl ist zahl2 {zahl2}")
elif(zahl3 > zahl1 and zahl3 > zahl2):
    print(f"Der großte Zahl ist Zahl3 {zahl3}")
else:
    print("Mindestens zwei Zahlen sind gleich groß")