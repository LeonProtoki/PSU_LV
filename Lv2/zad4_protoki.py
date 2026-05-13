import numpy as np
import matplotlib.pyplot as plt 

def sahovnica(vel_kvadrata,br_visina,br_sirina):
    bijeli=np.ones((vel_kvadrata,vel_kvadrata))*255 #bijeli kvadrat
    crni =np.zeros((vel_kvadrata,vel_kvadrata))     #crni kvadrat

    redovi=[]
    for i in range(br_visina):  #petlja ide do br_visine
        red=[]
        for j in range(br_sirina):
            if(i+j)%2==0:
                red.append(bijeli)  #parno-bijeli
            else:
                red.append(crni)    #parno-crno
        redovi.append(np.hstack(red)) #spajanje kvadrata u red horizontalno
        
    slika=np.vstack(redovi)           #spajanje redove u sliku okomito
    return slika

img=sahovnica(50,4,5)
plt.imshow(img,cmap='gray',vmin=0,vmax=255)
plt.show()
