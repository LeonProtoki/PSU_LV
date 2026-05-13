import pandas as pd

df = pd.read_csv("cars_processed.csv")

#broj automobila
print(len(df))

#tipovi pojedinih stupaca
print(df.dtypes)

#najskuplji
print("\nNajskuplji auto:")
print(df.loc[df.selling_price.idxmax()])

#najjeftiniji
print("\nNajjeftiniji auto:")
print(df.loc[df.selling_price.idxmin()])

#2012. god
print("automobili iz 2012.:", len(df[df['year']==2012]))

#najveca km
#idxmax() vraća indeks reda s najvećom vrijednosti,
#idxmin() s najmanjom
# df.loc[indeks] dohvaća taj red
print("automobili s najvecom km:")
print(df.loc[df["km_driven"].idxmax(),["name","km_driven"]])
#najmanja km 
print("automobili s najmanjom km:")
print(df.loc[df["km_driven"].idxmin(), ["name", "km_driven"]])

#najcesca vrijdnost sjedala
#mode() vraća najčešću vrijednost
#[0] uzima prvu (jer ih može biti više, ali ovdje je samo jedna)
print("najcesci broj sjedala:",df['seats'].mode()[0])

#dizel motori prosjecna km
print("disel:",round(df[df["fuel"]=="Diesel"]["km_driven"].mean(),2))
print("benzin:",round(df[df["fuel"]=="Petrol"]["km_driven"].mean(),2))