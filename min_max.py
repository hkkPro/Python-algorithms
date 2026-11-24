dane = [30,10,20,80,50]
maksimum = dane[0]
minimum = dane[0]

for dana in dane:
    if dana>=maksimum:
        maksimum = dana

for dana2 in dane:
    if dana2<= minimum:
        minimum = dana2      
print(f"Maksimum: {maksimum}, Minimum: {minimum}")
    
        

        