from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from funkcija_6_1 import generate_data

X = generate_data(500, 1) #generiranje podataka

inertia = [] #suma kvadriranih udaljenosti svih točaka do najbližeg centra klastera
K_range = range(1, 21)  #skup svih vrijednosti broja klastera

for k in K_range:
    k_means = KMeans(n_clusters=k, n_init=10)
    k_means.fit(X)
    inertia.append(k_means.inertia_)  # kriterijska funkcija

plt.plot(K_range, inertia, marker='o')
plt.xlabel("Broj klastera (K)")
plt.ylabel("Vrijednost kriterijske funkcije")
plt.title("Elbow-lakat metoda")
plt.show()

#Kako komentirati graf?
#-vrijednost stalno pada kad povećavamo K

#Kako odabrati optimalni K?
#-traži se lakat metoda(elbow)-(točka gdje se pad naglo usporava)