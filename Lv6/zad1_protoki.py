import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from funkcija_6_1 import generate_data

# generiranje 500 podataka (flag mijenja oblik podataka)
X = generate_data(500, 1)

# isprobavanje različitih K
for k in [2, 3, 4, 5]:
    kmeans = KMeans(n_clusters=k, n_init=10)   # model s k klastera
    labels = kmeans.fit_predict(X)             # treniranje + dodjela klastera
    centers = kmeans.cluster_centers_          # koordinate centara


    plt.figure()
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')  # obojeni podaci
    plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, marker='X')  # centri
    plt.title(f"K = {k}")
    plt.show()

#Što primjećujete pri više pokretanja?
#-rezultat se mijenja jer KMeans koristi slučajnu inicijalizaciju centara

#Što ako mijenjate način generiranja podataka (flag)?
#-flag 1–3 --> KMeans radi dobro
#-flag 4–5 --> radi loše jer KMeans pretpostavlja sferične (okrugle) klastere, nepotrebno ih razdvaja na dodatne klastere(grupe)
