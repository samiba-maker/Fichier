import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':

    # On utilise numpy pour lire le fichier
    a = np.loadtxt("malades_trains.txt")

    # On sort les observations des data
    x = a [:,0] # Slicing ! mais lequel ?
    y = a [:,1]

    print(x, y)

    # On fait une figure !
    fig = plt.figure()
    plt.scatter(x,y,label="Obs") # Affichage des obs

    plt.grid(True)
    plt.xlabel ('x : Taille(cm)')
    plt.ylabel ('y : Poids(Kg)')
    plt.title ("Regression Lineaire")
    plt.legend()
    plt.show()