# Das alter des Lehrer herausfinden und zwar soll das Alter kleiner als 45 sein
# Die Zehnerstelle und die Einerstelle zusammen  ergeben  eine zwei stelle Zahl (also 10 oder mehr)
# Die Einerstelle ist eine ungerade Zahl
# Die Zehnerstelle ist eine gerade Zahl

age = 1

while age < 45:
    if ((age % 10) % 2 == 1):   # Einerstelle herausnehmen
        if ((age // 10) % 2 == 0):  # Zehnerstelle herausnehmen
            if ((age % 10 + age // 10 ) >= 10):
                print(f"Das Alter ist: {age}")
    age +=1