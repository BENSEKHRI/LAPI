import cv2
import numpy as np
import easyocr
import testes
import time



cascade= cv2.CascadeClassifier("Ressources/haarcascade_russian_plate_number.xml")


def extract_number_plate (img_filename):
    img=cv2.imread(img_filename)
    
    #Image en gris
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    nplate=cascade.detectMultiScale(gray,1.1,4)
    
    #crop portion
    for (x,y,w,h) in nplate:
        wT,hT,cT=img.shape
        a,b=(int(0.02*wT),int(0.02*hT))
        plate=img[y+a:y+h-a,x+b:x+w-b,:]
        
        #make the img more darker to identify LPR
        kernel=np.ones((1,1),np.uint8)
        plate=cv2.dilate(plate,kernel,iterations=1)
        plate=cv2.erode(plate,kernel,iterations=1)
        plate_gray=cv2.cvtColor(plate,cv2.COLOR_BGR2GRAY)
        
        return plate_gray
         
            
def imgToNumber (plateNumber) : 
    #Utilisation de "EasyOCR" pour lire le texte de la plaque d'immatriculation découpée 
    reader = easyocr.Reader(['en'], gpu=False)
    result = reader.readtext(plateNumber)
    #Renvoi du résultat
    if(len(result) == 0):
        return 0
    else:
        read = result[0][-2]
        read=''.join(e for e in read if e.isalnum())
        read = read.upper()
        if len(read) == 0:
            return 0
        else:
            return read            
    

voitures = r"C:\Users\HP\OneDrive\Bureau\LAPI\Ressources\voitures"
data1 = r"C:\Users\HP\OneDrive\Bureau\LAPI\Ressources\json\data1.json"

def main () :
    start = time.time()
    for i in range(0,testes.nbFileDir(voitures)):
        img_filename = f"Ressources/voitures/{testes.render_i_cars(i)}"
        print("Traitement de la voiture : " + testes.render_i_cars(i))
        res = imgToNumber(extract_number_plate(img_filename))
        if res == 0 or res == None:
            testes.addXToJson(data1, 0)
            print("Erreur de lecture de la plaque :(\n")
            print("Voici la vraie plaque d'immatriculation    : " + testes.render_i_number_plates(i))
            print("Taux de réussite de lecture: 0 %\n")
        else:
            print("Voici la plaque d'immatriculation lue   : " + str(res))
            testes.addXToJson(data1, testes.compareStr(testes.render_i_number_plates(i), res))
            print("Voici la vraie plaque d'immatriculation : " + testes.render_i_number_plates(i))
            print("Taux de réussite de lecture:", testes.compareStr(testes.render_i_number_plates(i), res), "%\n")
        

    end = time.time()

    print("Le temps total écoulé depuis le début du programme est:",(end - start))

main()   




