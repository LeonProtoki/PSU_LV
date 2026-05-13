import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.metrics import ConfusionMatrixDisplay

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
    random_state=42
)

#kreiranje i istrenirnje stabla odlucivanja
dt = DecisionTreeClassifier(max_depth=3)
dt.fit(x_train, y_train)

y_pred = dt.predict(x_test)

# Matrica zabune
cm = confusion_matrix(y_test, y_pred)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=['Class 0','Class 1']
)

disp.plot(cmap=plt.cm.Blues)
plt.title("stablo odlucivanja-matrica zabune")
plt.show()

# Izracunaj tocnost
accuracy = accuracy_score(y_test, y_pred)

#report
print(classification_report(y_test, y_pred))

#stablo odlucivanja
plt.figure(figsize=(12,8))
plot_tree(
    dt,
    filled=True
)
plt.show()

#b) 
#povecanjem parametra max_depth stablo postaje složenije i moze dovesti do overfittinga,vise se granja
#smanjenjem max_depth model postaje jednosatvniji i moze doci do underfittinga,manje se granja manje cvorova ima

#c)bez skaliranja rezultati ostaju isti