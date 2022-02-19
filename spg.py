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
    print('*'+('-' * 25)+'conectarFunc-INICIO'+('-' * 25)+ '*')
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
        if procurarImagemSemRetornarErro("close"):
            contador = 0
            connect = True
            assinarClick = False
            playClick = False
            connectWallet = False
            reiniciarAPagina()
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
    print('*'+('-' * 25)+'conectarFunc-FIM'+('-' * 25)+ '*')

def dragInTheMenu1x():
    if not procurarImagemSemRetornarErro("connectWallet") and not procurarImagemSemRetornarErro("close"):
        x, y = procurarLocalizacaoDaImagemPelosEixos("setaDeEscolha")
        pyautogui.moveTo(x, y+440)
        pyautogui.mouseDown(button='left')
        #BEM MELHOR usar moveTo no lugar de dragTO
        pyautogui.moveTo(x, y+40, duration=3)
        # pyautogui.dragTo(x, y+40, duration = 3)
        time.sleep(4)
        pyautogui.mouseUp(button='left')
        time.sleep(2)
    else:
        raise Exception("Erro na função dragInTheMenu1x")

def procurarImagemSemRetornarErro(imagem):
    confidence = os.getenv("CONFIDENCE")
    if imagem == "15de15":
        confidence = 0.9
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
    return False

def procurarLocalizacaoDaImagemPelosEixos(imagem):
    print('Utiliando a func procurarLocalizacaoDaImagemPelosEixos: ' + imagem)
    contador = 0
    while contador < 35:
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
                print("ERRO - FUNÇÃO: procurarLocalizacaoDaImagemPelosEixos - Nao achei a imagem: "+imagem+' - '+ str(contador))         
        else:
             contador += 1
    return None, None


#### ERRO SÓ DAQUI PRA BAIXO ####

# Procura pela região em torno do botão fight se essa nave deve ou não ir batalhar
def fight():
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
                        return False
            # except:
            #     print("Erro na func fight, ao procurar imagem: FIGHT")   
        else:
            loop = False
    return True
    
# 100%
def fightBoss():
    time.sleep(2)
    confirmMap()
    if procurarImagemSemRetornarErro("fightBoss"):
        pyautogui.click(procurarLocalizacaoDaImagemPelosEixos("fightBoss"), duration = durationChoosed())

# 100%
def confirmMap():
    time.sleep(1)
    if procurarImagemSemRetornarErro("confirmDentroDoJogo"):
        x, y = procurarLocalizacaoDaImagemPelosEixos("confirmDentroDoJogo")
        if x != None:
            pyautogui.click(x, y, duration = durationChoosed())
    elif procurarImagemSemRetornarErro("confirmLose"):
        x, y = procurarLocalizacaoDaImagemPelosEixos("confirmLose")
        if x != None:
            pyautogui.click(x, y, duration = durationChoosed()) 

def backToMenu(): 
    print('*'+('-' * 10)+'backToMenu - INICIO'+('-' * 10)+ '*')  
    time.sleep(5)
    confirmMap()
    for i in range(3):
        if procurarImagemSemRetornarErro("ship"):
            x, y = procurarLocalizacaoDaImagemPelosEixos("ship")
            if x != None:
                pyautogui.click(x, y, duration = durationChoosed())
    print('*'+('-' * 10)+'backToMenu - FIM'+('-' * 10)+ '*')  

# 100%
def clickInTheXOfShips():
    confirmMap()
    if procurarImagemSemRetornarErro("xShips"):
        pyautogui.click(procurarLocalizacaoDaImagemPelosEixos("xShips"), duration = durationChoosed())

# 100%
def findShipByTheRegion():
    contador = 0
    time.sleep(3)
    loopSurrender = procurarImagemSemRetornarErro("surrenderInTheGame")
    while not loopSurrender:
        confirmMap()
        contador += 1
        loopSurrender = procurarImagemSemRetornarErro("surrenderInTheGame")
        if contador == 20:
            loopSurrender = True

    if procurarImagemSemRetornarErro("surrenderInTheGame"):
        try:
            x, y = pyautogui.locateCenterOnScreen('./assets/surrenderInTheGame.png', confidence=0.9)
            variacaoDoY = 57
            newY = y
            retorno = []
            loopOfWhile = True
            timeDeEntrada = datetime.datetime.utcnow()
            timeDeSaida = datetime.datetime.utcnow()
            while loopOfWhile:
                print('*'+('-' * 10)+'findShipByTheRegion --loopOfWhile-- INICIO'+('-' * 10)+ '*')
                for i in range(6):
                    img = pyautogui.locateCenterOnScreen('./assets/xVermelhoEmCimaDaNave.png', confidence=0.9, region=(x-30,(newY+49+variacaoDoY), 56, 60) )
                    newY+= 57  
                    if img == None:  
                        retorno.append(False)
                    else:
                        retorno.append(True)
                loopOfWhile = False
                for i in retorno:
                    if i == False:
                        loopOfWhile = True
                    elif procurarImagemSemRetornarErro("allBlack"):
                        print("Não existe nave na tela! - allBlack")
                        loopOfWhile = False
                timeDeSaida = datetime.datetime.utcnow()
                timeTotal = timeDeSaida - timeDeEntrada
                if (timeTotal.total_seconds() >= 900):
                    loopOfWhile = False
                print(retorno)
                retorno = []
                newY = y
                confirmMap()
                print('*'+('-' * 10)+'findShipByTheRegion --loopOfWhile-- FIM'+('-' * 10)+ '*')
            return True
        except BaseException as err:
            print("Ocorreu um ERRO na função - findShipByTheRegion: " + str(err))
    return False

def clickInTheXOfShipsLoop():
    time.sleep(2)
    while procurarImagemSemRetornarErro("processing"):
        time.sleep(1)
        print("Esperando carregamento!")
    time.sleep(2)
    x = procurarImagemSemRetornarErro("xShips")
    while x:
        clickInTheXOfShips()
        x = procurarImagemSemRetornarErro("xShips")

def maxAmmo():
    confirmMap()
    contador = 0
    setaDeEscolha = False
    while setaDeEscolha == False:
        time.sleep(1)
        setaDeEscolha = procurarImagemSemRetornarErro("setaDeEscolha")
        if setaDeEscolha and not procurarImagemSemRetornarErro("connectWallet") and not procurarImagemSemRetornarErro("close"):
            pyautogui.click(procurarLocalizacaoDaImagemPelosEixos("setaDeEscolha"), duration = durationChoosed())
            time.sleep(2)
            if procurarImagemSemRetornarErro("maxAmmo"):
                pyautogui.click(procurarLocalizacaoDaImagemPelosEixos("maxAmmo"), duration = durationChoosed())
        else:
            contador += 1
            if contador == 30:
                raise Exception("Erro na função maxAmmo")

def start():
    fightFinish = True
    while fightFinish:
        clickInTheXOfShipsLoop()
        maxAmmo()
        fightFinish = fight()
        fightBoss()
        confirmMap()
        findShipByTheRegion()
        backToMenu()
        if procurarImagemSemRetornarErro("ship"):
            backToMenu()
    for i in range(600):
        moveRange = round(random.uniform(100,700), 10)
        moveRange2 = round(random.uniform(100,700), 10)
        pyautogui.moveTo(moveRange, moveRange2, duration = 2)

# conectarFuncBool = True
time.sleep(2)
while True:
    try:
        
        # if conectarFuncBool == True :
            # conectarFunc()
            # conectarFuncBool = False
        conectarFunc()
        start()

    except BaseException as err:
        print("Ocorreu um ERRO: " + str(err))
        conectarFuncBool = True