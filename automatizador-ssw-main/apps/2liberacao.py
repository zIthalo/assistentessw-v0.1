import pyautogui
import time
import keyboard
import tkinter as tk
from datetime import datetime
from tkinter import simpledialog

data_atual = datetime.now().strftime("%d%m%Y")

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
    time.sleep(.5)
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

def vinte():
    destino = pyautogui.prompt(text='Qual é a unidade de destino?', title='Entrada de Dados', default='1')
    pyautogui.click(x=209, y=133)
    pyautogui.write(destino)
    cavalo = pyautogui.prompt(text='Qual é a placa do cavalo?', title='Entrada de Dados', default='1')
    pyautogui.click(x=239, y=169)
    pyautogui.write(cavalo)
    carreta = pyautogui.prompt(text='Qual é a placa da carreta?', title='Entrada de Dados', default='1')
    pyautogui.click(x=211, y=200)
    pyautogui.write(carreta)
    conferente = pyautogui.prompt(text='Quem é o conferente?', title='Entrada de Dados', default='1')
    pyautogui.click(x=237, y=403)
    pyautogui.write(conferente)
    lacre = pyautogui.prompt(text='Digite o lacre.', title='Entrada de Dados', default='1')
    pyautogui.click(x=222, y=426)
    pyautogui.write(lacre)


def abrir_caixa_de_dialogo():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    comando = simpledialog.askstring("Entrada", "Digite um comando:")

    if comando == "sub" or comando == "SUB":
        sub()
    if comando == "20":
        vinte()

keyboard.add_hotkey('alt+-', abrir_caixa_de_dialogo)

print("Aguardando atalhos: ")
keyboard.wait()  # Aguarda o programa continuar rodando