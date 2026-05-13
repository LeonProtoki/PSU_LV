import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.cluster import KMeans

img = mpimg.imread('example.png')

X = img.reshape(-1, 3)

kmeans = KMeans(n_clusters=10, n_init=10)
kmeans.fit(X)

values = kmeans.cluster_centers_
labels = kmeans.labels_

img_compressed = values[labels]
img_compressed = img_compressed.reshape(img.shape)

# konverzija ako treba
if img_compressed.max() <= 1:
    img_compressed = (img_compressed * 255).astype(np.uint8)
else:
    img_compressed = img_compressed.astype(np.uint8)

plt.figure()
plt.imshow(img)
plt.title("Original")

plt.figure()
plt.imshow(img_compressed)
plt.title("Kvantizirana")
plt.show()