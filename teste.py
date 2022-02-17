import pyautogui
import random
import time
import dotenv
import os
import cv2
from tkinter import *
import datetime

dotenv.load_dotenv()

# pastaApp=os.path.dirname('./')
# app=Tk()
# app.title("teste123")

# imgLogo=PhotoImage(file=pastaApp+"\\assets\\teste.png")
# l_logo=Label(app, image=imgLogo)
# l_logo.place(x=10, y=10)
# # cv2.imwrite('imagem'+'_tratada'+'.png', imgLogo)
# app.mainloop()

# def convertImage(): 
#     img = Image.open("./assets/teste.png") 
#     img = img.convert("RGBA") 
  
#     datas = img.getdata() 
  
#     newData = [] 
  
#     for items in datas: 
#         if item[0] == 255 and item[1] == 255 and item[2] == 255: 
#             newData.append((255, 255, 255, 0)) 
#         else: 
#             newData.append(item) 
  
#     img.putdata(newData) 
#     img.save("./New.png", "PNG") 
#     print("Successful") 
  
# # convertImage() 

def tratarImagem(imagem):
    imagem = cv2.imread('assets/'+imagem+'.png')
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
    _, imagem_tratada = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_OTSU)
    cv2.imwrite('imagem'+'_tratada'+'.png', imagem_tratada)
    return imagem_tratada

def procurarImagemSemRetornarErro(imagem):
    confidence = os.getenv("CONFIDENCE")
    img = None
    contador = 0
    if (imagem == "metamaskNotification"):
        time.sleep(10)
    while img == None:
        img = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
        if img != None:
            print('Achei a imagem: ' + imagem)
            print(img)
            return True
        contador += 1
        if contador >= 5:
            img = True
    print('Não consegui encontrar a imagem: ' + imagem)
    return False

def procurarLocalizacaoDaImagemPelosEixos(imagem):
    print('Utiliando a func procurarLocalizacaoDaImagemPelosEixos: ' + imagem)
    print('*' + '-' * 100 + '*')
    contador = 0
    while contador < 25:
        if procurarImagemSemRetornarErro(imagem):
            confidence = os.getenv("CONFIDENCE")
            try:
                x, y = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
                loop = False
                if x != None:
                    print('Clicando em: ' + str(x)+ ', ' + str(y))
                    return x, y
                else:
                    print('Erro na func procurarLocalizacaoDaImagemPelosEixos')
            except:
                print("Erro ao procurar imagem: " + imagem)            
        else:
             contador += 1
    print('*' + '-' * 100 + '*')
    return None, None

def confirmMap():
    if procurarImagemSemRetornarErro("confirmDentroDoJogo"):
        pyautogui.click(procurarLocalizacaoDaImagemPelosEixos("confirmDentroDoJogo"), duration = 1)




pyautogui.moveTo()
# print(pyautogui.position())







# for i in range(13, 16):
#     print(i)
# valor = round(random.uniform(0,3), 10)
# valor2 = random.uniform(1, 5)
# print(valor)
# print(valor2)
# pyautogui.moveTo(1003,339, duration = random.uniform(1, 10))

# img = pyautogui.locateCenterOnScreen('./assets/15de15.png', confidence=0.95)
# print(img)

# def fight():
#     x, y = pyautogui.locateCenterOnScreen('./assets/fight.png', confidence=0.95)
#     print(x,y)
#     time.sleep(1)
#     img = pyautogui.locateCenterOnScreen('./assets/energy.png', confidence=0.95, region=(x-420,y-80, 450,100))


#     # pyautogui.screenshot('my_screenshot.png', region=(x2, y2)) 
# fight()


# pyautogui.moveTo(1582, 640, duration = 1)

# time.sleep(2)
# # try:
# x, y = pyautogui.locateCenterOnScreen('./assets/surrenderInTheGame.png', confidence=0.95)
# variacaoDoY = 57
# newY = y
# retorno = []
# loopOfWhile = True
# timeDeEntrada = datetime.datetime.utcnow()
# timeDeSaida = datetime.datetime.utcnow()
# while loopOfWhile:
#     for i in range(6):
#         img = pyautogui.locateOnScreen('./assets/xVermelhoEmCimaDaNave.png', confidence=0.95, region=(x-30,(newY+49+variacaoDoY), 56,50) )
#         newY+= 57  
#         if img == None:  
#             retorno.append(False)
#         else:
#             retorno.append(True)
#     loopOfWhile = False
#     for i in retorno:
#         if i == False:
#             loopOfWhile = True
#     print(retorno)
#     retorno = []
#     newY = y
#     confirmMap()
#     timeDeSaida = datetime.datetime.utcnow()
#     timeTotal = timeDeSaida - timeDeEntrada
#     if (timeTotal.total_seconds() >= 900):
#         loopOfWhile = False



# for i in range(90):
#     time.sleep(1)
#     confirmMap()
# print("Sai do loop")


# x, y = pyautogui.locateCenterOnScreen('./assets/surrenderInTheGame.png', confidence=0.95)
# variacaoDoY = 56
# retorno = []
# newY = y
# pyautogui.screenshot('my_screenshot.png', region=(x-25,(newY+54+variacaoDoY), 45,40))
# img = pyautogui.locateCenterOnScreen('./assets/xVermelhoEmCimaDaNave.png', confidence=0.8, region=(x-25,(newY+54+variacaoDoY), 45,40))
# print(img)







# except:
#     print("teste")

# pyautogui.screenshot('my_screenshot.png', region=(x-20,y+110, 40,40))

# print(img)
# time.sleep(2)
# 
# while True:
#     pyautogui.moveTo(random.uniform(0, 1000), random.uniform(0, 1000), duration = random.uniform(1, 10))

# timeSleep = random.randint(5500, 11000)
# contador = 0
# while contador < timeSleep:
#     time.sleep(1)
#     if contador % 30 == 0:
#         durationRange = random.uniform(1, 10)
#         timeAcrescimo = durationRange // 1
#         contador += timeAcrescimo
#         pyautogui.moveTo(random.uniform(0, 1000), random.uniform(0, 1000), duration = durationRange)
#     contador += 1


#
# img = pyautogui.locateCenterOnScreen('./assets/0de15DentroDoUniverso.png', confidence=0.9)
# print(img)
# pyautogui.click(img)