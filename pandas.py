import pandas as pd

df = pd.read_csv('pomiary_pandas.csv')
print(df.head(3))
print(f"nazwy: {df.columns}")
print(f"Rodzaj danych: {df.dtypes}")
srednia_temp=sum(df["temperatura"])/len(df["temperatura"])
srednia_wilg=sum(df["wilgotnosc"])/len(df["wilgotnosc"])

#Metody Pandas:
    
#srednia_temp = df["temperatura"].mean()
#srednia_wilg = df["wilgotnosc"].mean()
#max_wilg = df["wilgotnosc"].max()

max_wilg = max(df["wilgotnosc"])
print(f"Max wilgotnosc: {max_wilg}")
print(f"Srednia temperatura: {srednia_temp}")
print(f"Srednia wilgotnosci: {srednia_wilg}")

over25 = df[df["temperatura"]>25]
print(over25)
df["alarm"] = df["temperatura"]>=28
print(df.head())

df.to_csv("raport.csv",index=False)