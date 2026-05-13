import pandas as pd
import numpy as np


mtcars=pd.read_csv('mtcars.csv')

print(mtcars.describe())
print("\n")
print(mtcars.iloc[0:,:2])
print(mtcars.tail(5))

#1.1
print("1.1 zadatak")
print("5 auta s najvecom potrosnjom:")
print(mtcars.sort_values(by="mpg").head(5))
print("\n")

#1.2
#ascdending=false -najveca do najmanja 
#ascending=true -najmanja do najveca
print("1.2 zadatak")
mpg_cyl8=mtcars[mtcars.cyl==8]
print("3 automobila s 8 cilindara i najmnajom potrosnjom:")
print(mpg_cyl8.sort_values(by="mpg", ascending=False).head(3))
print("\n")

#1.3
print("1.3 zadatak")
mpg_cyl6=mtcars[mtcars.cyl==6]
print("srednja potrosnja automobila sa 6 cilindara:")
print(mpg_cyl6["mpg"].mean())
print("\n")

#1.4
print("1.4 zadatak")
cars4=mtcars[(mtcars.cyl==4) & (mtcars.wt>=2.0) & (mtcars.wt<=2.2)]
print("srednja potrosnja automobila izmedu 2000 i 2200 lbs:")
print(cars4["mpg"].mean())
print("\n")

#1.5
print("1.5 zadatak")
print("manualac:")
cars_manual=mtcars[mtcars.am==1]
print(len(cars_manual))
print("\n")

print("automatic:")
cars_automatic=mtcars[mtcars.am==0]
print(len(cars_automatic))
print("\n")

#1.6
print("1.6 zadatak")
print("automatski mjenjac i konjska snaga veca od 100:")
automatic_hp=mtcars[(mtcars.am==0) & (mtcars.hp>100)]
print(len(automatic_hp))
print("\n")

#1.7
print("1.7 zadatak")
print("masa automobila u kg:")
mtcars["masa_kg"]= mtcars.wt*0.453592*1000
print(mtcars[["car","masa_kg"]])
print("\n")


