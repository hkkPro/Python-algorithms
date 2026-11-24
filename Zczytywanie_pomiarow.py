temperatury = []

while True:
    try:
        temperatura = input("Wprowadz temperature:").strip()
        if temperatura.upper() == "KONIEC":
            print(temperatury)
            liczba_pomiarow = len(temperatury)
            print(f"Liczba poprawnych pomiarow:{liczba_pomiarow}")
            break
        znaki = float(temperatura.replace("," , "."))
        temperatury.append(znaki)
        print(temperatury)
    except ValueError:
        print("Zla wartosc, wprowadz poprawna ponownie")