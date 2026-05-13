try:
    fhand = open("song.txt")
    rijeci_dict = {}
    
    for line in fhand:
        line = line.rstrip()
        rijeci = line.split()  
        
        for rijec in rijeci:
            rijec = rijec.lower()
            
            if rijec in rijeci_dict:
                rijeci_dict[rijec] += 1
            else:
                rijeci_dict[rijec] = 1
    
    fhand.close()
  
    jedinstvene = []
    for rijec, broj in rijeci_dict.items():
        if broj == 1:
            jedinstvene.append(rijec)
    
    print(f"Ukupno razlicitih rijeci: {len(rijeci_dict)}")
    print(f"Rijeci koje se pojavljuju samo jednom: {len(jedinstvene)}")
    print("Liste tih rijeci:")
    for rijec in jedinstvene:
        print(f"  {rijec}")
        
except FileNotFoundError:
    print("greska: Datoteka 'song.txt' nije pronadena")