import serial
import serial.tools.list_ports
import numpy as np

ESP32_VID = {'COM3', 'COM4'}


def search_esp(vid):
    for port in serial.tools.list_ports.comports():
        if port.device in vid:
            return port.device
    return None

def esp32_connect(urzadzenie):
    if urzadzenie is not None:
        ser = serial.Serial(urzadzenie, 115200, timeout=3)
        print(f"Connected: {urzadzenie}")
        return ser
    else:
        print("Couldn't find a device")
        return None

urzadzenie = search_esp(ESP32_VID)
pomiary = []
czas = []
i = 0
try:
    ser = esp32_connect(urzadzenie)
    while True:
        pomiar = ser.readline().decode('utf-8').strip()
        if not pomiar:
            i = i+2
            continue
        else:
            i = i+2
            pomiary.append(pomiar)
            czas.append(i)
            print(pomiar)
except KeyboardInterrupt:
    print("Measurement finished!")
except AttributeError:
    print("Device is not connected!")
except serial.SerialException:
    print("Device disconnected, measurement finished!")
finally:
    if urzadzenie is not None:
        ser.close()
obrobka = []
nowy_element=[]
wilg = []
temp = []
for wynik in pomiary:
    obrobka.append(wynik.replace(':',','))
for obrobiona in obrobka:
    nowy_element = obrobiona.split(',')
    if len(nowy_element) == 4:
        wilgotnosc = float(nowy_element[1])
        temperatura = float(nowy_element[3])
        wilg.append(wilgotnosc)
        temp.append(temperatura)        
        
print(temp)





    

    

                


        


    
           
        
        
