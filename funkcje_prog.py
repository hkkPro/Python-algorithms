def spr_alarm(pomiary, prog, wymagane):
        if wymagane<1:
            raise ValueError("Seria musi obejmowac minimum 1 pomiar")
        licznik = 0
        lista =[]
        for indeks, pomiar in enumerate(pomiary):
            if pomiar > prog:
                licznik = licznik+1
            else:
                licznik = 0
            if licznik == wymagane:
                lista.append(indeks)        
        return lista



print(spr_alarm([31, 32, 30, 33], 30, 1))