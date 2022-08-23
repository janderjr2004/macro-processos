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
import os
import sys


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

gravacao=True


def botao_play_hover(event):
    global botao_play_frame,botao_play_com_frame
    botao_play.place(x=1000,y=2000,height=60,width=60)
    botao_play_frame = Frame(janela_inicial_tk,height=64,width=64,bg='#2a8edd')
    botao_play_frame.place(x=5,y=5)
    botao_play_com_frame = Button(botao_play_frame,activebackground='#cce4f7',relief='sunken',borderwidth=0,border=0,image=play_inicial,fg='white',font=('Bahnschrift',11),height=60,width=60)
    botao_play_com_frame.place(x=1,y=1)
    botao_play_com_frame.configure(bg='#e5f1fb')
    botao_play_com_frame.bind('<Leave>',botao_play_hover_sair)

def botao_play_hover_sair(event):
    global botao_play_frame,botao_play_com_frame,botao_play
    botao_play_frame.place(x=1000,y=2000)
    botao_play_com_frame.place(x=1000,y=1000)
    botao_play = Button(janela_inicial_tk,relief='flat',borderwidth=0,border=0,image=play_inicial,fg='white',font=('Bahnschrift',11))
    botao_play.place(x=8,y=8,height=60,width=60)
    botao_play.bind('<Enter>',botao_play_hover)

    
def botao_record_hover(event):
    global botao_record_frame,botao_record_com_frame
    botao_record.place(x=1000,y=2000,height=60,width=60)
    botao_record_frame = Frame(janela_inicial_tk,height=64,width=64,bg='#2a8edd')
    botao_record_frame.place(x=77,y=5)
    botao_record_com_frame = Button(botao_record_frame,command=iniciar_gravacao,activebackground='#cce4f7',relief='sunken',borderwidth=0,border=0,image=record_inicial,fg='white',font=('Bahnschrift',11),height=60,width=60)
    botao_record_com_frame.place(x=1,y=1)
    botao_record_com_frame.configure(bg='#e5f1fb')
    botao_record_com_frame.bind('<Leave>',botao_record_hover_sair)

def botao_record_hover_sair(event):
    global botao_record_frame,botao_record,botao_record_com_frame
    botao_record_frame.place(x=1000,y=2000)
    botao_record_com_frame.place(x=1000,y=1000)
    botao_record = Button(janela_inicial_tk,relief='flat',command=iniciar_gravacao,borderwidth=0,border=0,image=record_inicial,fg='white',font=('Bahnschrift',11))
    botao_record.place(x=80,y=8,height=60,width=60)
    botao_record.bind('<Enter>',botao_record_hover)
    

def botao_stop_hover(event):
    global botao_stop_frame,botao_stop_com_frame
    botao_stop.place(x=1000,y=2000,height=60,width=60)
    botao_stop_frame = Frame(janela_inicial_tk,height=64,width=64,bg='#2a8edd')
    botao_stop_frame.place(x=149,y=5)
    botao_stop_com_frame = Button(botao_stop_frame,command=parar_gravacao,activebackground='#cce4f7',relief='sunken',borderwidth=0,border=0,image=stop_inicial,fg='white',font=('Bahnschrift',11),height=60,width=60)
    botao_stop_com_frame.place(x=1,y=1)
    botao_stop_com_frame.configure(bg='#e5f1fb')
    botao_stop_com_frame.bind('<Leave>',botao_stop_hover_sair)

def botao_stop_hover_sair(event):
    global botao_stop_frame,botao_stop_com_frame,botao_stop
    botao_stop_frame.place(x=1000,y=2000)
    botao_stop_com_frame.place(x=1000,y=1000)
    botao_stop = Button(janela_inicial_tk,relief='flat',borderwidth=0,command=parar_gravacao,border=0,image=stop_inicial,fg='white',font=('Bahnschrift',11))
    botao_stop.place(x=152,y=8,height=60,width=60)
    botao_stop.bind('<Enter>',botao_stop_hover)




def editar_inicial_hover(event):
    global editar_inicial_frame,editar_inicial_com_frame,editar_inicial,editar_inicial_foto
    editar_inicial.place(x=1000,y=2000,height=60,width=60)
    editar_inicial_frame = Frame(janela_inicial_tk,height=23,width=66,bg='#2a8edd')
    editar_inicial_frame.place(x=245,y=59)
    editar_inicial_com_frame = Button(editar_inicial_frame,activebackground='#cce4f7',compound=LEFT,text='  Editar',relief='sunken',borderwidth=0,border=0,image=editar_inicial_foto,fg='black',height=17,width=60)
    editar_inicial_com_frame.place(x=1,y=1)
    editar_inicial_com_frame.configure(bg='#e5f1fb')
    editar_inicial_com_frame.bind('<Leave>',editar_inicial_hover_sair)

def editar_inicial_hover_sair(event):
    global editar_inicial,editar_inicial_frame,editar_inicial_com_frame,editar_inicial_foto
    editar_inicial_frame.place(x=1000,y=2000)
    editar_inicial_com_frame.place(x=1000,y=1000)
    editar_inicial = Button(janela_inicial_tk,compound=LEFT,text='  Editar',relief='flat',image=editar_inicial_foto,fg='black',height=17,width=60)
    editar_inicial.place(x=249,y=62,height=17,width=60)
    editar_inicial.bind('<Enter>',editar_inicial_hover)
    

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

parar_com_gravacao=True

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

def conectarBDD_automatizacao():
        global con
        con = mysql.connector.connect(host='localhost',database='automatizacao',user='root',password='acesso123')


def iniciar_gravacao():
    autoincrement()
    botao_record.configure(state='disabled')
    botao_stop.configure(state='normal')
    hm = PyHook3.HookManager()
    hm.MouseAll = OnMouseEvent
    
        
        
    
def parar_gravacao():
    global parar_com_gravacao
    parar_com_gravacao=False
    
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

def sair_menu():
    janela_inicial_tk.withdraw()
    janela.deiconify()

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

main_thread_id = win32api.GetCurrentThreadId()
# initialize pygame and start the game loop
def on_timer():
    # win32api.PostThreadMessage(main_thread_id, win32con.WM_QUIT, 0, 0)
    messagebox.showinfo(' ','MACRO REALIZADO COM SUCESSO,      REINICIANDO APLICATIVO...')
    restart_program()

t = Timer(0.1, on_timer) # Quit after 5 seconds

    
    
    
    

def janela_inicial():
    global botao_record,label_by_jj,linha_horizontal_inferior,tree_macros,colunas_macros,linha_horizontal_treeview,style_macros,editar_inicial_foto,editar_inicial,c2,c1,label_nome_macro,entry_nome_macro,linha_vertical1_topo,label_stop,botao_stop,label_record,botao_record,stop_inicial,record_inicial,botao_play,play_inicial,linha_vertical1_topo,janela_inicial_tk,var1,var2
    
    subprocess.call('mkdir myprojects', shell= True)
    janela.withdraw()
    janela_inicial_tk = Toplevel()
    janela_inicial_tk.title('Macro PYTHON v1.0.0*')
    janela_inicial_tk.geometry('850x650')
    janela_inicial_tk.iconbitmap('./imgs/Papirus-Team-Papirus-Apps-Python.ico')

    


    menubar = Menu(janela_inicial_tk)

    filemenu = Menu(menubar,tearoff=False)
    menubar.add_cascade(label="         Arquivos         ", menu=filemenu)
    filemenu.add_command(label="     N̲ovo                         Ctrl+N")
    filemenu.add_command(label="     A̲brir", command=abrirarquivo)

    filemenu.add_separator()
    filemenu.add_command(label="     S̲alvar                         Ctrl+S")
    filemenu.add_command(label="     S̲alvar como                   ",command=salvarcomo_arquivo)
    filemenu.add_separator()
    filemenu.add_command(label="     S̲air   ",command=sair_menu)

    helpmenu = Menu(menubar,tearoff=False)
    menubar.add_cascade(label="       Ajuda       ", menu=helpmenu)
    helpmenu.add_command(label='     Documentação           Ctrl+D')
    janela_inicial_tk.config(menu=menubar)

    janela_inicial_tk.bind('<Control-n>',lambda x:print('nadad'))
    janela_inicial_tk.bind('<Control-s>',lambda x: salvarcomo_arquivo())
    ############# FIM DOS MENUS DO APP ################


    ############### MENU INICIAL, STOP,RECORD E PLAY #####################

    linha_horizontal_topo = Frame(janela_inicial_tk,width=850,height=1,bg='#CFCFCF')
    linha_horizontal_topo.place(x=0,y=105)

    linha_vertical1_topo = Frame(janela_inicial_tk,width=1,height=100,bg='#CFCFCF')
    linha_vertical1_topo.place(x=230,y=2)
        
        
        
    label_play = Label(janela_inicial_tk,text='Play',fg='black')
    label_play.place(x=22,y=68)

    play_inicial = ImageTk.PhotoImage(Image.open("./imgs/play.png"))
    botao_play = Button(janela_inicial_tk,relief='flat',borderwidth=0,border=0,image=play_inicial,fg='white',font=('Bahnschrift',11))
    botao_play.place(x=8,y=8,height=60,width=60)
    botao_play.bind('<Enter>',botao_play_hover)
    botao_play.configure(state='disabled')



    botao_record = Button(janela_inicial_tk,cursor='hand2',command=lambda: [iniciar_gravacao()],relief='flat',image=record_inicial,fg='white',font=('Bahnschrift',11))
    botao_record.place(x=80,y=8,height=60,width=60)
    botao_record.bind('<Enter>',botao_record_hover)


    label_record = Label(janela_inicial_tk,text='Record',fg='black')
    label_record.place(x=88,y=68)

    botao_stop = Button(janela_inicial_tk,cursor='hand2',command=lambda x: parar_gravacao(),relief='flat',image=stop_inicial,fg='white',font=('Bahnschrift',11))
    botao_stop.place(x=152,y=8,height=60,width=60)
    botao_stop.bind('<Enter>',botao_stop_hover)

    label_stop = Label(janela_inicial_tk,text='Stop',fg='black')
    label_stop.place(x=166,y=68)



    #################### FIM DO MENU INICIAL ###################

    #################### MENU 2 ##########################



    label_nome_macro= Label(janela_inicial_tk,text='Macro name',fg='black')
    label_nome_macro.place(x=300,y=12)

    entry_nome_macro = Entry(janela_inicial_tk, font=('Arial', 12), relief='solid')
    entry_nome_macro.place(x=245, y=35, width=195)

    linha_vertical1_topo = Frame(janela_inicial_tk,width=1,height=100,bg='#CFCFCF')
    linha_vertical1_topo.place(x=450,y=2)

    var1 = IntVar()
    var2 = IntVar()
    c1 = Checkbutton(janela_inicial_tk, text='CSV',variable=var1, onvalue=1, offvalue=0)
    c1.place(x=342,y=60)
    c2 = Checkbutton(janela_inicial_tk, text='TXT',variable=var2, onvalue=1, offvalue=0)
    c2.place(x=392,y=60)



    editar_inicial_foto = ImageTk.PhotoImage(Image.open("./imgs/lapis.png"))
    editar_inicial = Button(janela_inicial_tk,compound=LEFT,text='  Editar',relief='flat',image=editar_inicial_foto,fg='black')
    editar_inicial.place(x=249,y=62,height=17,width=60)
    editar_inicial.bind('<Enter>',editar_inicial_hover)



    #################### TREEVIEW DOS MACROS ######################

    style_macros = ttk.Style()
    style_macros.theme_use("vista")

    # TABELA DE MACROS

    colunas_macros = ('nada', 'acao','tempo', 'posicao_x', 'posicao_y','nada1', 'nada2')
    tree_macros = ttk.Treeview(janela_inicial_tk, columns=colunas_macros, show='headings')

    linha_horizontal_treeview = Frame(janela_inicial_tk,width=823,height=1,bg='#e5e5e5')
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

    linha_horizontal_inferior = Frame(janela_inicial_tk,width=850,height=1,bg='#CFCFCF')
    linha_horizontal_inferior.place(x=0,y=610)

    label_by_jj = Label(janela_inicial_tk,text='by: JJ',fg='black')
    label_by_jj.place(x=12,y=612,height=15)

    ######################## FIM DO TREEVIEW DOS MACROS ###################

    






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
                janela_inicial()
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
            dados = (str(input_user_placeholder_cadastro.get()),str(input_email_placeholder_cadastro.get()),str(input_senha_placeholder_cadastro.get()))
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


stop_inicial = ImageTk.PhotoImage(Image.open("./imgs/stop.png"))
record_inicial = ImageTk.PhotoImage(Image.open("./imgs/record.png"))

############# FIM DA JANELA OU FRAME 2 ###################

janela.mainloop()