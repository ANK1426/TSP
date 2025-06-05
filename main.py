from better import opt2
from brute_force import brute_force
from wykresy import wykres
from zlozonosc import zlozonosc
from najblizszy_sasiad import wykonanie

import time


punkty = [(0, 0),(2, 10),(4, 0),(6, 10),(8, 0),(10, 10),(5.6, 5.4)]
all_way=[]
all_dist=[]


start_time = time.time()
bruteforceway, bruteforcedist = brute_force(punkty)
all_way.append(bruteforceway)
all_dist.append(bruteforcedist)
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
nnway, nndist = wykonanie(punkty)
all_way.append(nnway)
all_dist.append(nndist)

print("--- %s seconds ---" % (time.time() - start_time))

optway, optdist = opt2(nnway)
all_way.append(optway)
all_dist.append(optdist)


wykres(all_way, all_dist)

zlozonosc()
