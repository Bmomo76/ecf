#importer les bibl
import os
import re#ouvrir  lire le fichier en ligne
fichier=open('input-emails.txt','r')
lines=fichier.readlines()
fichier.close()
liste=[] #créer une liste vide
motif=r'\b[a-zA-Z0-9_.%+-]+@[A-Za-z0-9._-]+\.[fr]{2,}\b' #resgex pour mail
for i in range(len(lines)):
    line=lines[i][39:].strip('\n') # prendre que l'adresse mail
    if re.match(motif,line):      # verifier que c'est une fr
        liste.append(line)
print(liste)


