from pathlib import Path
import urllib.request
import os
import shutil

dossier_utilisateur=Path.home()

"""
ossier_utilisateur=dossier_utilisateur/"TAVAILPRATIQUE"
ossier_utilisateur.mkdir(exist_ok=True)  

#Création des dossiers

dossier_utilisateur=Path.home()/"TAVAILPRATIQUE"/"Dossier1"
dossier_utilisateur.mkdir(exist_ok=True)
dossier_utilisateur=Path.home()/"TAVAILPRATIQUE"/"Dossier2"
dossier_utilisateur.mkdir(exist_ok=True)
dossier_utilisateur=Path.home()/"TAVAILPRATIQUE"/"Dossier3"
dossier_utilisateur.mkdir(exist_ok=True)
dossier_utilisateur=Path.home()/"TAVAILPRATIQUE"/"Dossier4"
dossier_utilisateur.mkdir(exist_ok=True)
dossier_utilisateur=Path.home()/"TAVAILPRATIQUE"/"Dossier5"
dossier_utilisateur.mkdir(exist_ok=True)  


liens1="https://archive.ics.uci.edu/static/public/942/rt-iot2022.zip"
dossier_destination_1=Path.home()/"TAVAILPRATIQUE"/"Dossier1"
urllib.request.urlretrieve(liens1,dossier_destination_1)

liens2="https://archive.ics.uci.edu/static/public/602/dry+bean+dataset.zip"
dossier_destination_2=Path.home()/"TAVAILPRATIQUE"/"Dossier2"
urllib.request.urlretrieve(liens2,dossier_destination_2)

liens3="https://archive.ics.uci.edu/static/public/45/heart+disease.zip"
dossier_destination_3=Path.home()/"TAVAILPRATIQUE"/"Dossier3"
urllib.request.urlretrieve(liens3,dossier_destination_3)

liens4="https://archive.ics.uci.edu/static/public/2/adult.zip"
dossier_destination_4=Path.home()/"TAVAILPRATIQUE"/"Dossier4"
urllib.request.urlretrieve(liens4,dossier_destination_4)

liens5="https://archive.ics.uci.edu/static/public/360/air+quality.zip"
dossier_destination_5=Path.home()/"TAVAILPRATIQUE"/"Dossier5"
urllib.request.urlretrieve(liens5,dossier_destination_5)     

#Le code permetant de renommer les fichiers et les dossiers

ancien_nom = Path.home()/"TAVAILPRATIQUE"/"Dossier1"/"rt-iot2022.zip"
nouveau_nom = Path.home()/"TAVAILPRATIQUE"/"Dossier1"/"Fichier1.zip"

os.rename(ancien_nom, nouveau_nom) 

ancien_nom2 = Path.home()/"TAVAILPRATIQUE"/"Dossier2"/"heart+disease.zip"
nouveau_nom2 = Path.home()/"TAVAILPRATIQUE"/"Dossier2"/"heartanddisease.zip"

os.rename(ancien_nom2, nouveau_nom2)

ancien_nom3 = Path.home()/"TAVAILPRATIQUE"/"Dossier3"/"dry+bean+dataset.zip"
nouveau_nom3 = Path.home()/"TAVAILPRATIQUE"/"Dossier3"/"dryandbeananddataset.zip"

os.rename(ancien_nom3, nouveau_nom3)

ancien_nom4 = Path.home()/"TAVAILPRATIQUE"/"Dossier4"/"adult.zip"
nouveau_nom4 = Path.home()/"TAVAILPRATIQUE"/"Dossier4"/"adults.zip"

os.rename(ancien_nom4, nouveau_nom4)

ancien_nom5 = Path.home()/"TAVAILPRATIQUE"/"Dossier5"/"air+quality.zip"
nouveau_nom5 = Path.home()/"TAVAILPRATIQUE"/"Dossier5"/"airandquality.zip"

os.rename(ancien_nom5, nouveau_nom5)  


ancien_nom = Path.home()/"TAVAILPRATIQUE"/"Dossier1"
nouveau_nom = Path.home()/"TAVAILPRATIQUE"/"Dossier11"

os.rename(ancien_nom, nouveau_nom) 

ancien_nom2 = Path.home()/"TAVAILPRATIQUE"/"Dossier2"
nouveau_nom2 = Path.home()/"TAVAILPRATIQUE"/"Dossier22"

os.rename(ancien_nom2, nouveau_nom2)

ancien_nom3 = Path.home()/"TAVAILPRATIQUE"/"Dossier3"
nouveau_nom3 = Path.home()/"TAVAILPRATIQUE"/"Dossier33"

os.rename(ancien_nom3, nouveau_nom3)

ancien_nom4 = Path.home()/"TAVAILPRATIQUE"/"Dossier4"
nouveau_nom4 = Path.home()/"TAVAILPRATIQUE"/"Dossier44"

os.rename(ancien_nom4, nouveau_nom4)

ancien_nom5 = Path.home()/"TAVAILPRATIQUE"/"Dossier5"
nouveau_nom5 = Path.home()/"TAVAILPRATIQUE"/"Dossier55"

os.rename(ancien_nom5, nouveau_nom5)

#Code permettant de deplaplacer le fichier ver un autrer dossier

source = Path.home()/"TAVAILPRATIQUE"/"Dossier11"/"Fichier1.zip"
cible = Path.home()/"TAVAILPRATIQUE"/"Dossier33"

shutil.move(source, cible) 

source2 = Path.home()/"TAVAILPRATIQUE"/"Dossier22"/"heartanddisease.zip"
cible2 = Path.home()/"TAVAILPRATIQUE"/"Dossier11"

shutil.move(source2, cible2)

source3 = Path.home()/"TAVAILPRATIQUE"/"Dossier33"/"dryandbeananddataset.zip"
cible3 = Path.home()/"TAVAILPRATIQUE"/"Dossier55"

shutil.move(source3, cible3)

source4 = Path.home()/"TAVAILPRATIQUE"/"Dossier44"/"adults.zip"
cible4 = Path.home()/"TAVAILPRATIQUE"/"Dossier22"

shutil.move(source4, cible4)

source5= Path.home()/"TAVAILPRATIQUE"/"Dossier55"/"airandquality.zip"
cible5 = Path.home()/"TAVAILPRATIQUE"/"Dossier44"

shutil.move(source5, cible5) 


#Code permettant de créer le doublons

fichier_original = source = Path.home()/"TAVAILPRATIQUE"/"Dossier33"/"Fichier1.zip"
fichier_doublon = Path.home()/"TAVAILPRATIQUE"/"Dossier33"/"Fichier1(1).zip"

# Copie du fichier original pour créer un doublon
shutil.copyfile(fichier_original, fichier_doublon) 


fichier_original2 = Path.home()/"TAVAILPRATIQUE"/"Dossier11"/"heartanddisease.zip"
fichier_doublon2 = Path.home()/"TAVAILPRATIQUE"/"Dossier11"/"heartanddisease(1).zip"

# Copie du fichier original pour créer un doublon
shutil.copyfile(fichier_original2, fichier_doublon2)

fichier_original3 = Path.home()/"TAVAILPRATIQUE"/"Dossier55"/"dryandbeananddataset.zip"
fichier_doublon3 = Path.home()/"TAVAILPRATIQUE"/"Dossier55"/"dryandbeananddataset(1).zip"

# Copie du fichier original pour créer un doublon
shutil.copyfile(fichier_original3, fichier_doublon3)

fichier_original4 = Path.home()/"TAVAILPRATIQUE"/"Dossier22"/"adults.zip"
fichier_doublon4 = Path.home()/"TAVAILPRATIQUE"/"Dossier22"/"adults(1).zip"

# Copie du fichier original pour créer un doublon
shutil.copyfile(fichier_original4, fichier_doublon4)

fichier_original5 = Path.home()/"TAVAILPRATIQUE"/"Dossier44"/"airandquality.zip"
fichier_doublon5 = Path.home()/"TAVAILPRATIQUE"/"Dossier44"/"airandquality(1).zip"

# Copie du fichier original pour créer un doublon
shutil.copyfile(fichier_original5, fichier_doublon5)

dossier_original = Path.home()/"TAVAILPRATIQUE"/"Dossier11"
dossier_doublon = Path.home()/"TAVAILPRATIQUE"/"Dossier11(1)"

# Copie du dossier original pour créer un doublon
shutil.copyfile(dossier_original, dossier_doublon)

dossier_original2 = Path.home()/"TAVAILPRATIQUE"/"Dossier22"
dossier_doublon2 = Path.home()/"TAVAILPRATIQUE"/"Dossier22(1)"

# Copie du dossier original pour créer un doublon
shutil.copyfile(dossier_original2, dossier_doublon2)

dossier_original3 = Path.home()/"TAVAILPRATIQUE"/"Dossier33"
dossier_doublon3 = Path.home()/"TAVAILPRATIQUE"/"Dossier33(1)"

# Copie du dossier original pour créer un doublon
shutil.copyfile(dossier_original3, dossier_doublon3)

dossier_original4 = Path.home()/"TAVAILPRATIQUE"/"Dossier44"
dossier_doublon4 = Path.home()/"TAVAILPRATIQUE"/"Dossier44(1)"

# Copie du dossier original pour créer un doublon
shutil.copyfile(dossier_original4, dossier_doublon4)

dossier_original5 = Path.home()/"TAVAILPRATIQUE"/"Dossier55"
dossier_doublon5 = Path.home()/"TAVAILPRATIQUE"/"Dossier55(1)"

# Copie du dossier original pour créer un doublon
shutil.copyfile(dossier_original5, dossier_doublon5) """

information_system=os.uname()
print(information_system)

os.cpu_count()









