import json

""" OUVRIR ET LIRE UN FICHIER
with open(chemin,"r") as f:
    contenu = f.read().splitlines()
    print(contenu)

"""
"""
chemin = "C:\\Users\\hp\\Documents\\Fichier.txt"

ce code pour ecrire da ns un fichier "w" pour ecraser et "a" pour ajouter
with open(chemin,"a") as f:
    f.write("\n Au revoir")
"""
chemin = "C:\\Users\\hp\\Documents\\Fichier.json"
with open(chemin,"w") as f:
    json.dump("Marc", f)


# LA SUITE DANS UN AUTRE FICHIER

# we learn now
    
