import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":

    filepath = "malades_trains.txt"

    with open(filepath) as fp:

        line = fp.readline()
        cnt = 1
        listoflist = []

        while line:

            line = line.rstrip()
            splittedline = line.split(" ")

            convertedline = [splittedline[0], int(splittedline[1]), int(splittedline[2])]

            listoflist.append(convertedline)

            # Une ligne correspond à un patient
            print("{} {} {}".format(convertedline[0], convertedline[1], convertedline[2]))

            line = fp.readline()
            cnt += 1

    # Transformation en tableau NumPy
    nl = np.array(listoflist, dtype=object)

    # Lecture des tailles + poids
    a = np.loadtxt(filepath, usecols=(1, 2))

    x = a[:, 0]
    y = a[:, 1]

    # Lecture des identifiants
    identifiants = np.loadtxt(filepath, usecols=0, dtype=str)
    
    fig, ax = plt.subplots()

    plt.scatter(x, y, label="Observations")

    # Ajout du nom de chaque patient près de son point
    for i in range(len(x)):
        plt.annotate(identifiants[ i],(x[i], y[i] + 0.2))

    plt.xlabel("Taille (cm)")
    plt.ylabel("Masse (kg)")
    plt.title("Taille + poids des patients")
    plt.legend()
    plt.grid()
    plt.show()