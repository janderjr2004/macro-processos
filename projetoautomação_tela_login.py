from tkinter import *
import tkinter.font as tkfont
from tkinter import messagebox
from tkinter import ttk
import PyHook3
import pyautogui
import win32gui
import win32con
import win32api
from PIL import Image, ImageTk
import mysql.connector

janela = Tk()
janela.title(' ')
janela.geometry('850x500')
janela.configure(background='white')
janela.resizable(width=FALSE,height=FALSE)
janela.iconbitmap('./imgs/Papirus-Team-Papirus-Apps-Python.ico')

cor = '#DCDCDC'


############ LOGIN,SENHA,E DATABASE DO BANCO DE DADOS ###############
global user_bdd,senha_bdd,database_bdd
arq = open("bdd.txt")
linhas = arq.readlines()
user_bdd = linhas[0][0:4]
senha_bdd = linhas[1][0:9]
database_bdd = linhas[2]
print(len(user_bdd),user_bdd)
print(len(senha_bdd),senha_bdd)
print(len(database_bdd),database_bdd)

############## FIM DAS VARIÁVEIS #####################


############## CONECTAR BANCO DE DADOS #################

def conectarBDD():
    global con
    con = mysql.connector.connect(host='localhost',database=database_bdd,user=user_bdd,password=senha_bdd)
    
################ FIM DA CONEXÃO ######################


################ LOGIN NO APP ########################

def LoginAPP():
    conectarBDD()
    if con.is_connected():
        try:
            cursor = con.cursor()
            comando_sql = "SELECT user,senha FROM users WHERE user=%s AND senha=%s;"
            dados = (str(input_user_placeholder.get()),str(input_senha_placeholder.get()))
            cursor.execute(comando_sql,dados)
            sql_login = cursor.fetchall()

            if sql_login[0][0]==input_user_placeholder.get() and sql_login[0][1]==input_senha_placeholder.get():
                messagebox.showinfo('','LOGADO COM SUCESSO!')
        except:
            messagebox.showerror('','USUÁRIO OU SENHA INCORRETOS')


########### PLACEHOLDERS TELA DE LOGIN ####################

def sumircomplaceholder_user(event):
    global cor,input_user_placeholder
    if len(input_user_placeholder.get())==0 or input_user_placeholder.get()=='User':
        input_user_placeholder.delete(0,'end')
        cor = 'black'
        input_user_placeholder.configure(fg=cor)

def voltarcomplaceholder_user(event):
    global cor,input_user_placeholder
    if len(input_user_placeholder.get())==0:
        input_user_placeholder.delete(0,'end')
        input_user_placeholder.insert(0,'User')
        cor = '#DCDCDC'
        input_user_placeholder.configure(fg=cor)
    else:
        pass
    
def sumircomplaceholder_senha(event):
    global cor,input_senha_placeholder
    if len(input_senha_placeholder.get())==0 or input_senha_placeholder.get()=='Password':
        input_senha_placeholder.delete(0,'end')
        cor = 'black'
        input_senha_placeholder.configure(show='*')
        input_senha_placeholder.configure(fg=cor)
    
def voltarcomplaceholder_senha(event):
    global cor,input_senha_placeholder
    if len(input_senha_placeholder.get())==0:
        input_senha_placeholder.delete(0,'end')
        input_senha_placeholder.insert(0,'Password')
        cor = '#DCDCDC'
        input_senha_placeholder.configure(fg=cor)
        input_senha_placeholder.configure(show='')
    else:
        pass
    
########### FIM PLACEHOLDERS TELA DE LOGIN ################   

########### TELA DE CADASTRO #################

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
    global imagem_olho_nao
    input_senha_placeholder_cadastro.configure(show='')
    imagem_olho_nao = ImageTk.PhotoImage(Image.open("./imgs/olhonao.png"))
    botao_ver.configure(image=amostra2_login)
    botao_ver.bind('<Enter>',botao_naover_cadastro_hover)
    botao_ver.bind('<Leave>',botao_naover_cadastro_hover_sair)
    
    botao_ver.configure(command=naoversenha)
def naoversenha():
    input_senha_placeholder_cadastro.configure(show='*')
    botao_ver.bind('<Enter>',botao_ver_cadastro_hover)
    botao_ver.bind('<Leave>',botao_ver_cadastro_hover_sair)
    botao_ver.configure(image=amostra2_login)
    botao_ver.configure(command=versenha)
    
    
def botao_ver_cadastro_hover(event):
    botao_ver.configure(image=olho_preto_ver)
    botao_ver.place(x=268,y=294,height=18)
def botao_ver_cadastro_hover_sair(event):
    botao_ver.configure(image=amostra2_login)
    botao_ver.place(x=268,y=295,height=18)
    
    
def botao_naover_cadastro_hover(event):
    botao_ver.configure(image=olho_preto)
    botao_ver.place(x=268,y=294,height=18)
def botao_naover_cadastro_hover_sair(event):
    botao_ver.configure(image=imagem_olho_nao)
    botao_ver.place(x=268,y=295,height=18)


    

    
def botao_cadastrar_hover(event):
    botao_cadastrar.configure(bg='#F0BB4A')
def botao_cadastrar_hover_sair(event):
    botao_cadastrar.configure(bg='#fec750')

def TelaDeCadastro():
    global janela_cadastro,imagem_olho,imagem_cadastro,amostra2,amostra1,botao_ver,input_user_placeholder_cadastro,input_email_placeholder_cadastro,input_senha_placeholder_cadastro,botao_cadastrar
    janela_cadastro = Toplevel()
    janela_cadastro.title(' ')
    janela_cadastro.geometry('350x400')
    janela_cadastro.configure(background='white')
    janela_cadastro.resizable(width=FALSE,height=FALSE)
    janela_cadastro.iconbitmap('./imgs/Papirus-Team-Papirus-Apps-Python.ico')

    
    cor = '#DCDCDC'

    imagem_cadastro = Label(janela_cadastro,bg='white')
    amostra1 = ImageTk.PhotoImage(Image.open("./imgs/python-icon.png"))
    imagem_cadastro['image'] = amostra1
    imagem_cadastro.place(x=120,y=50)

    input_user_placeholder_cadastro = Entry(janela_cadastro, width=25,fg=cor, justify='left',font=('Bahnschrift',11), highlightthickness=0, relief='flat')
    input_user_placeholder_cadastro.place(x=50,y=190,width=230,height=30)
    input_user_placeholder_cadastro.insert(0,'User')
    input_user_placeholder_cadastro.bind('<FocusIn>',sumircomplaceholder_user_cadastro)
    input_user_placeholder_cadastro.bind('<FocusOut>',voltarcomplaceholder_user_cadastro)

    linha = Frame(janela_cadastro,width=250,height=2,bg='#1E90FF')
    linha.place(x=50,y=216)


    input_email_placeholder_cadastro = Entry(janela_cadastro, width=25,fg=cor, justify='left',font=('Bahnschrift',11), highlightthickness=0, relief='flat')
    input_email_placeholder_cadastro.place(x=50,y=240,width=230,height=30)
    input_email_placeholder_cadastro.insert(0,'E-mail')
    input_email_placeholder_cadastro.bind('<FocusIn>',sumircomplaceholder_email_cadastro)
    input_email_placeholder_cadastro.bind('<FocusOut>',voltarcomplaceholder_email_cadastro)

    linha = Frame(janela_cadastro,width=250,height=2,bg='#1E90FF')
    linha.place(x=50,y=266)



    input_senha_placeholder_cadastro = Entry(janela_cadastro, width=25,fg=cor, justify='left',font=('Bahnschrift',11), highlightthickness=0, relief='flat')
    input_senha_placeholder_cadastro.place(x=50,y=290,width=230,height=30)
    input_senha_placeholder_cadastro.insert(0,'Password')
    input_senha_placeholder_cadastro.bind('<FocusIn>',sumircomplaceholder_senha_cadastro)
    input_senha_placeholder_cadastro.bind('<FocusOut>',voltarcomplaceholder_senha_cadastro)

    linha = Frame(janela_cadastro,width=250,height=2,bg='#1E90FF')
    linha.place(x=50,y=316)


    imagem_olho = Label(janela_cadastro,bg='white')
    amostra2 = ImageTk.PhotoImage(Image.open("./imgs/olho.png"))
    imagem_olho['image'] = amostra2
    imagem_olho.place(x=268,y=290,height=25)

    botao_ver = Button(janela_cadastro,activebackground='white',cursor='hand2',relief='sunken',image=amostra2,borderwidth=0,command=versenha,border=0,bg='white',fg='white',font=('Bahnschrift',11))
    botao_ver.place(x=268,y=295,height=18)
    botao_ver.bind('<Enter>',botao_ver_cadastro_hover)
    botao_ver.bind('<Leave>',botao_ver_cadastro_hover_sair)

    botao_cadastrar = Button(janela_cadastro,command=CadastraBDD,cursor='hand2', text='Cadastrar',border=0,bg='#fec750',fg='white',width=28,font=('Bahnschrift',11))
    botao_cadastrar.place(x=60,y=340)
    botao_cadastrar.bind('<Enter>', botao_cadastrar_hover)
    botao_cadastrar.bind('<Leave>', botao_cadastrar_hover_sair)
    
def CadastraBDD():
    conectarBDD()
    if con.is_connected():
        try:
            cursor = con.cursor()
            comando_sql = "INSERT INTO users(user,email,senha) VALUES(%s,%s,%s)"
            dados = (str(input_user_placeholder_cadastro.get()),str(input_senha_placeholder_cadastro.get()),str(input_email_placeholder_cadastro.get()))
            cursor.execute(comando_sql,dados)
            con.commit()
            messagebox.showinfo('','CADASTRO REALIZADO COM SUCESSO')
        except:
            messagebox.showerror('','USUÁRIO JÁ CADASTRADO')
########### FIM DO CADASTRO DE USUARIOS  #############

################### FRAME 1 ########################
C = Canvas(janela, bg ="white", 
           height = 250, width = 300,highlightthickness=0)

hwnd = C.winfo_id()
colorkey = win32api.RGB(255,255,255) #full black in COLORREF structure
wnd_exstyle = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
new_exstyle = wnd_exstyle | win32con.WS_EX_LAYERED
win32gui.SetWindowLong(hwnd,win32con.GWL_EXSTYLE,new_exstyle)
win32gui.SetLayeredWindowAttributes(hwnd,colorkey,255,win32con.LWA_COLORKEY)


frame1 = Frame(janela,width=325,height=500,bg='#1E90FF')
frame1.place(x=0,y=0)

shape2={'bounds': [100, 200, 200, 130, 100, 50], 'kind': 'tri', 'fill': True}
C.create_polygon(list(shape2.values())[0],fill='#1E90FF',outline='#1E90FF')
C.place(x=180,y=110) 

label_titulo_inicial = Label(frame1,text='SISTEMA EM',fg='white',font=('Bahnschrift','13'),bg='#1E90FF')
label_titulo_inicial.place(x=28,y=190)

label_titulo_inicial2 = Label(frame1,text='PYTHON',fg='white',font=('Bahnschrift Bold','28'),bg='#1E90FF')
label_titulo_inicial2.place(x=26,y=215,height=29)

label_titulo_inicial= Label(frame1,text='AUTOMATIZADOR DE PROCESSOS',fg='white',font=('Bahnschrift SemiBold','13'),bg='#1E90FF')
label_titulo_inicial.place(x=27,y=244)

################## FIM DO FRAME 1 ###########################

################## JANELA OU FRAME 2 ########################

def versenha_login():
    global imagem_olho_nao
    input_senha_placeholder.configure(show='')
    imagem_olho_nao = ImageTk.PhotoImage(Image.open("./imgs/olhonao.png"))
    
    botao_ver_login.configure(image=amostra2_login)
    
    
    botao_ver_login.bind('<Enter>',botao_naover_login_hover)
    botao_ver_login.bind('<Leave>',botao_naover_login_hover_sair)
    botao_ver_login.configure(command=naoversenha_login)
    
    
def naoversenha_login():
    input_senha_placeholder.configure(show='*')
    botao_ver_login.bind('<Enter>',botao_ver_login_hover)
    botao_ver_login.bind('<Leave>',botao_ver_login_hover_sair)
    botao_ver_login.configure(image=amostra2_login)
    botao_ver_login.configure(command=versenha_login)


def criar_conta_hover(event):
    criar_conta.configure(fg='#3F76B5')
    criar_conta.place(x=654,y=358)
def criar_conta_hover_sair(event):
    criar_conta.configure(fg='#57a1f8')
    criar_conta.place(x=654,y=359)
    
    
def botao_entrar_hover(event):
    botao_entrar.configure(bg='#F0BB4A')
def botao_entrar_hover_sair(event):
    botao_entrar.configure(bg='#fec750')


def botao_ver_login_hover(event):
    botao_ver_login.configure(image=olho_preto_ver)
    botao_ver_login.place(x=705,y=264,height=18)
def botao_ver_login_hover_sair(event):
    botao_ver_login.configure(image=amostra2_login)
    botao_ver_login.place(x=705,y=265,height=18)
    
    
def botao_naover_login_hover(event):
    botao_ver_login.configure(image=olho_preto)
    botao_ver_login.place(x=705,y=264,height=18)
def botao_naover_login_hover_sair(event):
    botao_ver_login.configure(image=imagem_olho_nao)
    botao_ver_login.place(x=705,y=265,height=18)

imagem = Label(janela,bg='white')
amostra = ImageTk.PhotoImage(Image.open("./imgs/python-icon.png"))
imagem['image'] = amostra
imagem.place(x=560,y=45)


input_user_placeholder = Entry(janela, width=25,fg=cor, justify='left',font=('Bahnschrift',11), highlightthickness=0, relief='flat')
input_user_placeholder.place(x=490,y=210,width=230,height=30)
input_user_placeholder.insert(0,'User')
input_user_placeholder.bind('<FocusIn>',sumircomplaceholder_user)
input_user_placeholder.bind('<FocusOut>',voltarcomplaceholder_user)

linha = Frame(janela,width=250,height=2,bg='#1E90FF')
linha.place(x=485,y=236)


input_senha_placeholder = Entry(janela, width=25,fg=cor, justify='left',font=('Bahnschrift',11), highlightthickness=0, relief='flat')
input_senha_placeholder.place(x=490,y=260,width=230,height=30)
input_senha_placeholder.insert(0,'Password')
input_senha_placeholder.bind('<FocusIn>',sumircomplaceholder_senha)
input_senha_placeholder.bind('<FocusOut>',voltarcomplaceholder_senha)

linha = Frame(janela,width=250,height=2,bg='#1E90FF')
linha.place(x=485,y=286)


amostra2_login = ImageTk.PhotoImage(Image.open("./imgs/olho.png"))
olho_preto = ImageTk.PhotoImage(Image.open("./imgs/olho_preto.png"))
olho_preto_ver = ImageTk.PhotoImage(Image.open("./imgs/olho_preto_ver.png"))


botao_ver_login = Button(janela,activebackground='white',cursor='hand2',relief='sunken',image=amostra2_login,borderwidth=0,command=versenha_login,border=0,bg='white',fg='white',font=('Bahnschrift',11))
botao_ver_login.place(x=705,y=265,height=18)
botao_ver_login.bind('<Enter>',botao_ver_login_hover)
botao_ver_login.bind('<Leave>',botao_ver_login_hover_sair)


botao_entrar = Button(janela, text='Login',cursor='hand2',activebackground='#F0BB4A',relief='sunken',borderwidth=0,command=LoginAPP,border=0,bg='#fec750',fg='white',width=28,font=('Bahnschrift',11))
botao_entrar.place(x=495,y=310)
botao_entrar.bind('<Enter>', botao_entrar_hover)
botao_entrar.bind('<Leave>', botao_entrar_hover_sair)

label_nao_conta = Label(janela, text='Não tem uma conta?', bg='white',fg='#363636',font=('Bahnschrift',10))
label_nao_conta.place(x=530,y=360)

criar_conta = Button(janela,width=4,text='Criar',activebackground='white',relief='sunken',borderwidth=0,command=TelaDeCadastro,border=0,bg='white',cursor='hand2',fg='#57a1f8',font=('Bahnschrift',10))
criar_conta.place(x=654,y=359)
criar_conta.bind('<Enter>', criar_conta_hover)
criar_conta.bind('<Leave>',criar_conta_hover_sair )


############# FIM DA JANELA OU FRAME 2 ###################

janela.mainloop()