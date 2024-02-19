from pathlib import Path
import urllib.request
import os

dossier_utilisateur=Path.home()
"""
ossier_utilisateur=dossier_utilisateur/"TAVAIL PRATIQUE D'IA"
ossier_utilisateur.mkdir(exist_ok=True)  

#Création des dossiers

dossier_utilisateur=Path.home()/"TAVAIL PRATIQUE D'IA"/"Dossier 1"
dossier_utilisateur.mkdir(exist_ok=True)
dossier_utilisateur=Path.home()/"TAVAIL PRATIQUE D'IA"/"Dossier 2"
dossier_utilisateur.mkdir(exist_ok=True)
dossier_utilisateur=Path.home()/"TAVAIL PRATIQUE D'IA"/"Dossier 3"
dossier_utilisateur.mkdir(exist_ok=True)
dossier_utilisateur=Path.home()/"TAVAIL PRATIQUE D'IA"/"Dossier 4"
dossier_utilisateur.mkdir(exist_ok=True)
dossier_utilisateur=Path.home()/"TAVAIL PRATIQUE D'IA"/"Dossier 5"
dossier_utilisateur.mkdir(exist_ok=True)                             

liens1="https://archive.ics.uci.edu/static/public/942/rt-iot2022.zip"
dossier_destination_1=Path.home()/"TAVAIL PRATIQUE D'IA"/"Dossier 1"
urllib.request.urlretrieve(liens1,dossier_destination_1)

liens2="https://archive.ics.uci.edu/static/public/602/dry+bean+dataset.zip"
dossier_destination_2=Path.home()/"TAVAIL PRATIQUE D'IA"/"Dossier 2"
urllib.request.urlretrieve(liens2,dossier_destination_2)

liens3="https://archive.ics.uci.edu/static/public/45/heart+disease.zip"
dossier_destination_3=Path.home()/"TAVAIL PRATIQUE D'IA"/"Dossier 3"
urllib.request.urlretrieve(liens3,dossier_destination_3)

liens4="https://archive.ics.uci.edu/static/public/2/adult.zip"
dossier_destination_4=Path.home()/"TAVAIL PRATIQUE D'IA"/"Dossier 4"
urllib.request.urlretrieve(liens4,dossier_destination_4)

liens5="https://archive.ics.uci.edu/static/public/360/air+quality.zip"
dossier_destination_5=Path.home()/"TAVAIL PRATIQUE D'IA"/"Dossier 5"
urllib.request.urlretrieve(liens5,dossier_destination_5)  """


ancien_nom = Path.home()/"TAVAIL PRATIQUE D'IA"/"Dossier 1"/"rt-iot2022.zip"
nouveau_nom = Path.home()/"TAVAIL PRATIQUE D'IA"/"Dossier 1"/"Fichier1.zip"

os.rename(ancien_nom, nouveau_nom)












