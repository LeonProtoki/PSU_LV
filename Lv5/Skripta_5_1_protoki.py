'''
Room occupancy classification 

R.Grbic, 2024.

'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, precision_score, recall_score, accuracy_score, classification_report


# ucitaj podatke za ucenje
df = pd.read_csv('occupancy_processed.csv')

feature_names = ['S3_Temp', 'S5_CO2']
target_name = 'Room_Occupancy_Count'
class_names = ['Slobodna', 'Zauzeta']

X = df[feature_names].to_numpy()
y = df[target_name].to_numpy()

# Scatter plot
plt.figure()
for class_value in np.unique(y):
    mask = y == class_value
    plt.scatter(X[mask, 0], X[mask, 1], label=class_names[class_value])

plt.xlabel('S3_Temp')
plt.ylabel('S5_CO2')
plt.title('Zauzetost prostorije')
plt.legend()
plt.show()

#a)
#kada je CO2 veci-prostorija je zauzeta
#kada su CO2 i temperatura nizi-prostorija je prazna
#postoji malo preklapanje-problem je klasifikacija,ali ne savrseno linearna

#b)
print("skup podataka sadrzi podatkovnih primejera:");
print(len(y))  
#y-vektor izlaznih vrijednosti, broj primjera
#x-ulazni podaci

#c)
print("razdioba podatkovnih primjera po klasama je:")
unique,counts =np.unique(y,return_counts=True)
print("klase:",unique)
print("broj:",counts)
