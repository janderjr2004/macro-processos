import pythoncom as pc, PyHook3 as ph
import time

def KeyboardHook(event):
    print(chr(event.Ascii))
    return True

hm = ph.HookManager()
hm.KeyDown = KeyboardHook
hm.HookKeyboard()

while time.clock() < 5:
    pc.PumpWaitingMessages()
























































