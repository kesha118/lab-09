""" 
Description: 
  Graphical user interface that displays select information about a 
  user-specified Pokemon fetched from the PokeAPI 

Usage:
  python poke_info_viewer.py
"""
from tkinter import *
from tkinter import ttk
from poke_api import get_pokemon_info
from tkinter import messagebox 

# Create the main window
root = Tk()
root.title("Pokemon Information")

# TODO: Create the frames
frame_input = ttk.Frame(root)
frame_input.grid(row=1, column=0, columnspan=2, pady=(20,1))

frame_info = ttk.LabelFrame(root, text="Info")
frame_info.grid(row=1, column=0, padx=(20,10), pady=(10,20), sticky=N)

frame_info = ttk.LabelFrame(root, text="stats")
frame_info.grid(row=1, column=1, padx=(10,20), pady=(10,20), sticky=N)

label_name = ttk.Entry(frame_input, text="Pokemon Name")
label_name.grid(row=0, column=0, padx=(10,5),pady=(10))

enter_name=ttk.Entry(frame_input)
enter_name.insert(0,'pikachu')
enter_name.grid(row=0, column=1)

def handle_button_get_info():
     poke_name = enter_name.get().strip()
     if poke_name == '': return
     poke_info = get_pokemon_info(poke_name)
     if poke_info:
          label_height_value = [text] = str(poke_info['height']) + ' dm'
          label_weight_value = [text] = str(poke_info['weight']) + ' hg'
          #types_list = [t['type']['name'].capitilize() for t in poke_info['types']]

button_get_info = ttk.button(frame_input, text='Get Info', command=handle_button_get_info)
button_get_info.grid(row=0, column=2, padx=10, pady=10)
# TODO: Populate the user input frame with widgets

label_height =ttk.Label(frame_info, text= "Height:")
label_height.grid(row=0, column=0, padx=(10,5),pady=(10,5), sticky=E)
label_height_value = ttk.Label(frame_info,width=20)
label_height_value.grid(row=1,column=1,padx=(0,10),pady=(10,5), sticky=W)

# TODO: Define button click event handler function

root.mainloop()