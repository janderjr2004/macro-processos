import tkinter.font as tkfont
import tkinter.ttk as ttk
from tkinter import *
import tkinter.font as tkfont
from tkinter import messagebox
from tkinter import ttk
import PyHook3
import pyautogui
import win32gui
import win32api
import win32con
from PIL import Image, ImageTk
import mysql.connector
from tkinter import filedialog
import subprocess
import time
import pythoncom
from csv import DictWriter
import csv
from threading import Timer
import sys
import os

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

subprocess.call('mkdir myprojects', shell= True)

janela = Tk()
janela.title('Macro PYTHON v1.0.0*')
janela.geometry('850x650')
janela.iconbitmap('./imgs/Papirus-Team-Papirus-Apps-Python.ico')

status_botao = 'disabled'

cliques = []
dicionario_eventos = {}

posicao_down = []
posicao_up = []
scroll_up_mouse = []
scroll_down_mouse = []

lista_inicial = [0]

start = 0
end = 0

parar_gravacao_1 = 1

############## CAPTAÇÃO DE EVENTOS DO MOUSE DO WINDOWS #################



def conectarBDD():
    global con
    con = mysql.connector.connect(host='localhost',database='automatizacao',user='root',password='acesso123')

def guardar_dados_BDD():
    conectarBDD()
    if con.is_connected():
            cursor = con.cursor()
            comando_sql = "INSERT INTO automacao(`mouseB_tecla`,`tempo`,`posicao_x`,`posicao_y`,`scroll_coord`) VALUES (%s,%s,%s,%s,%s)"
            if 0 in lista_inicial:
                dados = (botao_mouse,str('1'),posicao_mouse_x,posicao_mouse_y,str('0'))
                lista_inicial.clear()
            else:
                dados = (botao_mouse,str(tempo),posicao_mouse_x,posicao_mouse_y,str('0'))
            cursor.execute(comando_sql,dados)
            print('foi aqui')
            con.commit()

def guardar_dados_scroll_BDD():
    global scroll_up_mouse,scroll_down_mouse
    conectarBDD()
    if con.is_connected():
            cursor = con.cursor()
            comando_sql = "INSERT INTO automacao(`mouseB_tecla`,`tempo`,`posicao_x`,`posicao_y`,`scroll_coord`) VALUES (%s,%s,%s,%s,%s)"
            if scroll_up_mouse:
                dados = (botao_mouse,str('0.5'),str('0'),str('0'),scroll_rolagens_up)
                scroll_up_mouse.clear()
            elif scroll_down_mouse:
                dados = (botao_mouse,str('0.5'),str('0'),str('0'),scroll_rolagens_down)
                scroll_down_mouse.clear()
            cursor.execute(comando_sql,dados)
            con.commit()

def autoincrement():
    conectarBDD()
    if con.is_connected():
            cursor = con.cursor()
            comando_sql = "ALTER TABLE `automatizacao`.`automacao` AUTO_INCREMENT = 1 ;"
            cursor.execute(comando_sql)
            con.commit()
            print('foi aqui')



main_thread_id = win32api.GetCurrentThreadId()
# initialize pygame and start the game loop
def on_timer():
    # win32api.PostThreadMessage(main_thread_id, win32con.WM_QUIT, 0, 0)
    messagebox.showinfo(' ','MACRO REALIZADO COM SUCESSO,      REINICIANDO APLICATIVO...')
    restart_program()

t = Timer(0.1, on_timer) # Quit after 5 seconds


def OnMouseEvent(event):
    global posicao,x,y,cliques,posicao_mouse_x,posicao_mouse_y,botao_mouse,start,end,tempo,posicao_down,posicao_up,scroll_rolagens_down,scroll_rolagens_up,scroll_up_mouse,scroll_down_mouse, parar_gravacao,stop_record,hm,botao_stop,parar_com_gravacao
    
    try:
        if parar_gravacao_1==False:
            t.start()
            
    except:
        janela_inicial_tk.withdraw()
        janela.deiconify

        
        
    
    nome = event.MessageName
    posicao = event.Position
    mouse = nome
    x = int(posicao[0])
    y = int(posicao[1])
    ### FUNÇÃO DE CLIQUE OU DRAG TO COM O BOTÃO ESQUERDO ###

    if nome=='mouse left down' :
        posicao_mouse_x = str(x)
        posicao_mouse_y = str(y)
        posicao_down.append(posicao_mouse_x)
        posicao_down.append(posicao_mouse_y)
        
    if nome=='mouse left up':
        posicao_mouse_x = str(x)
        posicao_mouse_y = str(y)
        posicao_up.append(posicao_mouse_x)
        posicao_up.append(posicao_mouse_y)
        
        if posicao_down[0]==posicao_up[0] and posicao_up[1]==posicao_down[1]:
            if scroll_up_mouse:
                botao_mouse = 'WHLUP'
                scroll_rolagens_up = len(scroll_up_mouse)
                guardar_dados_scroll_BDD()
                
            if scroll_down_mouse:
                botao_mouse = 'WHLDW'
                scroll_rolagens_down = len(scroll_down_mouse)
                guardar_dados_scroll_BDD()
                
            end = time.time()
            tempo = calculatempo()
            botao_mouse = 'LB'
            posicao_mouse_x = str(x)
            posicao_mouse_y = str(y)
            guardar_dados_BDD()
            print('botao esquerdo')
            start = time.time()
            posicao_down.clear()
            posicao_up.clear()
        else:
            if scroll_up_mouse:
                botao_mouse = 'WHLUP'
                scroll_rolagens_up = len(scroll_up_mouse)
                guardar_dados_scroll_BDD()
                
            if scroll_down_mouse:
                botao_mouse = 'WHLDW'
                scroll_rolagens_down = len(scroll_down_mouse)
                guardar_dados_scroll_BDD()

            end = time.time()
            tempo = calculatempo()
            botao_mouse = 'LDG'
            posicao_mouse_x = str(x)
            posicao_mouse_y = str(y)
            guardar_dados_BDD()
            print('drag to esquerdo')
            start = time.time()
            posicao_down.clear()
            posicao_up.clear()
    
    
    ### FUNÇÃO DE CLIQUE OU DRAG TO COM O BOTÃO DIREITO ###
    
    if nome=='mouse right down' :
        posicao_mouse_x = str(x)
        posicao_mouse_y = str(y)
        posicao_down.append(posicao_mouse_x)
        posicao_down.append(posicao_mouse_y)
        
    if nome=='mouse right up':
        posicao_mouse_x = str(x)
        posicao_mouse_y = str(y)
        posicao_up.append(posicao_mouse_x)
        posicao_up.append(posicao_mouse_y)
        
        if posicao_down[0]==posicao_up[0] and posicao_up[1]==posicao_down[1]:
            if scroll_up_mouse:
                botao_mouse = 'WHLUP'
                scroll_rolagens_up = len(scroll_up_mouse)
                guardar_dados_scroll_BDD()
                
            if scroll_down_mouse:
                botao_mouse = 'WHLDW'
                scroll_rolagens_down = len(scroll_down_mouse)
                guardar_dados_scroll_BDD()
                
                
            end = time.time()
            tempo = calculatempo()
            botao_mouse = 'RB'
            posicao_mouse_x = str(x)
            posicao_mouse_y = str(y)
            guardar_dados_BDD()
            print('botao direito')
            start = time.time()
            posicao_down.clear()
            posicao_up.clear()
        else:
            if scroll_up_mouse:
                botao_mouse = 'WHLUP'
                scroll_rolagens_up = len(scroll_up_mouse)
                guardar_dados_scroll_BDD()
                
            if scroll_down_mouse:
                botao_mouse = 'WHLDW'
                scroll_rolagens_down = len(scroll_down_mouse)
                guardar_dados_scroll_BDD()

            end = time.time()
            tempo = calculatempo()
            botao_mouse = 'RDG'
            posicao_mouse_x = str(x)
            posicao_mouse_y = str(y)
            guardar_dados_BDD()
            print('drag to direito')
            start = time.time()
            posicao_down.clear()
            posicao_up.clear()

    ### FUNÇÃO DE CLIQUE OU DRAG TO COM O BOTÃO DO MEIO ###
    
    if nome=='mouse middle down' :
        posicao_mouse_x = str(x)
        posicao_mouse_y = str(y)
        posicao_down.append(posicao_mouse_x)
        posicao_down.append(posicao_mouse_y)
        
    if nome=='mouse middle up':
        posicao_mouse_x = str(x)
        posicao_mouse_y = str(y)
        posicao_up.append(posicao_mouse_x)
        posicao_up.append(posicao_mouse_y)
        
        if posicao_down[0]==posicao_up[0] and posicao_up[1]==posicao_down[1]:
            if scroll_up_mouse:
                botao_mouse = 'WHLUP'
                scroll_rolagens_up = len(scroll_up_mouse)
                guardar_dados_scroll_BDD()
                
            if scroll_down_mouse:
                botao_mouse = 'WHLDW'
                scroll_rolagens_down = len(scroll_down_mouse)
                guardar_dados_scroll_BDD()
                
            end = time.time()
            tempo = calculatempo()
            botao_mouse = 'MB'
            posicao_mouse_x = str(x)
            posicao_mouse_y = str(y)
            guardar_dados_BDD()
            print('botao do meio')
            start = time.time()
            posicao_down.clear()
            posicao_up.clear()
        else:
            if scroll_up_mouse:
                botao_mouse = 'WHLUP'
                scroll_rolagens_up = len(scroll_up_mouse)
                guardar_dados_scroll_BDD()
                
            if scroll_down_mouse:
                botao_mouse = 'WHLDW'
                scroll_rolagens_down = len(scroll_down_mouse)
                guardar_dados_scroll_BDD()
                
            end = time.time()
            tempo = calculatempo()
            botao_mouse = 'MDG'
            posicao_mouse_x = str(x)
            posicao_mouse_y = str(y)
            guardar_dados_BDD()
            print('drag to meio')
            start = time.time()
            posicao_down.clear()
            posicao_up.clear()

    
    ### FUNÇÃO DE SCROLL DO MOUSE ###
    if nome=='mouse wheel':
        if event.Wheel==-1:
            if scroll_up_mouse:
                botao_mouse = 'WHLUP'
                scroll_rolagens_up = len(scroll_up_mouse)
                guardar_dados_scroll_BDD()
                
            scroll_down_mouse.append(event.Wheel)
            print(scroll_down_mouse)
            
        if event.Wheel==1:
            if scroll_down_mouse:
                botao_mouse = 'WHLDW'
                scroll_rolagens_down = len(scroll_down_mouse)
                guardar_dados_scroll_BDD()
            scroll_up_mouse.append(event.Wheel)
            print(scroll_down_mouse)

    return True

    

def iniciar_gravacao():
    global parar_gravacao
    autoincrement()
    botao_record.configure(state='disabled')
    botao_stop.configure(state='normal')
    hm = PyHook3.HookManager()
    hm.MouseAll = OnMouseEvent
    hm.HookMouse()
        
        
    
def parar_gravacao():
    global parar_gravacao_1
    parar_gravacao_1=False
    
def calculatempo():
    return end-start

def puxaridmax():
    global dados_id
    conectarBDD()
    if con.is_connected():
            cursor = con.cursor()
            comando_sql = "SELECT MAX(id_ordem) FROM automacao"
            cursor.execute(comando_sql)
            dados = cursor.fetchall()
            dados_id = dados[0][0]
            return dados_id

def puxar_dados_bdd():
    global dados
    conectarBDD()
    if con.is_connected():
            cursor = con.cursor()
            comando_sql = "SELECT mouseB_tecla,tempo,posicao_x,posicao_y,scroll_coord FROM automacao"
            cursor.execute(comando_sql)
            dados = cursor.fetchall()
            print(dados)
            
def pyautoguicomando_mouse_esquerdo():
    for i in range(0,10):
        if dados[i][0]=='LB':
            pyautogui.click(x=int(dados[i][2]),y=int(dados[i][3]),duration=float(dados[i][1]))
        if dados[i][0]=='RB':
            pyautogui.rightClick(x=int(dados[i][2]),y=int(dados[i][3]),duration=float(dados[i][1]))
        if dados[i][0]=='MB':
            pyautogui.middleClick(x=int(dados[i][2]),y=int(dados[i][3]),duration=float(dados[i][1]))
        if dados[i][0]=='DGLI':
            pyautogui.mouseDown(x=int(dados[i][2]),y=int(dados[i][3]),button='left',duration=float(dados[i][1]))
        if dados[i][0]=='DGLF':
            pyautogui.dragTo(x=int(dados[i][2]),y=int(dados[i][3]),duration=float(dados[i][1]))
        if dados[i][0]=='WHLDW':
            pyautogui.scroll(-120*int(dados[i][4]))
        if dados[i][0]=='WHLUP':
            pyautogui.scroll(120*int(dados[i][4]))


############# MENUS DO APP ################

def abrirarquivo():
    name = filedialog.askopenfilename(initialdir = "/",title = "Abrir Arquivo",filetypes = (("txt","*.txt"),("CSV","*.csv")))
    
def salvarcomo_arquivo():
    name1 = filedialog.asksaveasfilename(defaultextension=".*",filetypes = [("Documento de texto",'.txt'),("CSV",'.csv')])
    
    puxar_dados_bdd()

    ordem_id= 0
    
    with open(name1,'w',newline='') as csvfile:
        csv.writer(csvfile, delimiter=',').writerow(["ordem_id","botao","posicao_x","posicao_y","tempo","scroll"])

    for i in range(0,puxaridmax()):
        ordem_id +=1
        headersCSV = ["ordem_id","botao","posicao_x","posicao_y","tempo","scroll"]      
        dict={"ordem_id": ordem_id, "botao": dados[i][0], "posicao_x": dados[i][2] , "posicao_y": dados[i][3], "tempo": dados[i][1], "scroll": dados[i][4] }
        
        with open(name1, 'a', newline='') as f_object:
            dictwriter_object = DictWriter(f_object, fieldnames=headersCSV)
            dictwriter_object.writerow(dict)
            f_object.close()

menubar = Menu(janela)

filemenu = Menu(menubar,tearoff=False)
menubar.add_cascade(label="         Arquivos         ", menu=filemenu)
filemenu.add_command(label="     N̲ovo                         Ctrl+N")
filemenu.add_command(label="     A̲brir", command=abrirarquivo)

filemenu.add_separator()
filemenu.add_command(label="     S̲alvar                         Ctrl+S")
filemenu.add_command(label="     S̲alvar como                   ",command=salvarcomo_arquivo)
filemenu.add_separator()
filemenu.add_command(label="     S̲air   ")

helpmenu = Menu(menubar,tearoff=False)
menubar.add_cascade(label="       Ajuda       ", menu=helpmenu)
helpmenu.add_command(label='     Documentação           Ctrl+D')
janela.config(menu=menubar)

janela.bind('<Control-n>',lambda x:print('nadad'))
janela.bind('<Control-s>',lambda x: salvarcomo_arquivo())
############# FIM DOS MENUS DO APP ################


############### MENU INICIAL, STOP,RECORD E PLAY #####################

linha_horizontal_topo = Frame(janela,width=850,height=1,bg='#CFCFCF')
linha_horizontal_topo.place(x=0,y=105)

linha_vertical1_topo = Frame(janela,width=1,height=100,bg='#CFCFCF')
linha_vertical1_topo.place(x=230,y=2)


def botao_play_hover(event):
    global botao_play_frame,botao_play_com_frame
    botao_play.place(x=1000,y=2000,height=60,width=60)
    botao_play_frame = Frame(janela,height=64,width=64,bg='#2a8edd')
    botao_play_frame.place(x=5,y=5)
    botao_play_com_frame = Button(botao_play_frame,activebackground='#cce4f7',relief='sunken',borderwidth=0,border=0,image=play_inicial,fg='white',font=('Bahnschrift',11),height=60,width=60)
    botao_play_com_frame.place(x=1,y=1)
    botao_play_com_frame.configure(bg='#e5f1fb')
    botao_play_com_frame.bind('<Leave>',botao_play_hover_sair)

def botao_play_hover_sair(event):
    botao_play_frame.place(x=1000,y=2000)
    botao_play_com_frame.place(x=1000,y=1000)
    botao_play = Button(janela,relief='flat',borderwidth=0,border=0,image=play_inicial,fg='white',font=('Bahnschrift',11))
    botao_play.place(x=8,y=8,height=60,width=60)
    botao_play.bind('<Enter>',botao_play_hover)

    
def botao_record_hover(event):
    global botao_record_frame,botao_record_com_frame
    botao_record.place(x=1000,y=2000,height=60,width=60)
    botao_record_frame = Frame(janela,height=64,width=64,bg='#2a8edd')
    botao_record_frame.place(x=77,y=5)
    botao_record_com_frame = Button(botao_record_frame,command=iniciar_gravacao,activebackground='#cce4f7',relief='sunken',borderwidth=0,border=0,image=record_inicial,fg='white',font=('Bahnschrift',11),height=60,width=60)
    botao_record_com_frame.place(x=1,y=1)
    botao_record_com_frame.configure(bg='#e5f1fb')
    botao_record_com_frame.bind('<Leave>',botao_record_hover_sair)

def botao_record_hover_sair(event):
    botao_record_frame.place(x=1000,y=2000)
    botao_record_com_frame.place(x=1000,y=1000)
    botao_record = Button(janela,relief='flat',command=iniciar_gravacao,borderwidth=0,border=0,image=record_inicial,fg='white',font=('Bahnschrift',11))
    botao_record.place(x=80,y=8,height=60,width=60)
    botao_record.bind('<Enter>',botao_record_hover)
    

def botao_stop_hover(event):
    global botao_stop_frame,botao_stop_com_frame
    botao_stop.place(x=1000,y=2000,height=60,width=60)
    botao_stop_frame = Frame(janela,height=64,width=64,bg='#2a8edd')
    botao_stop_frame.place(x=149,y=5)
    botao_stop_com_frame = Button(botao_stop_frame,command=parar_gravacao,activebackground='#cce4f7',relief='sunken',borderwidth=0,border=0,image=stop_inicial,fg='white',font=('Bahnschrift',11),height=60,width=60)
    botao_stop_com_frame.place(x=1,y=1)
    botao_stop_com_frame.configure(bg='#e5f1fb')
    botao_stop_com_frame.bind('<Leave>',botao_stop_hover_sair)

def botao_stop_hover_sair(event):
    botao_stop_frame.place(x=1000,y=2000)
    botao_stop_com_frame.place(x=1000,y=1000)
    botao_stop = Button(janela,relief='flat',borderwidth=0,command=parar_gravacao,border=0,image=stop_inicial,fg='white',font=('Bahnschrift',11))
    botao_stop.place(x=152,y=8,height=60,width=60)
    botao_stop.bind('<Enter>',botao_stop_hover)
     
       
    
label_play = Label(janela,text='Play',fg='black')
label_play.place(x=22,y=68)

play_inicial = ImageTk.PhotoImage(Image.open("./imgs/play.png"))
botao_play = Button(janela,relief='flat',borderwidth=0,border=0,image=play_inicial,fg='white',font=('Bahnschrift',11))
botao_play.place(x=8,y=8,height=60,width=60)
botao_play.bind('<Enter>',botao_play_hover)
botao_play.configure(state='disabled')

stop_inicial = ImageTk.PhotoImage(Image.open("./imgs/stop.png"))
record_inicial = ImageTk.PhotoImage(Image.open("./imgs/record.png"))

botao_record = Button(janela,cursor='hand2',command=lambda: [iniciar_gravacao()],relief='flat',image=record_inicial,fg='white',font=('Bahnschrift',11))
botao_record.place(x=80,y=8,height=60,width=60)
botao_record.bind('<Enter>',botao_record_hover)


label_record = Label(janela,text='Record',fg='black')
label_record.place(x=88,y=68)

botao_stop = Button(janela,cursor='hand2',command=parar_gravacao,relief='flat',image=stop_inicial,fg='white',font=('Bahnschrift',11))
botao_stop.place(x=152,y=8,height=60,width=60)
botao_stop.bind('<Enter>',botao_stop_hover)

label_stop = Label(janela,text='Stop',fg='black')
label_stop.place(x=166,y=68)


#################### FIM DO MENU INICIAL ###################

#################### MENU 2 ##########################

def editar_inicial_hover(event):
    global editar_inicial_frame,editar_inicial_com_frame
    editar_inicial.place(x=1000,y=2000,height=60,width=60)
    editar_inicial_frame = Frame(janela,height=23,width=66,bg='#2a8edd')
    editar_inicial_frame.place(x=245,y=59)
    editar_inicial_com_frame = Button(editar_inicial_frame,activebackground='#cce4f7',compound=LEFT,text='  Editar',relief='sunken',borderwidth=0,border=0,image=editar_inicial_foto,fg='black',height=17,width=60)
    editar_inicial_com_frame.place(x=1,y=1)
    editar_inicial_com_frame.configure(bg='#e5f1fb')
    editar_inicial_com_frame.bind('<Leave>',editar_inicial_hover_sair)

def editar_inicial_hover_sair(event):
    editar_inicial_frame.place(x=1000,y=2000)
    editar_inicial_com_frame.place(x=1000,y=1000)
    editar_inicial = Button(janela,compound=LEFT,text='  Editar',relief='flat',image=editar_inicial_foto,fg='black',height=17,width=60)
    editar_inicial.place(x=249,y=62,height=17,width=60)
    editar_inicial.bind('<Enter>',editar_inicial_hover)

label_nome_macro= Label(janela,text='Macro name',fg='black')
label_nome_macro.place(x=300,y=12)

entry_nome_macro = Entry(janela, font=('Arial', 12), relief='solid')
entry_nome_macro.place(x=245, y=35, width=195)

linha_vertical1_topo = Frame(janela,width=1,height=100,bg='#CFCFCF')
linha_vertical1_topo.place(x=450,y=2)

var1 = IntVar()
var2 = IntVar()
c1 = Checkbutton(janela, text='CSV',variable=var1, onvalue=1, offvalue=0)
c1.place(x=342,y=60)
c2 = Checkbutton(janela, text='TXT',variable=var2, onvalue=1, offvalue=0)
c2.place(x=392,y=60)

editar_inicial_foto = ImageTk.PhotoImage(Image.open("./imgs/lapis.png"))
editar_inicial = Button(janela,compound=LEFT,text='  Editar',relief='flat',image=editar_inicial_foto,fg='black')
editar_inicial.place(x=249,y=62,height=17,width=60)
editar_inicial.bind('<Enter>',editar_inicial_hover)



#################### TREEVIEW DOS MACROS ######################

style_macros = ttk.Style()
style_macros.theme_use("vista")

# TABELA DE MACROS

colunas_macros = ('nada', 'acao','tempo', 'posicao_x', 'posicao_y','nada1', 'nada2')
tree_macros = ttk.Treeview(janela, columns=colunas_macros, show='headings')

linha_horizontal_treeview = Frame(janela,width=823,height=1,bg='#e5e5e5')
linha_horizontal_treeview.place(x=13,y=142)

tree_macros.column("nada", width=30, anchor=CENTER, minwidth=30, stretch=NO)
tree_macros.column("acao", width=200, anchor=NW, minwidth=120,stretch=NO)
tree_macros.column("tempo", width=110, anchor=NW, minwidth=110, stretch=NO)
tree_macros.column("posicao_x", width=110,anchor=NW, minwidth=85, stretch=NO)
tree_macros.column("posicao_y", width=110,anchor=NW, minwidth=85, stretch=NO)
tree_macros.column("nada1", width=30, anchor=CENTER, minwidth=30)
tree_macros.column("nada2", width=30, anchor=CENTER, minwidth=30, stretch=NO)

tree_macros.heading('nada', text=' ')
tree_macros.heading("acao", text='Ação')
tree_macros.heading("tempo", text='Tempo')
tree_macros.heading("posicao_x", text='Posição X')
tree_macros.heading("posicao_y", text='Posição Y')
tree_macros.heading('nada1', text=' ')
tree_macros.heading('nada2', text=' ')
tree_macros.place(x=12, y=118, height=485, width=825)

linha_horizontal_inferior = Frame(janela,width=850,height=1,bg='#CFCFCF')
linha_horizontal_inferior.place(x=0,y=610)

label_by_jj = Label(janela,text='by: JJ',fg='black')
label_by_jj.place(x=12,y=612,height=15)

######################## FIM DO TREEVIEW DOS MACROS ###################

janela.mainloop()