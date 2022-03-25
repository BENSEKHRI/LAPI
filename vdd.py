import matplotlib.pyplot as plt
import numpy as np
import json



#Lecture d'un fichier json
data1 = r"C:\Users\HP\OneDrive\Bureau\LAPI\Ressources\json\data1.json"
data2 = r"C:\Users\HP\OneDrive\Bureau\LAPI\Ressources\json\data2.json"


# Création d'un graphique à partir de données d'un fichier json
def graphique(data, ocr):
    with open(data, "r",) as a:
        df1 = json.load(a)
        x = np.linspace(1, 99, 100)
        
        plt.figure(figsize=(12,8))
        plt.title(f'Taux de réussite de lecture des plaques d\'immatriculation avec {ocr}\n')
        plt.plot(x, df1, label = ocr, c='grey')
        plt.xlabel('Voitures')
        plt.ylabel('Taux de réussite de lecture %')
        plt.legend()
        plt.savefig(f'Ressources/plt/GraphiqueTauxDeRéussite{ocr}.png')
        plt.show()
    

# Création deux (02) graphiques à partir de deux données json 
def graphique2 (data1, data2):
    with open(data1, "r",) as a:
        with open(data2, "r",) as b:
            df1 = json.load(a)
            df2 = json.load(b)
            x = np.linspace(1, 99, 100)

            plt.figure(figsize=(12,8))
            plt.subplot(2, 1, 1)
            plt.title('Taux de réussite de lecture des plaques d\'immatriculation avec EasyOCR et Tesseract\n')
            plt.plot(x, df1, label = 'EasyOCR', c='green')
            plt.xlabel('Voitures')
            plt.ylabel('Taux de réussite de lecture %')
            plt.legend()
            
            plt.subplot(2, 1, 2)
            plt.plot(x, df2, label = 'Tesseract', c='blue')
            plt.xlabel('Voitures')
            plt.ylabel('Taux de réussite de lecture %')
            plt.legend()
            plt.savefig('Ressources/plt/GraphiqueTauxDeRéussiteEasyOCR_Tesseract.png')
            plt.show()


# Création d'un histograme à partir de données json
def histogramme (data, ocr):
    with open(data, "r",) as a:
        df1 = json.load(a)
     
        plt.figure(figsize=(12,8))
        plt.title(f'Taux de réussite de lecture des plaques d\'immatriculation avec {ocr}\n')
        plt.hist(df1, edgecolor='white', color = 'grey', label = ocr)
        plt.xlabel('Taux de réussite de lecture %')
        plt.ylabel('Nombre de voitures')
        plt.legend()
        plt.savefig(f'Ressources/plt/DiagrammeTauxDeRéussite{ocr}.png')
        plt.show()
        
        
# Création de deux (02) histogramme à partir de deux données json
def histogramme2 (data1, data2):
    with open(data1, "r",) as a:
        with open(data2, "r",) as b:
            df1 = json.load(a)
            df2 = json.load(b)
            
            plt.figure(figsize=(12,8))
            plt.subplot(2,1,1)
            plt.title('Taux de réussite de lecture des plaques d\'immatriculation avec EasyOCR et Tesseract\n')
            plt.hist(df1, edgecolor='white', color = 'green', label = 'EasyOCR')
            plt.xlabel('Taux de réussite de lecture %')
            plt.ylabel('Nombre de voitures')
            plt.legend()
            
            plt.subplot(2,1,2)
            plt.hist(df2, edgecolor='white',color = 'blue', label = 'Tesseract')
            plt.xlabel('Taux de réussite de lecture %')
            plt.ylabel('Nombre de voitures')
            plt.legend()
            plt.savefig('Ressources/plt/DiagrammeTauxDeRéussiteEasyOCR_Tesseract.png')
            plt.show()


graphique(data1, "EasyOCR")
graphique(data2, "Tesseract")
graphique2(data1, data2)

histogramme(data1, "EasyOCR")
histogramme(data2, "Tesseract")
histogramme2(data1, data2)




    