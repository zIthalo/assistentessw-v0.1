import pyautogui
import time
import keyboard
import tkinter as tk
from datetime import datetime
from tkinter import simpledialog

data_atual = datetime.now().strftime("%d%m%Y")

def ag():
    pyautogui.click(x=224, y=375, clicks=3)
    pyautogui.write("***AGENDAR ENTREGA***")

def lc():
    pyautogui.click(x=216, y=456, clicks=3)
    pyautogui.write('LOCAL DE ENTREGA')
    pyautogui.press('enter')

def interior():
    pyautogui.click(x=205, y=314, clicks=3)
    pyautogui.write('093')

def cem():
    pyautogui.click(x=205, y=314, clicks=3)
    pyautogui.write('100')

def log():
    pyautogui.click(x=648, y=130)
    # pyautogui.write('12092097482')
    pyautogui.write('ithalo')
    pyautogui.press('enter')
    pyautogui.write('Mor2016.')
    pyautogui.press('enter')

def cub():
    pyautogui.click(x=549, y=328, clicks=2)

    
def ven():
    pyautogui.click(x=520, y=167)
    pyautogui.write('13631538000812')
    # pyautogui.press('+')
    # pyautogui.press('enter')

def tec():
    pyautogui.click(x=520, y=167)
    pyautogui.write('08640510000992')
    # pyautogui.press('+')
    # pyautogui.press('enter')

def mor():
    pyautogui.click(x=520, y=167)
    pyautogui.write('22161801000333')
    # pyautogui.press('+')
    # pyautogui.press('enter')

def sub():
    pyautogui.click(x=292, y=102, clicks=2)
    pyautogui.write('72090442000187')
    pyautogui.press('enter')
    pyautogui.write('BLU')
    pyautogui.press('enter')
    pyautogui.write(data_atual)
    pyautogui.press('enter')
    pyautogui.write(',01')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.write('11')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.write('ARMAZEM')
    pyautogui.write('2')
    pyautogui.write('72090442000934')
    pyautogui.write('72090442000934')
    time.sleep(1.5)
    pyautogui.press('enter')
    time.sleep(.5)
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.write('1')
    pyautogui.press('enter')
    pyautogui.write(data_atual)
    pyautogui.press('enter')
    pyautogui.write(',0001')
    pyautogui.press('enter')
    # Pergunta ao usuário a quantidade de volumes
    vl = pyautogui.prompt(text='Quantos volumes?', title='Entrada de Dados', default='1')
    pyautogui.write(vl)
    pyautogui.press('enter')
    pyautogui.write(',001')
    pyautogui.press('enter')
    pyautogui.write(',01')
    pyautogui.press('enter')
    pyautogui.write('SEGUE ' + vl + ' PALLETS')
    pyautogui.click(x=168, y=459)


def abrir_caixa_de_dialogo():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    comando = simpledialog.askstring("Entrada", "Digite um comando:")

    if comando == "ag":
        ag()
    elif comando == "lc":
        lc()
    elif comando == "in":
        interior()
    elif comando == "log":
        log()
    elif comando == "cem":
        cem()
    elif comando == "cub":
        cub()
    elif comando == "ven":
        ven()
    elif comando == "tec":
        tec()
    elif comando == "mor":
        mor()
    elif comando == "sub":
        sub()
    else:
        print("Comando não reconhecido!")

# Associa o comando 'alt+D' para abrir a caixa de diálogo
keyboard.add_hotkey('alt+-', abrir_caixa_de_dialogo)

# keyboard.add_hotkey('alt+1', interior())


print("Aguardando atalhos: ")
keyboard.wait()  # Aguarda o programa continuar rodando