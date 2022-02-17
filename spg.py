import pyautogui
import random
import time
import dotenv
import os
import datetime

dotenv.load_dotenv()

def reiniciarAPagina():
    pyautogui.keyDown("ctrl")
    pyautogui.press("f5")
    pyautogui.keyUp("ctrl")
    time.sleep(5)

def durationChoosed():
    # durationChoosed = float(os.getenv("DURATION")) + round(random.uniform(0,3), 10)
    return 1

def conectarFunc():
    contador = 0
    connect = True
    assinarClick = False
    playClick = False
    connectWallet = False
    pyautogui.click(procurarLocalizacaoDaImagemPelosEixos("spaceCrypto"), duration = 2)
    time.sleep(2)
    reiniciarAPagina()
    while connect == True:
        if contador == 50:
            raise Exception("Erro ao tentar realizar o login")
        if connectWallet == False and procurarImagemSemRetornarErro("connectWallet"):
            pyautogui.click(procurarLocalizacaoDaImagemPelosEixos("connectWallet"), duration = durationChoosed())
            connectWallet = True
        if assinarClick == False and connectWallet == True and (procurarImagemSemRetornarErro("assinar") or procurarImagemSemRetornarErro("metamaskNotification")):
            if procurarImagemSemRetornarErro("assinar"):
                pyautogui.click(procurarLocalizacaoDaImagemPelosEixos("assinar"), duration = durationChoosed())
            elif procurarImagemSemRetornarErro("metamaskNotification"):
                pyautogui.click(procurarLocalizacaoDaImagemPelosEixos("metamaskNotification"), duration = durationChoosed())
                time.sleep(5)
                pyautogui.click(procurarLocalizacaoDaImagemPelosEixos("assinar"), duration = durationChoosed())
            assinarClick = True
        if playClick == False and assinarClick == True and connectWallet == True and procurarImagemSemRetornarErro("play"):
            pyautogui.click(procurarLocalizacaoDaImagemPelosEixos("play"), duration = durationChoosed()) 
            playClick = True
            connect = False
        contador += 1

def dragInTheMenu1x():
    x, y = procurarLocalizacaoDaImagemPelosEixos("setaDeEscolha")
    pyautogui.moveTo(x, y+440)
    pyautogui.mouseDown(button='left')
    #BEM MELHOR usar moveTo no lugar de dragTO
    pyautogui.moveTo(x, y+40, duration=3)
    # pyautogui.dragTo(x, y+40, duration = 3)
    time.sleep(4)
    pyautogui.mouseUp(button='left')
    time.sleep(2)

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
                if x != None:
                    print('Clicando em: ' + str(x)+ ', ' + str(y))
                    return x, y
                else:
                    print('Erro na func procurarLocalizacaoDaImagemPelosEixos')
            except:
                raise("Nao achei a imagem: "+ imagem)         
        else:
             contador += 1
    print('*' + '-' * 100 + '*')
    return None, None

# Procura pela região em torno do botão fight se essa nave deve ou não ir batalhar
def fight():
    print('*' + '-' * 100 + '*')
    print('Utiliando a func FIGHT')
    loop = True
    contador = 0
    while loop:
        if not procurarImagemSemRetornarErro("15de15"):
            # try:
                img = pyautogui.locateCenterOnScreen('./assets/energy.png', confidence=0.9)
                if img != None:
                    x, y = img
                    # x2, y2 = pyautogui.locateCenterOnScreen('./assets/fight.png', confidence=0.9)
                    if x != None:
                        pyautogui.click(x+160, y+50, duration = durationChoosed())
                        time.sleep(1)
                else:
                    dragInTheMenu1x()
                    contador += 1
                    if contador >= 30:
                        loop = False
            # except:
            #     print("Erro na func fight, ao procurar imagem: FIGHT")   
        else:
            loop = False
    print('*' + '-' * 100 + '*')

def fightBoss():
    confirmMap()
    time.sleep(2)
    if procurarImagemSemRetornarErro("fightBoss"):
        pyautogui.click(procurarLocalizacaoDaImagemPelosEixos("fightBoss"), duration = durationChoosed())

def confirmLose():
    confirmMap()
    time.sleep(5)
    if procurarImagemSemRetornarErro("confirmLose"):
        pyautogui.click(procurarLocalizacaoDaImagemPelosEixos("confirmLose"), duration = durationChoosed())
        pyautogui.moveTo(100, 100)

def confirmMap():
    if procurarImagemSemRetornarErro("confirmDentroDoJogo"):
        pyautogui.click(procurarLocalizacaoDaImagemPelosEixos("confirmDentroDoJogo"), duration = durationChoosed())
    if procurarImagemSemRetornarErro("confirmLose"):
        pyautogui.click(procurarLocalizacaoDaImagemPelosEixos("confirmLose"), duration = durationChoosed())

def backToMenu():
    confirmMap()
    if procurarImagemSemRetornarErro("ship"):
        pyautogui.click(procurarLocalizacaoDaImagemPelosEixos("ship"), duration = durationChoosed())

def clickInTheXOfShips():
    confirmMap()
    if procurarImagemSemRetornarErro("xShips"):
        pyautogui.click(procurarLocalizacaoDaImagemPelosEixos("xShips"), duration = durationChoosed())

def findShipByTheRegion():
    print('Utiliando a func findShipByTheRegion')
    contador = 0
    time.sleep(3)
    loopSurrender = procurarImagemSemRetornarErro("surrenderInTheGame")
    while not loopSurrender:
        confirmMap()
        contador += 1
        print("Esperando aparecer a imagme: surrenderInTheGame!")
        if contador == 20:
            loopSurrender = True

    if procurarImagemSemRetornarErro("surrenderInTheGame"):
        try:
            x, y = pyautogui.locateCenterOnScreen('./assets/surrenderInTheGame.png', confidence=0.95)
            variacaoDoY = 57
            newY = y
            retorno = []
            loopOfWhile = True
            timeDeEntrada = datetime.datetime.utcnow()
            timeDeSaida = datetime.datetime.utcnow()
            while loopOfWhile:
                for i in range(6):
                    img = pyautogui.locateOnScreen('./assets/xVermelhoEmCimaDaNave.png', confidence=0.95, region=(x-30,(newY+49+variacaoDoY), 56,50) )
                    newY+= 57  
                    if img == None:  
                        retorno.append(False)
                    else:
                        retorno.append(True)
                loopOfWhile = False
                for i in retorno:
                    if i == False:
                        loopOfWhile = True
                timeDeSaida = datetime.datetime.utcnow()
                timeTotal = timeDeSaida - timeDeEntrada
                if (timeTotal.total_seconds() >= 900):
                    loopOfWhile = False
                print(retorno)
                retorno = []
                newY = y
                confirmMap()
            return True
        except:
            print("Erro na func: findShipByTheRegion")
    return False

def clickInTheXOfShipsLoop():
    while procurarImagemSemRetornarErro("processing"):
        time.sleep(1)
        print("Esperando carregamento!")
    x = procurarImagemSemRetornarErro("xShips")
    while x:
        clickInTheXOfShips()
        x = procurarImagemSemRetornarErro("xShips")

def maxAmmo():
    confirmMap()
    time.sleep(5)
    if procurarImagemSemRetornarErro("setaDeEscolha"):
        pyautogui.click(procurarLocalizacaoDaImagemPelosEixos("setaDeEscolha"), duration = durationChoosed())
    if procurarImagemSemRetornarErro("maxAmmo"):
        pyautogui.click(procurarLocalizacaoDaImagemPelosEixos("maxAmmo"), duration = durationChoosed())

def start():
    for i in range(4):
        maxAmmo()
        fight()
        fightBoss()
        confirmLose()
        findShipByTheRegion()
        backToMenu()
        clickInTheXOfShipsLoop()
    time.sleep(1200)

conectarFuncBool = True
time.sleep(2)
while True:
    # try:
        if conectarFuncBool == True :
            conectarFunc()
            conectarFuncBool = False
        start()

    # except BaseException as err:
    #     print("Ocorreu um ERRO: " + str(err))
    #     conectarFuncBool = True