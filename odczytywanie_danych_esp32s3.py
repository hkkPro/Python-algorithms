import serial
import serial.tools.list_ports
import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

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
start = time.perf_counter()
try:
    ser = esp32_connect(urzadzenie)
    while True:
        pomiar = ser.readline().decode('utf-8').strip()
        if not pomiar:
            continue
        else:
            pomiary.append(pomiar)
            end = time.perf_counter()
            time_elapsed = round(end-start,2)
            czas.append(time_elapsed)
            if len(pomiary)>=120:
                print("AutoStop - Made 120 measurements")
                break
            print(f"Collected measurements: {len(pomiary)} of 120")
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

if urzadzenie is not None:
    for wynik in pomiary:
        obrobka.append(wynik.replace(':',','))
    for obrobiona in obrobka:
        nowy_element = obrobiona.split(',')
        if len(nowy_element) == 4:
            wilgotnosc = float(nowy_element[1])
            temperatura = float(nowy_element[3])
            wilg.append(wilgotnosc)
            temp.append(temperatura)
    czas_np=np.array(czas)
    temp_np=np.array(temp)
    wilg_np=np.array(wilg)
    fig, ax = plt.subplots()
    ax.plot(czas_np,wilg_np)
    ax.set_xticks(czas_np[::3])
    ax.tick_params(axis='x', rotation=90)
    plt.tight_layout()
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    plt.show()
        






    

    

                


        


    
           
        
        
