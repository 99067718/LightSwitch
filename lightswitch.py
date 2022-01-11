import tkinter as tk
import webbrowser
import time
window = tk.Tk()
window.title("Yay a lightswitch!!!")
window.configure(bg="yellow")
OnOff = "on"
ClickedThebutton = 0
lightOn = tk.PhotoImage(file='Assets\Images\on.png')
lightOff = tk.PhotoImage(file='Assets\Images\off.png') 
lightBulbOn = tk.PhotoImage(file='Assets\Images\onLightBulb.png')
lightBulbOff = tk.PhotoImage(file='Assets\Images\offLightBulb.png')
lightBulbImage = tk.Label(image=lightBulbOn)
lightBulbImage.pack()

def Click():
    global OnOff
    global ClickedThebutton
    if OnOff == "off":
        print("the light is now on.")
        window.configure(bg="yellow")
        OnOff = "on"
        window.title("The light is on WOW")
        button.configure(image=lightOn)
        lightBulbImage.configure(image=lightBulbOn)
        ClickedThebutton += 1

    else:
        print("the light is now off.")
        window.configure(bg="black")
        OnOff = "off"
        window.title("Aww the light is now off")
        button.configure(image= lightOff)
        lightBulbImage.configure(image=lightBulbOff)
        ClickedThebutton += 1

    if ClickedThebutton == 10:
        print("wow")
button = tk.Button(image= lightOn, bg="white", fg="black",command = Click, borderwidth=0)
button.pack(pady = 30, padx = 30)

# schijf hier tussen je code

# schijf hier tussen je code

window.mainloop()