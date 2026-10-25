import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

n_righe = 40
negozi = ["Milano", "Roma", "Napoli", "Torino", "Bologna", "Bari", "Firenze", "Cagliari", "Palermo"]
prodotti = {
    "Smartphone": (200.99,1990.0) ,
    "Laptop": (567.00, 899.99) ,
    "TV": (599.99, 4000.0) , 
    "Tablet": (329.99, 2000.0) , 
    "Cuffie": (20.0, 130.0) ,
    "Computer": (780.0, 4000.0)
    }
date = pd.date_range("2026-01-01", "2026-12-31")

df = pd.DataFrame()
df["Data"] = np.random.choice(date, n_righe)
df["Negozio"] = np.random.choice(negozi, n_righe)
df["Prodotto"] = np.random.choice(list(prodotti), n_righe)
df["Quantità"] = np.random.randint(1, 10, n_righe)
df["Prezzo_unitario"] = df["Prodotto"].apply(lambda p: round(np.random.uniform(prodotti[p][0], prodotti[p][1]), 2))

df = df.sort_values("Data").reset_index(drop=True)
df["Data"] = df["Data"].dt.strftime("%Y-%m-%d")
df.to_csv("vendite.csv", index=False)
print(df)