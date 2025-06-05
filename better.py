from brute_force import total_dys , distance



def opt2(way):
    way=way.copy()
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
    print("Dla OPT2")
    print(f"Minimalny dystans to: {total_dys(way)} dla punktów {way}" )
  
    
    return way ,total_dys(way)
