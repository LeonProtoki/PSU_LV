import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.cluster import KMeans

img = mpimg.imread('example_grayscale.png')

# ako je RGB → pretvori u grayscale
if len(img.shape) == 3:
    img = img.mean(axis=2)

X = img.reshape(-1, 1)

kmeans = KMeans(n_clusters=10, n_init=10)
kmeans.fit(X)

values = kmeans.cluster_centers_.squeeze()
labels = kmeans.labels_

img_compressed = values[labels]
img_compressed = img_compressed.reshape(img.shape)

plt.figure()
plt.imshow(img, cmap='gray')
plt.title("Original")

plt.figure()
plt.imshow(img_compressed, cmap='gray')
plt.title("Kvantizirana")
plt.show()

#manji broj klastera--> lošija kvaliteta
#veći broj--> bolja slika



#IZRAČUNAJTE KOLIKA SE KOMPRESIJA OVE SLIKE MOŽE POSTIĆI AKO SE KORISTE 10 KLASTERA
# broj piksela
num_pixels = img.shape[0] * img.shape[1]

# original: 256 razina sive--> 8 bita po pikselu
original_bits = num_pixels * 8

# kompresija:
# svaki piksel treba log2(K) bita (K = broj klastera)
K = 10
bits_per_pixel = np.ceil(np.log2(K))  # zaokruživanje na cijeli broj bitova

compressed_bits = num_pixels * bits_per_pixel

# dodatno treba spremiti centre klastera 
compressed_bits += K * 8  # svaki centar = 8 bita

# omjer kompresije
compression_ratio = original_bits / compressed_bits

print(f"Original veličina (bitovi): {original_bits}")
print(f"Kompresirana veličina (bitovi): {compressed_bits}")
print(f"Kompresijski omjer: {compression_ratio:.2f}x")