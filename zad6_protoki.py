

fname = input("Ime datoteke: ")

try:
    f = open(fname,encoding='latin1')
except:
    print("Datoteka se ne moze otvoriti:", fname)
    quit()

ham_rijeci = []
spam_rijeci = []
spam_uzvik = 0

for line in f:
    line = line.rstrip()
    
    if "\t" in line:
        dijelovi = line.split("\t")
        tip = dijelovi[0]
        poruka = dijelovi[1]
        
        broj_rijeci = len(poruka.split())
        
        if tip == "ham":
            ham_rijeci.append(broj_rijeci)
        elif tip == "spam":
            spam_rijeci.append(broj_rijeci)
 
            if poruka.endswith("!"):
                spam_uzvik += 1

f.close()

if len(ham_rijeci) > 0:
    prosjek_ham = sum(ham_rijeci) / len(ham_rijeci)
    print("Prosjecan broj rijeci u ham porukama:", round(prosjek_ham, 2))

if len(spam_rijeci) > 0:
    prosjek_spam = sum(spam_rijeci) / len(spam_rijeci)
    print("Prosjecan broj rijeci u spam porukama:", round(prosjek_spam, 2))

print("Broj spam poruka koje zavrse sa '!' :", spam_uzvik)
print("Ukupno spam poruka:", len(spam_rijeci))
