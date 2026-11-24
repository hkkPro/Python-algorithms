import numpy as np
wilgotnosc = [-80, -60, -5, 160]
np_wilgotnosc = np.array(wilgotnosc)


mask = (np_wilgotnosc >=0) & (np_wilgotnosc <=100)
poprawne = np_wilgotnosc[mask]

bledne = np_wilgotnosc[mask == False]

suma_poprawnych = poprawne.sum()
if len(poprawne)>0:
    srednia_poprawnych = suma_poprawnych/len(poprawne)
    print(f"Srednia poprawnych: {srednia_poprawnych}")
else:
    print("Srednia: Brak poprawnych pomiarow")

over70 = poprawne>70
pop_over70 = poprawne[over70]

print(f"Poprawne: {poprawne}")
print(f"Bledne: {bledne}")
print(f"Liczba poprawnych: {len(poprawne)}")
print(f"Liczba blednych: {len(bledne)}")
print(f"Powyzej 70: {pop_over70}")





