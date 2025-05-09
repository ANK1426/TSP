#Algorytm brute-force, czyli szukamy wszystkich możliwych dróg
#i wybieramy najkrótszą. Złożonośc obliczeniowa (n-1)!/2


def permutacja(lista): #wyznacza permutacje zbioru [1,...,n]
    if len(lista) == 0:
        return [[]]

    b = []
    for i in range(len(lista)):
        x = lista[:i] + lista[i+1:]
        for perm in permutacja(x):
            b.append([lista[i]] + perm)
    return b

def odp(n):  #ignoruje permutacje w odwrotnej kolejności
    b = permutacja([i for i in range(1, n)])
    for i in range(len(b)):
        b[i].insert(0, 0) #tutaj strategicznie dodajemy zero na początku i na końcu
        b[i].append(0)

    final = []
    for trasa in b:
        odwrotna = trasa[::-1]
        if odwrotna not in final and trasa not in final:
            final.append(trasa)

    return final


def distance(a,b): #dystans pomiędzy dwoma dowolnymi punktami
    return (((a[0]-b[0])**2+(a[1]-b[1])**2)**(0.5))

def total_dys(lista): #całkowity dystans, czyli suma po parach
    d=0
    for i in range(len(lista)-1):
        d+=distance(lista[i],lista[i+1])
    return d

def brute_force(parametry):
    n=len(parametry)
    slownik={}
    for i in range(n): #to słownik postaci {0:(pierwsza para współrzędnych)...}
        slownik[i]=parametry[i]
    kolejnosc=odp(n)
    m=len(kolejnosc)
    print(kolejnosc) 
    for i in range(m): #zmieniamy tablice z np. [0,1,2] na [(0,1),(2,3),(4,5)]
        for j in range(n+1):
            kolejnosc[i][j]=slownik[kolejnosc[i][j]]
    print(kolejnosc)
    min=kolejnosc[0]
    for i in range(m):
        if total_dys(kolejnosc[i]) < total_dys(min):
            min=kolejnosc[i]
    return total_dys(min) #wynik to minimalny dystans