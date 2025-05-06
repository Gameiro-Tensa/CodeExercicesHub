# Ecrire un Programme Python, qui permet d'evaluer une note saisi au clavier (si la note est superieur a 10 alors il affiche valider sion non valider)
# NB la note comprise entre 0 et 20

print("Bitte geben Sie Ihre Note ein, um zu prüfen ob es bestanden oder nicht bestanden")

note = int(input("Note hier eingeben (zwischen 0 und 20):  "))

if  0 <= note <= 20:
    if note >= 10:
        print("Bestanden")
    else:
        print("Nicht bestanden")
else:
    print("ungültiger Eingabe. Die Note muss zwischen 0 und 20 liegen ")