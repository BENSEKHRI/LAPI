import os
import pathlib
import json
from Bio import pairwise2
from Bio.pairwise2 import format_alignment



voitures = r"C:\Users\HP\OneDrive\Bureau\LAPI\Ressources\voitures"


# Renvoi le nombre de fichier d'un dossier - dans notre cas on choisi le dossier "voitures"
def nbFileDir (voitures) :
    initial_count = 0
    for path in pathlib.Path(voitures).iterdir():
        if path.is_file():
            initial_count += 1
    return initial_count


# Renvoi le nom de la i ème voiture du dossier "voitures"
def render_i_cars (i):
    cars = os.listdir(voitures)
    return cars[i]


#Renvoi la i ème plaque d'immatriculation du fichier "number_plate.txt"
def render_i_number_plates (i):
    chemin = r"C:\Users\HP\OneDrive\Bureau\LAPI\Ressources\number_plate.txt"
    
    with open(chemin, "r", encoding='utf_8') as f:
        contenu = f.read().splitlines()
        return contenu[i]


# Ajoute des dossier (list) à notre fichier data.json
def addXToJson(chemin, x): 
    
    with open(chemin, "r",) as f:
        data = json.load(f)

    data.append(x)

    with open(chemin, "w",) as f:
        json.dump(data, f, indent=4)
       
       
#compare deux chaine de caractère et renvoi le taux de compatibilité de dest par rapport à str en % 
def compareStr (src, dest):
    alignments = pairwise2.align.globalxx(src, dest)
    tauxDeCompatibilite = format_alignment(*alignments[0])
    taille = len(src)
    return int((tauxDeCompatibilite * 100) / taille)
        
