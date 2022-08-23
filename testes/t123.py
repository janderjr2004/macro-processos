# import tkinter as tk
# import tkinter.ttk as ttk
  
# root = tk.Tk()
  
# # initialize style function
# style = ttk.Style()
  
# # Use clam theme
# style.theme_use('default')
  
# # Used TLabelframe for styling labelframe widgets,
# # and use red color for border
# style.configure("TLabelframe", bordercolor="red")
  
# labelframe = ttk.LabelFrame(root, text = "GFG")
# labelframe.grid(padx = 30, pady = 30)
  
# left = tk.Label(labelframe, text = "Geeks for Geeks")
# left.pack()
  
# root.mainloop()

import tkinter as tk
import tkinter.ttk as ttk
  
# initialize the tkinter window
root = tk.Tk()
  
# initializing the style function
style = ttk.Style()
  
# creating the theme with the
# initializing the style function
style = ttk.Style()
  
# creating the theme with the
style.theme_create('style_class',
  
                   # getting the settings
                   settings={
  
                       # getting through the Labelframe
                       # widget
                       'TLabelframe': {
                           
                           # configure the changes
                           'configure': {
                               'background': 'green'
                           }
                       },
  
                       # getting through the Labelframe's 
                       # label widget
                       'TLabelframe.Label': {
                           'configure': {
                               'background': '#f0f0f0'
                           }
                       }
                   }
                   )
style.theme_use('style_class')
  
# created a label frame with title "Group"
labelframe = ttk.LabelFrame(root, text="Group")
  
# provide padding
labelframe.pack(padx=30, pady=30)
  
# created the text label inside the the labelframe
left = tk.Label(labelframe, text="Geeks for Geeks")
  
left.pack()
  
root.mainloop()