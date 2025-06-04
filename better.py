def distance(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**(0.5)

def calydyst(way):
    total = 0
    for k in range(len(way) - 1):
        total += distance(way[k], way[k + 1])
    # dodajemy odcinek powrotny do punktu startowego
    total += distance(way[-1], way[0])
    return total


def opt2(way):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(way) - 2):
            for j in range(i + 1, len(way) - 1):
                old = distance(way[i - 1], way[i]) + distance(way[j], way[j + 1])
                new = distance(way[i - 1], way[j]) + distance(way[i], way[j + 1])
                if old > new:
                    way[i:j + 1] = reversed(way[i:j + 1])
                    improved = True
    print("dla OPT2")
    print(way)
    print(calydyst(way))
    return way
