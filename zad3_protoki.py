brojevi=[]

while True:
    unos=input("unesi broj ili Done:")

    if unos=="Done":
        break
    
    try:
        broj=float(unos)
        brojevi.append(broj)
    except ValueError:
        print("greska")

print("korisnik je unio ",len(brojevi), "brojeva")
print("srednja vrijednost brojeva je:", sum(brojevi)/len(brojevi))
print("minimalna vrijednost brojeva je:",min(brojevi))
print("maksimalna vrijednost brojeva je:",max(brojevi))    

brojevi.sort()
print(brojevi)