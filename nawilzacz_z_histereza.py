wilg = [38, None, 45, 48, 49,32, 50, 51, None, 55, 56, 30, 28 ,27, 102, 102, 102, 102]

def steruj_nawilzaczem(wilgotnosc):
    stany = []
    start = False
    for wilgotnosci in wilgotnosc:
        try:
            if (0<=wilgotnosci<40):
                start = True
                stany.append(start)
            elif (100>=wilgotnosci > 50):
                start = False
                stany.append(start)
            elif (40<=wilgotnosci<=50):
                stany.append(start)
            else:
                start = False
                stany.append(start)
        except TypeError:
            start = False
            stany.append(start)
    return stany

print(steruj_nawilzaczem(wilg))