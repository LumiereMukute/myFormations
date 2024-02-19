from pathlib import Path

#recuper me dossier utilisareur
p=Path.home()
"""
#
p=p/"DossierTest"   #Pour l'instant le dossier n'existe pas encore
p.mkdir()   #cette fonction permet de mettre le dossier visible et si le dossier exist deja mkdir ne va pas fonctionner

#mkdir(exist_ok=True) il n'y aura pas erreur si le dossier existe deja """

"""
p=Path.home()/"DossierTest"/"1"/"2"/"3"  #créér de sous-dossier
p.mkdir(parents=True) #permet de specifier que le dossier parents exists 

# p=Path.home()/"DossierTest"/"1"/"2"/"3"/"readme.txt"
p=Path.home()/"DossierTest"/"1"/"2"/"3"/"readme.py"
p.touch() #toucch permet de voir le fichier dans le dossier """

#Le code permetant de renommer le fichier 
""""
import os

ancien_nom = Path.home()/"DossierTest"/"1"/"2"/"3"/"lumoi.txt"
nouveau_nom = Path.home()/"DossierTest"/"1"/"2"/"3"/"readme.txt"

# Renommer le fichier
os.rename(ancien_nom, nouveau_nom) """

#Code permettant de deplaplacer le fichier ver un autrer dossier
"""
import shutil

# Chemin du fichier source
source = Path.home()/"DossierTest"/"1"/"2"/"3"/"readme.txt"

# Chemin du dossier cible
cible = Path.home()/"DossierTest"/"1"/"2"

# Déplacer le fichier du dossier source vers le dossier cible
shutil.move(source, cible)

print(f"Le fichier a été déplacé de {source} vers {cible}") """

#Code permettant de créer le doublons
"""
import shutil

# Chemin du fichier original
fichier_original = Path.home()/"DossierTest"/"1"/"2"/"3"/"readme.py"

# Chemin du fichier doublon
fichier_doublon = Path.home()/"DossierTest"/"1"/"2"/"3"/"readme(1).py"

# Copie du fichier original pour créer un doublon
shutil.copyfile(fichier_original, fichier_doublon)

print("Le doublon du fichier a été créé avec succès.")""" 

# La suppression de fichier dans un dossier
"""
fichier_a_supprimer = Path.home()/"DossierTest"/"1"/"2"/"3"/"readme.py"
if fichier_a_supprimer.exists():
    fichier_a_supprimer.unlink()  // unlik permet de supprimer le fichier
    print ("La suppression a reussi")
else:
    print("Les fichier n'existe pas") """

#la commade permettant de supprimer le dossier
"""
repertoire_a_supprimer= Path.home()/"DossierTest"/"1"/"2"/"3"

repertoire_a_supprimer.rmdir()"""


 










