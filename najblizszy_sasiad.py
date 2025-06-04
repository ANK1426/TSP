from wykresy import wykres
start=[]
dist=[]
way=[]


def wykonanie(punkty):
    for i in range(len(punkty)):
        nowe_punkty = punkty[:]  # kopia listy
        nowe_punkty[0], nowe_punkty[i] = nowe_punkty[i], nowe_punkty[0]  # zamień pierwszy z i-tym
        
        dlugosc, trasa = najblizszy_sasiad(nowe_punkty)
        start.append(nowe_punkty[0])
        dist.append(dlugosc)
        way.append(trasa)
        best=dist.index(min(dist))

   
    
    print("Najlepsza trasa od sąsiadów")
    print(way[best])
    print(dist[best])
    print(start[best])
    return way[best]



def najblizszy_sasiad(punkty):
    trasa=[punkty[0]]
    pozostałe=punkty[1:]
    odleglosc=0
    while pozostałe:
        d=[]
        for x in pozostałe:
            d.append(distance(trasa[-1],x))    
        ostatni=min(d)
        odleglosc=odleglosc+ostatni
        index=d.index(ostatni)
        trasa.append(pozostałe[index])
        pozostałe.remove(pozostałe[index])

    
    odleglosc=odleglosc+distance(trasa[-1],trasa[0])
    
    trasa.append(trasa[0])
    
    return  odleglosc , trasa



def distance(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**(0.5)


