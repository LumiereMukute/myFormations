from pathlib import Path
Path.home() #recuper le chemin du dossier utilisateur
Path.cwd() #le dossier courqnt
p= Path("c:\\Users\\ph\\Documents") #permet de creer un chenin personnalise
# p.parent() #pernt de recuperer le dossier pqrent de mon dossier document

# P\\Documents              on concatenne les chennin
# P\\Documents\\main.py     on concatenne les chennin
# p.joinpath("Documents","main.py")  :Permet aussi de concatenner

#  (p\\"Documents"\\"main.py").suffix   : Permet de recuper le suffix qui est "py"  on peut aussi avec joinpath

p = Path("C:\\Users\\ph\\Documents\\index.html")
print(p.name)     #nom du fichier
print(p.parent)   #recuperer le chemin parent du fichier
print(p.stem)     #partie avant extension
print(p.suffix)         #prend l'extension
print(p.suffixes)       #recuperer plusieurs extensions sous forme de liste
print(p.parts)          #prend toutes les parties du chemin
print(p.exists())       #Si le fichier existe
print(p.is_dir())       #si c'est un dissier
print(p.is_file())      #si c'est un fichier


