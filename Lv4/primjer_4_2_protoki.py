import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures

def non_func(x):
    y = 1.6345 - 0.6235*np.cos(0.6067*x) - 1.3501*np.sin(0.6067*x) - 1.1622 * np.cos(2*x*0.6067) - 0.9443*np.sin(2*x*0.6067)
    return y

def add_noise(y):
    np.random.seed(14)
    varNoise = np.max(y) - np.min(y)
    y_noisy = y + 0.1*varNoise*np.random.normal(0,1,len(y))
    return y_noisy
 
x = np.linspace(1,10,50)
y_true = non_func(x)
y_measured = add_noise(y_true)

x = x[:, np.newaxis]
y_measured = y_measured[:, np.newaxis]

# make polynomial features
#poly = PolynomialFeatures(degree=15)
#xnew = poly.fit_transform(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y_true, 'k--', label='pozadinska funkcija f', alpha=0.5)

degress =[2,6,15]
for d in degress:
    poly=PolynomialFeatures(degree=d)
    xnew=poly.fit_transform(x)
    
    np.random.seed(12)
    indeksi = np.random.permutation(len(xnew))
    indeksi_train = indeksi[0:int(np.floor(0.7*len(xnew)))]
    indeksi_test = indeksi[int(np.floor(0.7*len(xnew)))+1:len(xnew)]

    xtrain = xnew[indeksi_train,]
    ytrain = y_measured[indeksi_train]

    xtest = xnew[indeksi_test,]
    ytest = y_measured[indeksi_test]

    linearModel = lm.LinearRegression()
    linearModel.fit(xtrain,ytrain)

    ytest_p = linearModel.predict(xtest)
    MSE_test = mean_squared_error(ytest, ytest_p)
    print(" ", MSE_test)

  
    plt.plot(x, linearModel.predict(xnew),label=f"deg={d}")

plt.legend()
plt.show()

#zad1- formula 4-3, 4-7, 4-5, 4-4,4-14
#zad1 koristi jednostavni linearni model ,dok zad2 ima polinomske clanove
#zad1 ima veci mse jer ravna linija ne moze dobro opisati nelinearnu funkciju
#zad2 ima manji mse jer polinomski model prati oblik podataka
#previsoki degree moze dovesti do overfittinga