import numpy as np
import matplotlib.pyplot as plt

#a)
data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)

mpg=data[ : ,0]
hp=data[ : ,3]
wt=data[ : ,5]
cyl=data[ : ,1]

#b) i c)
#s-size da tockice budu vidljivije,c-color da budu u boji(zuta najtezi ljubicasta najlaksi)
plt.scatter(mpg,hp,s=wt*15,c=wt)
plt.xlabel('hp')
plt.ylabel('mpg')
plt.title('ovisnost mpg,hp i wt')
plt.grid(True)
plt.show()


#d)
print('\n\n')
print('mpg vrijednosti')
print('min mpg:') 
print(mpg.min())
print('max mpg:')
print(mpg.max())
print('srednja vrijednost mpg:')
print(mpg.mean())

#e)
print('\n\n')
print('mpg vrijednosti za mpg_cyl6')
mpg_cyl6=mpg[cyl==6]
print('min mpg_cyl6:')
print(mpg_cyl6.min())
print('max mpg_cyl6:')
print(mpg_cyl6.max())
print('srednja vrijednost mpg_cyl6:')
print(mpg_cyl6.mean())
#print(np.mean(mpg_cyl6))

print('\n\n')
