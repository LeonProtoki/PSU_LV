

import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("tiger.png")
img = img[:,:,0].copy()
img_a=img + 0.5
img_a=np.clip(img_a, 0, 1)  # drži između 0 i 1
plt.figure()
plt.imshow(img_a, cmap="gray")
plt.show()

img_b=np.rot90(img,k=-1) #k-1 u smjeru kazaljke na satu
plt.figure()
plt.imshow(img_b, cmap="gray")
plt.title("b) Rotirana")
plt.show()


img_c=np.fliplr(img)
plt.figure()
plt.imshow(img_c, cmap="gray")
plt.title("c) Zrcaljena")
plt.show()

img_d=img[::10,::10] #svaki 10. redak i svaki 10. stupac
plt.figure()
plt.imshow(img_d, cmap="gray")
plt.title("d) Smanjena rezolucija")
plt.show()

img_e=np.zeros_like(img)
sirina=img.shape[1]    # ukupna širina slike
cetvrtina=sirina //4  # veličina jedne četvrtine
# kopiraj samo drugu četvrtinu
img_e[:, cetvrtina:cetvrtina*2] = img[:, cetvrtina:cetvrtina*2]
plt.figure()
plt.imshow(img_e, cmap="gray")
plt.title("e) Druga cetvrtina")
plt.show()
