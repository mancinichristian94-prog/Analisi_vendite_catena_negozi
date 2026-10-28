import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import random
from datetime import date, timedelta

### PARTE 1 ### CREAZIONE FILE CSV VENDITE DELLA CATENA DI NEGOZI

prezzi = {
    "Smartphone": (400, 700),
    "Laptop": (700, 1500),
    "TV": (300, 1000),
    "Smartwatch": (120, 300),
    "Cuffie": (120, 300),
    "PC": (1200, 3000),
}

negozi = ["Milano", "Roma", "Napoli", "Firenze", "Bari", "Taranto", "Trento"]
prodotti = list(prezzi)
data_inizio = date(2026, 1, 1)

with open("vendite.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Data", "Negozio", "Prodotto", "Quantità", "Prezzo_unitario"])

    for i in range(30):
        data = data_inizio + timedelta(days=i)
        negozio = random.choice(negozi)
        prodotto = random.choice(prodotti)
        quantita = random.randint(1, 10)
        prezzo = round(random.uniform(*prezzi[prodotto]), 2)
        writer.writerow([data, negozio, prodotto, quantita, prezzo])

### PARTE 2 ### IMPORTAZIONE IN PANDAS

df = pd.read_csv("vendite.csv", parse_dates= ["Data"])

print("Le prime 5 righe del dataframe: \n", df.head())
print("\nStruttura del dataframe: \n", df.shape)
df.info

### PARTE 3 ###

df["Incasso"] = df["Quantità"] * df["Prezzo_unitario"]

print("Incasso totale: ", df["Incasso"].sum())

print("\nIncasso medio per negozio: \n")
print(df.groupby("Negozio")["Incasso"].mean())

print("\nTop 3 prodotti per quantità: ")
print(df.groupby("Prodotto")["Quantità"].sum().nlargest(3))

print("\nIncasso medio per Negozio e Prodotto: \n")
print(df.groupby(["Negozio", "Prodotto"])["Incasso"].mean())

### PARTE 4 ###

q = df["Quantità"].to_numpy()

media = np.mean(q)
minimo = np.min(q)
massimo = np.max(q)
dev_std = np.std(q)

print("Media:", media)
print("Minimo:", minimo)
print("Massimo:", massimo)
print("Deviazione standard:", dev_std)

# 2. Percentuale di vendite sopra la media
perc_sopra_media = np.sum(q > media) / len(q) * 100
print("Vendite sopra la media:", round(perc_sopra_media, 2), "%")

# 3. Array 2D con Quantità e Prezzo_unitario
arr = df[["Quantità", "Prezzo_unitario"]].to_numpy()
incasso_np = arr[:, 0] * arr[:, 1]

# 4. Confronto con la colonna Incasso del DataFrame
print("Risultati uguali:", np.allclose(incasso_np, df["Incasso"].to_numpy()))

### PARTE 5 ###

# 1. Grafico a barre: incasso totale per negozio
df.groupby("Negozio")["Incasso"].sum().plot(kind="bar")
plt.title("Incasso totale per negozio")
plt.xlabel("Negozio")
plt.ylabel("Incasso (€)")
plt.tight_layout()
plt.show()

# 2. Grafico a torta: percentuale di incassi per prodotto
df.groupby("Prodotto")["Incasso"].sum().plot(kind="pie", autopct="%1.1f%%")
plt.title("Incassi per prodotto")
plt.ylabel("")
plt.show()

# 3. Grafico a linee: andamento giornaliero degli incassi
df.groupby("Data")["Incasso"].sum().plot(kind="line", marker="o")
plt.title("Andamento giornaliero degli incassi")
plt.xlabel("Data")
plt.ylabel("Incasso (€)")
plt.tight_layout()
plt.show()

### PARTE 6 ###

categorie = {
    "Smartphone": "Informatica",
    "Laptop": "Informatica",
    "PC": "Informatica",
    "Smartwatch": "Informatica",
    "TV": "Elettrodomestici",
    "Cuffie": "Accessori",
}
df["Categoria"] = df["Prodotto"].map(categorie)

# 2. Incasso totale e quantità media per categoria
print("Incasso totale per categoria:")
print(df.groupby("Categoria")["Incasso"].sum())

print("\nQuantità media per categoria:")
print(df.groupby("Categoria")["Quantità"].mean())

# 3. Salvataggio
df.to_csv("vendite_analizzate.csv", index=False)
