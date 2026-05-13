
ime_datoteke = input("ime datoteke: ")

try:
    fhand = open(ime_datoteke)
    vrijednosti = []
    
    for line in fhand:
        line = line.rstrip() 
        
        if line.startswith("X-DSPAM-Confidence:"):
            parts = line.split(":")
            broj = float(parts[1].strip())
            vrijednosti.append(broj)
    
    fhand.close()
    
    if len(vrijednosti) > 0:
        prosjek = sum(vrijednosti) / len(vrijednosti)
        print(f"Average X-DSPAM-Confidence: {prosjek}")
    else:
        print("Nije pronadena niti jedna X-DSPAM-Confidence linija")
        
except FileNotFoundError:
    print(f"greska: Datoteka '{ime_datoteke}' nije pronadena")
except ValueError:
    print("greska: Problem pri pretvaranju broja")
