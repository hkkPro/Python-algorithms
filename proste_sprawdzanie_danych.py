temperatury = [10, 18, 22.5, 26, 30, -5]

def ocen_temperature(temperatury):  
    if temperatury < 18:
        return "ZA ZIMNO"
    elif temperatury >= 18 and temperatury <=26:
        return "OK"
    elif temperatury > 26:
        return "ZA CIEPLO"

for temperatura in temperatury:
    wynik = ocen_temperature(temperatura)
    print(wynik, temperatura)