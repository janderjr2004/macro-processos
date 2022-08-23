from tkinter import *
from tkinter import font
from tkinter import messagebox
import win32gui
import win32con
import win32api
from PIL import Image, ImageTk
import mysql.connector

import sys
 
 
janela = Tk()
janela.title(' ')
janela.geometry('350x400')
janela.configure(background='white')
janela.resizable(width=FALSE,height=FALSE)
janela.iconbitmap('Papirus-Team-Papirus-Apps-Python.ico')

def sumircomplaceholder_senha_cadastro(event):
    global cor,input_senha_placeholder_cadastro
    if len(input_senha_placeholder_cadastro.get())==0 or input_senha_placeholder_cadastro.get()=='Password':
        input_senha_placeholder_cadastro.delete(0,'end')
        cor = 'black'
        input_senha_placeholder_cadastro.configure(show='*')
        input_senha_placeholder_cadastro.configure(fg=cor)
    
def voltarcomplaceholder_senha_cadastro(event):
    global cor,input_senha_placeholder_cadastro
    if len(input_senha_placeholder_cadastro.get())==0:
        input_senha_placeholder_cadastro.delete(0,'end')
        input_senha_placeholder_cadastro.insert(0,'Password')
        cor = '#DCDCDC'
        input_senha_placeholder_cadastro.configure(fg=cor)
        input_senha_placeholder_cadastro.configure(show='')
    else:
        pass


def sumircomplaceholder_user_cadastro(event):
    global cor,input_user_placeholder_cadastro
    if len(input_user_placeholder_cadastro.get())==0 or input_user_placeholder_cadastro.get()=='User':
        input_user_placeholder_cadastro.delete(0,'end')
        cor = 'black'
        input_user_placeholder_cadastro.configure(fg=cor)
    
def voltarcomplaceholder_user_cadastro(event):
    global cor,input_user_placeholder_cadastro
    if len(input_user_placeholder_cadastro.get())==0:
        input_user_placeholder_cadastro.delete(0,'end')
        input_user_placeholder_cadastro.insert(0,'User')
        cor = '#DCDCDC'
        input_user_placeholder_cadastro.configure(fg=cor)
    else:
        pass
    

def sumircomplaceholder_email_cadastro(event):
    global cor,input_email_placeholder_cadastro
    if len(input_email_placeholder_cadastro.get())==0 or input_email_placeholder_cadastro.get()=='E-mail':
        input_email_placeholder_cadastro.delete(0,'end')
        cor = 'black'
        input_email_placeholder_cadastro.configure(fg=cor)
    
def voltarcomplaceholder_email_cadastro(event):
    global cor,input_email_placeholder_cadastro
    if len(input_email_placeholder_cadastro.get())==0:
        input_email_placeholder_cadastro.delete(0,'end')
        input_email_placeholder_cadastro.insert(0,'E-mail')
        cor = '#DCDCDC'
        input_email_placeholder_cadastro.configure(fg=cor)
    else:
        pass

def versenha():
    input_senha_placeholder_cadastro.configure(show='')
    botao_ver.configure(command=naoversenha)
def naoversenha():
    input_senha_placeholder_cadastro.configure(show='*')
    botao_ver.configure(command=versenha)

cor = '#DCDCDC'

imagem = Label(janela,bg='white')
amostra1 = ImageTk.PhotoImage(Image.open("python-icon.png"))
imagem['image'] = amostra1
imagem.place(x=120,y=50)

input_user_placeholder_cadastro = Entry(janela, width=25,fg=cor, justify='left',font=('Bahnschrift',11), highlightthickness=0, relief='flat')
input_user_placeholder_cadastro.place(x=50,y=190,width=230,height=30)
input_user_placeholder_cadastro.insert(0,'User')
input_user_placeholder_cadastro.bind('<FocusIn>',sumircomplaceholder_user_cadastro)
input_user_placeholder_cadastro.bind('<FocusOut>',voltarcomplaceholder_user_cadastro)

linha = Frame(janela,width=250,height=2,bg='#1E90FF')
linha.place(x=50,y=216)


input_email_placeholder_cadastro = Entry(janela, width=25,fg=cor, justify='left',font=('Bahnschrift',11), highlightthickness=0, relief='flat')
input_email_placeholder_cadastro.place(x=50,y=240,width=230,height=30)
input_email_placeholder_cadastro.insert(0,'E-mail')
input_email_placeholder_cadastro.bind('<FocusIn>',sumircomplaceholder_email_cadastro)
input_email_placeholder_cadastro.bind('<FocusOut>',voltarcomplaceholder_email_cadastro)

linha = Frame(janela,width=250,height=2,bg='#1E90FF')
linha.place(x=50,y=266)



input_senha_placeholder_cadastro = Entry(janela, width=25,fg=cor, justify='left',font=('Bahnschrift',11), highlightthickness=0, relief='flat')
input_senha_placeholder_cadastro.place(x=50,y=290,width=230,height=30)
input_senha_placeholder_cadastro.insert(0,'Password')
input_senha_placeholder_cadastro.bind('<FocusIn>',sumircomplaceholder_senha_cadastro)
input_senha_placeholder_cadastro.bind('<FocusOut>',voltarcomplaceholder_senha_cadastro)

linha = Frame(janela,width=250,height=2,bg='#1E90FF')
linha.place(x=50,y=316)


imagem_olho = Label(janela,bg='white')
amostra = ImageTk.PhotoImage(Image.open("olho.png"))
imagem_olho['image'] = amostra
imagem_olho.place(x=268,y=290,height=25)

botao_ver = Button(janela,image=amostra,command=versenha,border=0,bg='white',fg='white',font=('Bahnschrift',11))
botao_ver.place(x=268,y=295,height=18)


botao_entrar = Button(janela, text='Cadastrar',border=0,bg='#fec750',fg='white',width=28,font=('Bahnschrift',11))
botao_entrar.place(x=60,y=340)

janela.mainloop()