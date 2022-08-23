from tkinter import *
import tkinter.font as tkfont
from tkinter import messagebox
from tkinter import ttk
import PyHook3
import pyautogui

cliques = []
posicao_mouse = []
dicionario_eventos = {}

def OnMouseEvent(event):
    global posicao,x,y,cliques
    if parar():
        nome = event.MessageName
        posicao = event.Position
        mouse = nome
        x = int(posicao[0])
        y = int(posicao[1])
        
        ### FUNÇÃO DE CLIQUE COM O BOTÃO ESQUERDO ###
        if mouse=='mouse left down':
            cliques.append('mouse left down')
        if mouse=='mouse left up':
            cliques.append('mouse left up')
            
        if 'mouse left down' in cliques and 'mouse left up' in cliques:
            dicionario_eventos['LB'] = posicao
            posicao_mouse.append(x)
            posicao_mouse.append(y)
            cliques.clear()
            print(dicionario_eventos)
            posicao_mouse.clear()
        
        
        ### FUNÇÃO DE CLIQUE COM O BOTÃO DIREITO ###
        if mouse=='mouse right down':
            cliques.append('mouse right down')
        if mouse=='mouse right up':
            cliques.append('mouse right up')
            
        if 'mouse right down' in cliques and 'mouse right up' in cliques:
            dicionario_eventos['RB'] = posicao
            posicao_mouse.append(x)
            posicao_mouse.append(y)
            cliques.clear()
            print(dicionario_eventos)
            posicao_mouse.clear()
            
        for chaves in dicionario_eventos:
            valor = dicionario_eventos[chaves]
            if dicionario_eventos[chaves]=='LB':
                x = int(valor[0])
                y = int(valor[1])
        
        return True

    else:
        return False

def mensagems():
    hm = PyHook3.HookManager()
    hm.MouseAll = OnMouseEvent
    hm.HookMouse()
    
    if __name__ == '__main__':
        import pythoncom
        pythoncom.PumpMessages()

def fazerpyautogui():
    pyautogui.click(x=x,y=y)
    
def parar():
    return True

janela = Tk()
janela.title(' ')
janela.geometry('310x300+700+390')
janela.configure(background='white')
janela.resizable(width=FALSE,height=FALSE)


botao_iniciar_gravacao= Button(janela, text='GRAVAR',command=mensagems,relief='flat',bg='black',fg='white',width=15)
botao_iniciar_gravacao.grid()

botao_fazer = Button(janela, text='FAZER',command=fazerpyautogui,relief='flat',bg='black',fg='white',width=15)
botao_fazer.grid()

botao_parar = Button(janela, text='PARAR',command=parar,relief='flat',bg='black',fg='white',width=15)
botao_parar.grid()

janela.mainloop()