import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

df=pd.read_csv('occupancy_processed.csv')

feature_names=['S3_Temp','S5_CO2']
target_name='Room_Occupancy_Count'

x = df[feature_names].to_numpy()
y = df[target_name].to_numpy()

#podjela 80-20
x_train,x_test,y_train,y_test=train_test_split(
    x,y,
    test_size=0.2,
    stratify=y,
    random_state=51
)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

model=KNeighborsClassifier(n_neighbors=5)
model.fit(x_train,y_train)

y_pred=model.predict(x_test)

#matrica zabune
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=['Class 0','Class 1']
    )

disp.plot(cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.show()

# Izracunaj preciznost
precision = precision_score(y_test, y_pred)
# Izracunaj odziv
recall = recall_score(y_test, y_pred)
# Izracunaj tocnost
accuracy = accuracy_score(y_test, y_pred)

print("\n")
print("preciznost:",precision)
print("odziv:",recall)
print("tocnost:",accuracy)
#report
print(classification_report(y_test, y_pred))

#e)
#veci broj susjeda-glada granica odlucivanje i moze uzrokovati underfitting
#manji broj susjeda cini model osjetljivijim na sum i moze dovest do overfittinga

#f)
#bez skaliranja rezultati su losiji jer knn koristi udaljenost izemdu podataka a varijable imaju razlicite skale