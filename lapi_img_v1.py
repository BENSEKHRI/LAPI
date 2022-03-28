import cv2
import numpy as np
import easyocr
import testes


cascade= cv2.CascadeClassifier("Ressources/haarcascade_russian_plate_number.xml")


def extract_num(img_filename):
    img=cv2.imread(img_filename)
    cv2.imshow("imgInit", img)
    cv2.imwrite("Ressources/numberPlate/EasyOCR/imgInit.png", img)
    cv2.waitKey(0)
    
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
       
        cv2.imshow("La plaque d'immatriculation", plate_gray)
        cv2.imwrite("Ressources/numberPlate/EasyOCR/numberPlate.png", plate_gray)
        cv2.waitKey(0)

    #Utilisation de "EasyOCR" pour lire le texte de la plaque d'immatriculation découpée 
    reader = easyocr.Reader(['en'], gpu=False)
    result = reader.readtext(plate_gray)
    
    #Renvoi du résultat
    if(len(result) == 0):
        print("Erreur lors de la lecture de la plaque...")
    else:
        read = result[0][-2]
        read=''.join(e for e in read if e.isalnum())
        read = read.upper()
        if len(read) == 0:
            print("Erreur lors de la lecture de la plaque...")
        else:
            print("La plaque d'immatriculation est : ", read)
            
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.rectangle(img,(x,y),(x+w,y+h),(51,51,255),2)
            res = cv2.rectangle(img,(x-1,y-40),(x+w+1,y),(51,51,255),-1)
            res = cv2.putText(img,read,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,255,255),2)

            cv2.imshow("resultat", res)
            cv2.imwrite("Ressources/numberPlate/EasyOCR/numberPlateInCar.png", res)
            cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    

extract_num("Ressources/voitures/car085.jpg")
