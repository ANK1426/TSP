from wykresy import wykres
from brute_force import total_dys
start=[]
dist=[]
way=[]


def wykonanie(punkty): #warunek sensowności programu
    if not punkty:
        print("Błąd: lista punktów jest pusta.")
        return []

    if len(punkty) < 2:
        print("Błąd: potrzebne są co najmniej dwa punkty.")
        return []

def distance(a,b): 
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**(0.5)


def najblizszy_sasiad(punkty): #sam algorytm najlbiższego sąsiada
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

#ostateczne wersja
def wykonanie(punkty):
    for i in range(len(punkty)):
        nowe_punkty = punkty[:]  # kopia listy
        nowe_punkty[0], nowe_punkty[i] = nowe_punkty[i], nowe_punkty[0]  # zamień pierwszy z i-tym
        
        dlugosc, trasa = najblizszy_sasiad(nowe_punkty)
        start.append(nowe_punkty[0])
        dist.append(dlugosc)
        way.append(trasa)
        best=dist.index(min(dist))

    print("Dla najbliższego sąsiada")
    print(f"Minimalny dystans to: {total_dys(way[best])}, dla punktów:{way[best]}" )
    
    return way[best] ,total_dys(way[best])



