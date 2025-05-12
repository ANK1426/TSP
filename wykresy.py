import matplotlib.pyplot as plt
import numpy as np

def wykres(a):
    x= [punkt[0] for punkt in a]
    y= [punkt[1] for punkt in a]
    plt.plot(x,y,color='blue',label='Punkty',linestyle='-',marker='o')
    plt.show()



   