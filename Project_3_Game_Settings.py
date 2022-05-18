
import tkinter as tk 
from tkinter import Toplevel, ttk, BooleanVar


import json
#I manage to get througth most parts of the project i got the gui to read in a default settings. 
# However, I could not figure out how to update the default settings after change. 
# When you change the settings it does write to a json file 
# The only things I had issues with was restoring default settings after chnage and updated the default settings to the new settings

def change_settings():
    #This function gets and variable values and places them in a dictionary to better manage them
    settings ={'Game_difficulty': preset.get(),
                'Character_name': tag.get(),
                'Volume': sound.get(),
                'Texture': quality.get(),
                'Graphics': resolution.get(),
                'Objective_Pop-up': var1.get(),
                'Scalable_Enemies': var2.get()
        }

    
    with open('Project_3_Settings.json', 'w') as file:
        json.dump(settings, file, indent=4)
       







#Function to access the default settings of the pyhton
def access_settings():
    branche = Toplevel(main)
    branche.title("Settings Menu")
    branche.geometry('470x470')

    with open('Project_3_Default_Settings.json', 'r') as file:
        data = json.load(file)


    p = data["Game_difficulty"]
    t = data["Character_name"]
    s = data["Volume"]
    m = data["Texture"]
    r = data["Graphics"]
    v = data["Objective_Pop-up"]
    v2 = data["Scalable_Enemies"]


    preset = tk.StringVar()
    tag = tk.StringVar()
    quality = tk.StringVar()
    sound = tk.IntVar()
    resolution = tk.StringVar()
    

    preset.set(p)
    tag.set(t)
    quality.set(m)
    sound.set(s)
    resolution.set(r)

    

    title = tk.Label(branche, text="Default Settings Menu")
    title.pack()


    # Overall game dificulty dropdown menu
    difficulty_label = tk.Label(branche, text="Game difficulty")
    difficulty_label.pack()
    difficulty = tk.OptionMenu(branche, preset, "Easy", "Meduim", "Hard")
    difficulty.pack()
    difficulty.configure(width=10)

    # Character name entry box
    name_label = tk.Label(branche, text="Chracter Name")
    name_label.pack()
    name = tk.Entry(branche, textvariable=tag)
    name.pack()


    # Volume scale
    volume_label = tk.Label(branche, text="Set Volume")
    volume_label.pack()
    volume = tk.Scale(branche, from_=0, to=100, variable=sound, orient="horizontal")
    volume.pack()

    # Texture class dropdown menu
    texture_label = tk.Label(branche, text="Texture")
    texture_label.pack()
    texture = tk.OptionMenu(branche, quality, "Lowest", "Low","Meduim", "High", "Highest")
    texture.pack()
    texture.configure(width=10)

    # Graphics dropdown

    graphics_label = tk.Label(branche, text="Graphics")
    graphics_label.pack()
    graphics = tk.OptionMenu(branche, resolution, "Low", "Meduim", "High")
    graphics.pack()
    graphics.configure(width=10)


    # checkbutton
    objective_label = tk.Label(branche, text="Show Objective Pop-ups")
    objective_label.pack()
    objective = tk.Checkbutton(branche, variable=v)
    objective.pack()


    # checkbutton
    scalable_label = tk.Label(branche, text="Scalable Enemies")
    scalable_label.pack()
    scalable = tk.Checkbutton(branche, variable=v2)
    scalable.pack()

    
  






main = tk.Tk()
main.title("Start Menu")
main.geometry('470x470')

with open('Project_3_Default_Settings.json', 'r') as file:
    data = json.load(file)


p = data["Game_difficulty"]
t = data["Character_name"]
s = data["Volume"]
m = data["Texture"]
r = data["Graphics"]
v = data["Objective_Pop-up"]
v2 = data["Scalable_Enemies"]


preset = tk.StringVar()
tag = tk.StringVar()
quality = tk.StringVar()
sound = tk.IntVar()
resolution = tk.StringVar()
var1 = tk.BooleanVar()
var2 = tk.BooleanVar()

preset.set(p)
tag.set(t)
quality.set(m)
sound.set(s)
resolution.set(r)
var1.set(v)
var2.set(v2)




#Overall game dificulty dropdown menu 
difficulty_label = tk.Label(main, text="Game difficulty")
difficulty_label.pack()
difficulty = tk.OptionMenu(main, preset, "Easy", "Meduim", "Hard")
difficulty.pack()
difficulty.configure(width=10)

#Character name entry box 
name_label = tk.Label(main, text="Chracter Name")
name_label.pack()
name= tk.Entry(main, textvariable = tag)
name.pack()


#Volume scale 
volume_label = tk.Label(main, text="Set Volume")
volume_label.pack()
volume = tk.Scale(main,from_= 0, to=100, variable=sound, orient = "horizontal")
volume.pack()

#Texture class dropdown menu 
texture_label = tk.Label(main, text="Texture")
texture_label.pack()
texture = tk.OptionMenu(main, quality, "Lowest", "Low","Meduim", "High", "Highest")
texture.pack()
texture.configure(width=10)

#Graphics dropdown
graphics_label = tk.Label(main, text="Graphics")
graphics_label.pack()
graphics = tk.OptionMenu(main, resolution, "Low", "Meduim", "High")
graphics.pack()
graphics.configure(width=10)


#checkbutton
objective_label = tk.Label(main, text="Show Objective Pop-ups")
objective_label.pack()
objective = tk.Checkbutton(main, variable=var1)
objective.pack()


#checkbutton 
scalable_label = tk.Label(text="Scalable Enemies")
scalable_label.pack()
scalable = tk.Checkbutton(main, variable=var2)
scalable.pack()


acces = ttk.Button(main, text= "Change Settings", command=change_settings)
acces.pack()


main.mainloop()

