import numpy as np

filepath = "malades_trains.txt"

# Ouverture du fichier en lecture
with open(filepath) as fp:

    # Lecture de la première ligne
    line = fp.readline()

    # Compteur de lignes
    cnt = 1

    # Liste qui contiendra toutes les lignes converties
    listoflist = []

    # On continue tant que la ligne n'est pas vide
    while line:

        # Affichage du numéro et du contenu brut de la ligne
        print("Line {}: {}".format(cnt, repr(line)))

        # Suppression du retour à la ligne final
        line = line.rstrip()

        # Affichage de la ligne nettoyée
        print("Line {}: {}".format(cnt, line))

        # Découpage de la ligne à chaque espace
        splittedline = line.split(" ")

        # Affichage de la ligne découpée
        print("Splitted Line : {}".format(splittedline))

        # Conversion des chaînes de caractères en entiers
        convertedline = [int(num) for num in splittedline]

        # Ajout de la ligne convertie dans la liste principale
        listoflist.append(convertedline)

        # Affichage de la liste de listes construite
        print("listoflist : {}".format(listoflist))

        # Lecture de la ligne suivante
        line = fp.readline()

        # Passage au numéro de ligne suivant
        cnt += 1

# Transformation de la liste de listes en tableau NumPy
nl = np.array(listoflist)

print(nl)
