import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ucitavanje ociscenih podataka
df = pd.read_csv('cars_processed.csv')
print(df.info())
print("\n")

#najveca km
#idxmax() vraća indeks reda s najvećom vrijednosti,
#idxmin() s najmanjom
print("automobili s najvecom km:")
print(df.loc[df["km_driven"].idxmax(),["name","km_driven"]])
#najmanja km 
print("automobili s najmanjom km:")
print(df.loc[df["km_driven"].idxmin(), ["name", "km_driven"]])
print("\n")

# razliciti prikazi
sns.pairplot(df, hue='fuel')

sns.relplot(data=df, x='km_driven', y='selling_price', hue='fuel')
df = df.drop(['name','mileage'], axis=1)

obj_cols = df.select_dtypes(object).columns.values.tolist()
num_cols = df.select_dtypes(np.number).columns.values.tolist()

fig = plt.figure(figsize=[15,8])
for col in range(len(obj_cols)):
    plt.subplot(2,2,col+1)
    sns.countplot(x=obj_cols[col], data=df)

df.boxplot(by ='fuel', column =['selling_price'], grid = False)

df.hist(['selling_price'], grid = False)

tabcorr = df.corr(numeric_only=True)
sns.heatmap(tabcorr, annot=True, linewidths=2, cmap='coolwarm')

print("\n")
#broj automobila
print(len(df))
print("\n")


#tipovi pojedinih stupaca
print(df.dtypes)
print("\n")

#najskuplji
print("Najskuplji auto:")
print(df.loc[df.selling_price.idxmax()])
print("\n")


#najjeftiniji
print("Najjeftiniji auto:")
print(df.loc[df.selling_price.idxmin()])
print("\n")

#2012. god
print("broj automobila proizvedeno u 2012.:", len(df[df['year']==2012]))
print("\n")


#najcesci broj sjedala
#mode() vraća najčešću vrijednost
#[0] uzima prvu (jer ih može biti više, ali ovdje je samo jedna)
print("najcesci broj sjedala:",df['seats'].mode()[0])
print("\n")

#dizel motori prosjecna km
print("disel motori:",round(df[df["fuel"]=="Diesel"]["km_driven"].mean(),2))
print("\n")
#benzin motori prosjecna km
print("benzin motori:",round(df[df["fuel"]=="Petrol"]["km_driven"].mean(),2))
print("\n")

plt.show()
