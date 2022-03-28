# Mohand Lounis BENSEKHRI
# N° étudiant: 11710457
# Master 1 Informatique 
# Université Sorbonne Paris Nord - Institut Galilée 
# 28/03/2022

# Initiation à la recherche
# LAPI "Lecture automatique des plaques d’immatriculation"
La reconnaissance automatisée des plaques minéralogiques également appelée LAPI "Lecture automatique des plaques d’immatriculation" ou en anglais Automatic number-plate recognition (ANPR) est une technologie destinée à identifier les plaques d'immatriculation de véhicules via l'utilisation de techniques de reconnaissance optique de caractères (OCR).

# Pré-requis
    * python 3.9.7
    * pip

    * cv2
    * easyocr
    * pytesseract
    * matplotlib
    * pathlib
    * os
    * Bio
    * numpy
    * time

# Contenu du répertoire LAPI
    Ressources
        json : 
            dossier qui contient l'ensemble des taux de réussite de lecture dans les fichier dataX | le fichier number_plate contient la liste de toutes les places des voitures utilisées.
        numberPlate :
            EasyOCR:
                Contient les images que l'on créer lors de lancement de " lapi_img_v1.py "
            Tesseract:
                Contient les images que l'on créer lors de lancement de " lapi_img_v2.py "
        plt :
            Contient l'ensemble des diagramme et graphiques que l'ont créer lors de lancement de " vdd.py "
        voitures : 
            Contient les 100 images des véhicules qui sont utilisées lors des testes.
        haarcascade_russian_plate_number.xml: 
            fichier obligatoire pour la découpe de la plaque d'immatriculation
        number_plate.txt :
            Contient l'ensemble des plaque des matriculation en text contrairement aux fichier json où elles sont sous forme d'une liste
    
    lapi_img_v1.py : 
        fichier qui permet de visualiser la découpe et la lecture de la plaque d'immatriculation pour un véhicule choisie - EasyOCR
    
    lapi_img_v2.py :
        fichier qui permet de visualiser la découpe et la lecture de la plaque d'immatriculation pour un véhicule choisie - Tesseract
    
    lapi_v1.py : 
        fichier qui permet de lancer l'expérience pour les 100 véhicules - EasyOCR
    
    lapi_v2.py :
        fichier qui permet de lancer l'expérience pour les 100 véhicules - Tesseract

    testes.py : 
        fichier qui contient l'ensemble des fonction de test
    
    vdd.py :
        fichier qui permet de modéliser les résultats en diagramme et graphiques
 
# Exécution
    python monFichier.py
