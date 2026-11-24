pomiary = [20,22,19,23,21]

def statystyki(pomiary):
    suma = 0
    values = dict()
    if not pomiary:
        return "None"
    elif pomiary:
        minimum = pomiary[0]
        for pomiar in pomiary:
            if pomiar < minimum:
                minimum = pomiar   
        maksimum = pomiary[0]
        for pomiar in pomiary:
            if pomiar > maksimum:
                maksimum = pomiar
        number = len(pomiary)
        for pomiar in pomiary:
            suma = pomiar+suma
        avg = suma/number 
        values["liczba"] = number
        values["minimum"] = minimum
        values ["maksimum"] = maksimum
        values ["srednia"] = avg
        return values

obliczenia = statystyki(pomiary)
print(obliczenia)