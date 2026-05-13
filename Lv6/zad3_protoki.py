import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from funkcija_6_1 import generate_data

X = generate_data(500, 1)

#računa kako se klasteri spajaju
Z = linkage(X, method='ward') 

plt.figure(figsize=(10, 5))
dendrogram(Z) #grafički prikaz spajanja
plt.title("Dendrogram-ward")
plt.xlabel("Podaci")
plt.ylabel("Udaljenost")
plt.show()

C = linkage(X, method='complete')

plt.figure(figsize=(10, 5))
dendrogram(C) #grafički prikaz spajanja
plt.title("Dendrogram-complete")
plt.xlabel("Podaci")
plt.ylabel("Udaljenost")
plt.show()

S = linkage(X,method='single')

plt.figure(figsize=(10,5))
dendrogram(S)
plt.title("Dendrogram-single")
plt.xlabel("Podaci")
plt.ylabel("Udaljenost")
plt.show()

A=linkage(X,method='average')

plt.figure(figsize=(10,5))
dendrogram(A)
plt.title("Dendrogram-average")
plt.xlabel("Podaci")
plt.ylabel("Udaljenost")
plt.show()

#single-->osjetljiv na šum (“lančani efekt”)
#complete--> kompaktniji klasteri
#ward--> najčešće najbolji (minimizira varijancu)
#average--> slican kao complete ali kompleksniji, prosjecna udaljenost izmedu dva klastera