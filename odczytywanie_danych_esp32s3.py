import serial
import serial.tools.list_ports
import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import csv

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
status = 0
urzadzenie = search_esp(ESP32_VID)
pomiary = []
czas = []
start = time.perf_counter()
try:
    ser = esp32_connect(urzadzenie)
    while True:
        pomiar = ser.readline().decode('utf-8', errors='ignore').strip()
        if pomiar == "error":
            status = status+1
            print(f"Error {status} / 15. DHT11 is not responding, retrying....")
            if status == 15:
                print("Sensor error! Check the connection of the DHT module.")
                break
            continue
        else:
            status = 0
            pomiary.append(pomiar)
            end = time.perf_counter()
            time_elapsed = round(end-start,2)
            czas.append(time_elapsed)
            if len(pomiary)>=120:
                print("AutoStop - Made 120 measurements")
                break
            print(f"Collected measurements: {len(pomiary)} of 120")
except KeyboardInterrupt:
    print("Measurement finished by user!")
except AttributeError:
    print("Device is not connected!")
except serial.SerialException:
    print("Device disconnected, measurement finished!")
finally:
    if urzadzenie is not None:
        ser.close()
obrobka = []         
wilg = []
temp = []
czas_pop =[]

if urzadzenie is not None and len(pomiary)>0:
    for wynik in pomiary:
        obrobka.append(wynik.replace(':',','))
    for tim, obrobiona in zip(czas,obrobka):
        nowy_element = obrobiona.split(',')
        if len(nowy_element) == 4:
            wilgotnosc = float(nowy_element[1])
            temperatura = float(nowy_element[3])
            wilg.append(wilgotnosc)
            temp.append(temperatura)
            czas_pop.append(tim)

    czas_np=np.array(czas_pop)
    temp_np=np.array(temp)
    wilg_np=np.array(wilg)

    def format_wykresu(ax):
        ax.set_xticks(czas_np[::3])
        ax.tick_params(axis='x', rotation=90)
        ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
        ax.grid(True)
        
    if len(temp) >0:
        fig, ax1 = plt.subplots()
        fig2, ax2 = plt.subplots()
        
        ax1.plot(czas_np,wilg_np, color ='blue')
        ax1.set_title("Wykres pomiaru wilgotnosci")
        ax1.set_xlabel("Czas [s]")
        ax1.set_ylabel("Wilgotnosc wzgledna [%]")
        format_wykresu(ax1)
        ax2.plot(czas_np, temp_np, color = 'red')
        ax2.set_title("Wykres pomiaru temperatury")
        ax2.set_xlabel("Czas [s]")
        ax2.set_ylabel("Temperatura [°C]")
        format_wykresu(ax2)
        fig.tight_layout()
        fig2.tight_layout()
        
        
        fig.savefig("wykres_wilgotnosc.png")
        fig2.savefig("wykres_temperatury.png")
        
        plt.show()
        
        alltime = czas_np[-1]
        min_temp = np.min(temp_np)
        min_hum = np.min(wilg_np)
        max_temp = np.max(temp_np)
        max_wilg = np.max(wilg_np)
        avg_temp = round(np.mean(temp_np), 2)
        avg_hum = round(np.mean(wilg_np), 2)
        
        with open("dane.csv","w",encoding='utf-8',newline="") as f:
            writer = csv.writer(f, delimiter =";")
            writer.writerow(["Czas [s]","Temperatura [°C]","Wilgotnosc [%]"])
            for c,t,w in zip(czas_pop,temp, wilg):
                writer.writerow([str(c).replace(".",","),str(t).replace(".",","),str(w).replace(".",",")])
            
        with open("raport.txt", "w", encoding="utf-8") as f2:
                f2.write(f"Czas badania: {alltime} sekund\n")
                f2.write(f"Minimalna temperatura: {min_temp}°C, Minimalna wilgotnosc: {min_hum}%\n")
                f2.write(f"Maksymalna temperatura: {max_temp}°C, Maksymalna wilgotnosc: {max_wilg}%\n")
                f2.write(f"Srednia temperatura: {avg_temp}°C\n")
                f2.write(f"Srednia wilgotnosc: {avg_hum}%")
        
        






    

    

                


        


    
           
        
        
