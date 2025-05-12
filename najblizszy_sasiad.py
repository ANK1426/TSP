from wykresy import wykres


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
    wykres(trasa)
    return  odleglosc , trasa



def distance(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**(0.5)


print(najblizszy_sasiad([[1,2],[4,5],[0,4],[5,5]]))