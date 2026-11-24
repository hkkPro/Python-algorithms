dane = [0, 50, 100, 180, 260, 310, 500]

def harmonogram (czasy_ms):
    prog_czujnik = 0
    prog_ekran = 0
    wyswietlanie = []
    for dana in czasy_ms:
        if dana !=0:
            if dana - prog_czujnik >=100:
                wyswietlanie.append(("czujnik", dana))
                prog_czujnik = dana
            if dana - prog_ekran >=250:
                wyswietlanie.append(("ekran", dana))
                prog_ekran = dana
    return wyswietlanie

wynik = harmonogram(dane)
for elementy in wynik:
    print(elementy)