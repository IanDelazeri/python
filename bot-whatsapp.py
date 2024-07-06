import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
from time import strftime
import pyautogui

webbrowser.open('https://web.whatsapp.com/')
sleep(30)
#Ler planilha e guardar informações sobre nome, telefone e data 

workbook = openpyxl.load_workbook('cliente.xlsx')
pagina_cliente = workbook['Planilha1']

for linha in pagina_cliente.iter_rows(min_row=2):
    #nome, telefone, data
    nome = linha[0].value
    telefone = linha[1].value
    vencimento = linha[2].value
    print('nome: {}'.format(nome) )
    print('telefone: {}'.format(telefone))
    print('vencimendo: {}'.format(vencimento))
    
    mensagem = f" olá {nome} seu boleto vence dia {vencimento.strftime('%d/%m/%y')} Favor pagar no link https://www.youtube.com"
    link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
    webbrowser.open(link_mensagem_whatsapp)
    sleep(3)

    seta = pyautogui.locateCenterOnScreen('seta.png')
    sleep(3)
    pyautogui.click(seta[0],seta[1])
    sleep(3)
    pyautogui.hotkey('ctrl','w')
    sleep(3)
    




