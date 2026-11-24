dane = "TEMP=23.5;HUM=99;STATE=ON"
            
def parsuj_wiadomosc(tekst):
    try:
        value = dict()
        litery = tekst.split(";")
        for litera in litery:
            wartosci = litera.split("=")
            if len(wartosci)!=2:
                return None
            nazwa = wartosci[0].strip()
            liczba = wartosci[1].strip()
            if nazwa not in ("TEMP", "HUM", "STATE"):    
                return None
            if nazwa == "TEMP":
                if "temperatura" in value:
                    return None
                value["temperatura"] = float(liczba)
            elif nazwa == "HUM":
                if "wilgotnosc" in value:
                    return None
                value["wilgotnosc"] = float(liczba)
            elif nazwa == "STATE":
                if "stan" in value:
                    return None
                if liczba == "OFF":        
                    value["stan"] = False

                elif liczba == "ON":
                    value["stan"] = True
                else:
                    return None

        if len(value)!=3:
            return None
        if not (0<= value["wilgotnosc"]<=100):
            return None
        return value
    except ValueError:
        return None

        


print(parsuj_wiadomosc(dane))