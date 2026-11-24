pomiary = [10,20,30]
okno = 2

def srednia_kroczaca(pomiary, okno):
    suma = 0
    wartosci =[]
    j = 0
    if okno <= 0:
        raise ValueError
    for j in range(len(pomiary)-(okno-1)):
        suma = 0
        for i in range(j,j+okno):
            if i >= len(pomiary):
                return None
            suma=suma+pomiary[i]
        avg = suma/okno
        wartosci.append(avg)
    return wartosci
    
    
print(srednia_kroczaca(pomiary,okno))