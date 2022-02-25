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

    if imagem == 'allBlack':
        confidence = 0.95
    elif imagem == "15de15" or imagem == "close":
        confidence = 0.9
    elif imagem == "connectWallet" or imagem == "play":
        confidence = 0.8

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
            if imagem == "connectWallet" or "play":
                confidence = 0.8
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
    contadorDeImg = 0
    while loop:
        if procurarImagemSemRetornarErro("close"):
            raise Exception("Erro na função clickInTheXOfShips")
        if not procurarImagemSemRetornarErro("15de15"):
            # try:
                img = pyautogui.locateCenterOnScreen('./assets/energy.png', confidence=0.9)
                if img != None:
                    x, y = img
                    # x2, y2 = pyautogui.locateCenterOnScreen('./assets/fight.png', confidence=0.9)
                    if x != None:
                        pyautogui.click(x+160, y+50, duration = durationChoosed())
                        time.sleep(1)
                    contadorDeImg += 1
                    if contadorDeImg >= 20 :
                        dragInTheMenu1x()
                        contadorDeImg = 0
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
    if procurarImagemSemRetornarErro("close"):
        raise Exception("Erro na função clickInTheXOfShips")
    time.sleep(1)
    if procurarImagemSemRetornarErro("confirmDentroDoJogo"):
        x, y = procurarLocalizacaoDaImagemPelosEixos("confirmDentroDoJogo")
        if x != None:
            pyautogui.click(x, y, duration = durationChoosed())
    elif procurarImagemSemRetornarErro("confirmLose"):
        x, y = procurarLocalizacaoDaImagemPelosEixos("confirmLose")
        if x != None:
            pyautogui.click(x, y+370, duration = durationChoosed()) 

def backToMenu(): 
    if procurarImagemSemRetornarErro("close"):
        raise Exception("Erro na função clickInTheXOfShips")
    print('*'+('-' * 10)+'backToMenu - INICIO'+('-' * 10)+ '*')  
    time.sleep(5)
    for i in range(3):
        if procurarImagemSemRetornarErro("ship"):
            confirmMap()
            x, y = procurarLocalizacaoDaImagemPelosEixos("ship")
            if x != None:
                pyautogui.click(x, y, duration = durationChoosed())
    print('*'+('-' * 10)+'backToMenu - FIM'+('-' * 10)+ '*')  

# 100%
def clickInTheXOfShips():
    if procurarImagemSemRetornarErro("close"):
        raise Exception("Erro na função clickInTheXOfShips")
    confirmMap()
    if procurarImagemSemRetornarErro("xShips"):
        pyautogui.click(procurarLocalizacaoDaImagemPelosEixos("xShips"), duration = durationChoosed())

# 100%
def findShipByTheRegion():
    contador = 0
    contadorLoop = 0
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
                if procurarImagemSemRetornarErro("close"):
                    raise Exception("Erro na função findShipByTheRegion - loopOfWhile")
                print('*'+('-' * 10)+'findShipByTheRegion --loopOfWhile-- INICIO'+('-' * 10)+ '*')
                for i in range(5):
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
                if not procurarImagemSemRetornarErro('allBlack'):
                    loopOfWhile = False
                elif retorno.count(True) >= 3:
                    time.sleep(1)
                    contadorLoop += 1
                    print("TESTE COUNT TRUE ---------------------------")
                    if contadorLoop > 50 :
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
    if procurarImagemSemRetornarErro("close"):
        raise Exception("Erro na função clickInTheXOfShipsLoop")
    time.sleep(2)
    while procurarImagemSemRetornarErro("processing"):
        time.sleep(1)
        print("Esperando carregamento!")
    time.sleep(2)
    x = procurarImagemSemRetornarErro("xShips")
    while x:
        if not procurarImagemSemRetornarErro("15de15"):
            clickInTheXOfShips()
            x = procurarImagemSemRetornarErro("xShips")
        else:
            x = False

def maxAmmo():
    confirmMap()
    contador = 0
    setaDeEscolha = False
    while setaDeEscolha == False:
        if procurarImagemSemRetornarErro("close"):
            raise Exception("Erro na função maxAmmo")
        time.sleep(1)
        setaDeEscolha = procurarImagemSemRetornarErro("setaDeEscolha")
        if setaDeEscolha:
            pyautogui.click(procurarLocalizacaoDaImagemPelosEixos("setaDeEscolha"), duration = durationChoosed())
            time.sleep(2)
            if procurarImagemSemRetornarErro("maxAmmo"):
                pyautogui.click(procurarLocalizacaoDaImagemPelosEixos("maxAmmo"), duration = durationChoosed())
                setaDeEscolha = True
        else:
            if procurarImagemSemRetornarErro("connectWallet"):
                pyautogui.click(procurarLocalizacaoDaImagemPelosEixos("close"), duration = durationChoosed())
            if contador >= 30:
                setaDeEscolha = True
                print("-- ENTRANDO EM CONTADOR NA FUNÇÃO, ANTES DE LANÇAR EXCEÇÃO: maxAmmo()")
                raise Exception("Erro na função maxAmmo")
            contador += 1

def openTheSPG():
    time.sleep(15)
    site_on = os.getenv("SITE_ON")
    x, y = procurarLocalizacaoDaImagemPelosEixos("metamaskWhitOutNotification")
    pyautogui.click(x-500, y, duration=15)
    time.sleep(15)
    pyautogui.keyDown("ctrl")
    pyautogui.press("a")
    pyautogui.keyUp("ctrl")
    time.sleep(15)
    pyautogui.write(site_on)
    pyautogui.press("enter")

def start():
    fightFinish = True
    while fightFinish:
        print("-- ENTRANDO EM FUNÇÃO - main: clickInTheXOfShipsLoop()")
        clickInTheXOfShipsLoop()
        print("-- ENTRANDO EM FUNÇÃO - main: maxAmmo()")
        maxAmmo()
        print("-- ENTRANDO EM FUNÇÃO - main: fightFinish()")
        fightFinish = fight()
        print("-- ENTRANDO EM FUNÇÃO - main: fightBoss()")
        fightBoss()
        print("-- ENTRANDO EM FUNÇÃO - main: confirmMap()")
        confirmMap()
        print("-- ENTRANDO EM FUNÇÃO - main: findShipByTheRegion()")
        findShipByTheRegion()
        print("-- ENTRANDO EM FUNÇÃO - main: backToMenu()")
        backToMenu()
        if procurarImagemSemRetornarErro("ship"):
            confirmMap()
            backToMenu()
    pyautogui.click(procurarLocalizacaoDaImagemPelosEixos("spaceCrypto"), duration = 2)
    time.sleep(2)
    reiniciarAPagina()
    for i in range(14600):
        moveRange = round(random.uniform(100,700), 10)
        moveRange2 = round(random.uniform(100,700), 10)
        pyautogui.moveTo(moveRange, moveRange2, duration = 1)        

# conectarFuncBool = True
time.sleep(2)
while True:
    try:
        conectarFunc()
        start()
    except BaseException as err:
        print("Ocorreu um ERRO: " + str(err))