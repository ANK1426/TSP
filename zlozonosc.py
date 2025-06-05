import matplotlib.pyplot as plt
import math as m

n=[x for x in range(1,12)]

brute_force = [m.factorial((n-1))/2 for n in n]
nn = [n**3 for n in n]
opt2 = [n**3+n+n**2 for n in n]

def zlozonosc():
    plt.figure(figsize=(12, 6))

    plt.plot(n,brute_force,label="Brute force O(n!)",marker='s')
    plt.plot(n,nn,label="Najbliższy sąsiad O(n^3)",marker='s')
    plt.plot(n,opt2,label="Najbliższy sąsiad + opt2 O(n^3)+O(n^2)",marker='s')
    plt.legend()
    plt.title("Wykres złożoności obliczeniowej dla różnych algorytmów w problemie komwojażera")
    plt.xlabel("Ilość punktów")
    plt.ylabel("Ilosc operacji - skala log")
    plt.yscale("log")
    plt.grid()



    plt.show()
