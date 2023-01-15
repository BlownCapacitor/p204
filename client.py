import socket
from tkinter import *
from  threading import Thread
from PIL import ImageTk, Image
import random

screen_width = None
screen_height = None

SERVER = None
PORT = None
IP_ADDRESS = None


canvas1 = None

playerName = None
nameEntry = None
nameWindow = None

def saveName():
    global SERVER 
    global playerName
    global nameWindow
    global nameEntry

    playerName = nameEntry.get()
    nameEntry.delete(0,END)
    nameWindow.destroy()
    SERVER.send(playerName.encode())
    

def askPlayerName():
    global playerName
    global nameEntry
    global nameWindow
    global canvas1
    global screen_width
    global screen_height

    nameWindow  = Tk()
    nameWindow.title("Tambola Game: Login")
    nameWindow.geometry('800x533')


    screen_width = nameWindow.winfo_screenwidth()
    screen_height = nameWindow.winfo_screenheight()

    bg = ImageTk.PhotoImage(file = "./assets/tambola2.jpeg")

    canvas1 = Canvas( nameWindow, width = 500,height = 500)
    canvas1.pack(fill = "both", expand = True)
    canvas1.create_image( 0, 0, image = bg, anchor = "nw")
    canvas1.create_text( screen_width/4.05,screen_height/7.55, text = "Enter Name:", font=("Chalkboard SE",60), fill="black")
    canvas1.create_text( screen_width/4,screen_height/7.5, text = "Enter Name:", font=("Chalkboard SE",60), fill="#32a852")
    nameEntry = Entry(nameWindow, width=15, justify='center', font=('Chalkboard SE', 30), bd=5, bg='white')
    nameEntry.place(x = screen_width/7, y=screen_height/5.5 )
    button = Button(nameWindow, text="Save", font=("Chalkboard SE", 30),width=9, command=saveName, height=1, bg="#80deea", bd=3)
    button.place(x = screen_width/5.5, y=screen_height/4)
    nameWindow.resizable(True, True)
    nameWindow.mainloop()

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    PORT  = 5000
    IP_ADDRESS = '127.0.0.1'

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    askPlayerName()




setup()
