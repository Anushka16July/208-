import socket
from threading import Thread
from tkinter import *
from tkinter import ttk



PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

setup()

def musicWindow():

    window=Tk()

    window.title('Messenger')
    window.geometry("300x300")
    window.configure(bg='LightSkyBlue')

    global listbox
    global selectLabel 


    selectLabel = Label(window,text="select song",bg='LightSKyBlue',font=('Calibri',0))
    selectLabel.place(x=2,y=1)

   
   
