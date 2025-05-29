from wykresy import wykres
start=[]
dist=[]
way=[]


def wykonanie(punkty):
    for i in range(len(punkty)):
        nowe_punkty = punkty[:]  # kopia listy
        nowe_punkty[0], nowe_punkty[i] = nowe_punkty[i], nowe_punkty[0]  # zamień pierwszy z i-tym
        print(f"Startowy punkt: {nowe_punkty[0]}")
        dlugosc, trasa = najblizszy_sasiad(nowe_punkty)
        print(f"Długość trasy: {dlugosc}")
        print(f"Trasa: {trasa}\n")
        start.append(nowe_punkty[0])
        dist.append(dlugosc)
        way.append(trasa)

    wykres(start,way,dist)
    print(way)
    print(dist)
    print(start)




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


print(wykonanie([[1,2],[4,5],[0,4],[5,5]]))