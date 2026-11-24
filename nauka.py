
import csv
with open("nauka2.csv", encoding='utf-8') as file:
    liczby =[]
    dane =[]
    bledy =[]
    naglowek = file.readline()
    odczytanie = csv.reader(file,delimiter=",")
    for  wiersz in odczytanie:
            if len(wiersz) != 2:
                bledy.append(wiersz)
                continue
            czas = wiersz[0]
            wartosc = wiersz[1]    
            dane.append(wartosc)
    for dana in dane:
        try:
            liczba = float(dana)
            liczby.append(liczba)
        except ValueError:
            bledy.append(dana)
    suma_poprawne = len(liczby)
    suma_bledne = len(bledy)
    if liczby:
        srednia = sum(liczby)/suma_poprawne
        maksimum = max(liczby)
        minimum = min(liczby)
    else:
        srednia = maksimum = minimum = "Brak wartosci do wyswietlenia"
        
    
with open("raport.txt","w",encoding="utf-8") as f:
    f.write(f"Poprawne pomiary: {suma_poprawne}\n")
    f.write(f"Bledne wiersze: {suma_bledne}\n")
    f.write(f"Maksimum: {maksimum}\n")
    f.write(f"Minimum: {minimum}\n")
    f.write(f"Srednia: {srednia}\n")
        

    

            
            
            

           
            
    
        
        
