import numpy as np
temperatury = [18, 20, 22, 24, 26, 28]

np_temp = np.array(temperatury)

shape = np_temp.shape

typ = np_temp.dtype

maks = np_temp.max()

minimum = np_temp.min()

avg = np_temp.sum()/len(np_temp)

rozmiar = np_temp.size

skorygowane = np_temp-0.5

fahrenheit = (skorygowane*1.8)+32

print(f"Tablica: {np_temp}")
print(f"Ksztalt: {shape}")
print(f"Typ: {typ}")
print(f"Maks: {maks}, Min: {minimum}")
print(f"Srednia: {avg}, Fahrenheit: {fahrenheit}")
print(f"Rozmiar tablicy: {rozmiar}")

#roznica w mnozeniu tablicy w np a bazowej python jest taka
#ze w pythonie mnozenie tablicy wymnaza nie wartosci elementow
#tylko same elementy, a w np mnozenie odbywa sie przez wartosci
#znajdujace sie w tablicy