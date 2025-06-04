from najblizszy_sasiad import wykonanie
from better import opt2
from brute_force import brute_force
from wykresy import wykres

punkty = [(0, 0), (1, 1), (2, 0), (5, 5), (6, 5), (5.5, 6)]


c=wykonanie(punkty)
brute_force(punkty)
opt2(c)
