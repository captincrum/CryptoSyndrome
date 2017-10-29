# Name         : Shawn McCrum
# Date         : 2017/10/29
# Description  : Use Gdax API. Set up account access.
# Documentation: https://github.com/danpaquin/gdax-python
from tkinter import *
from myWS import *
from publicConnect import *
from privateConnection import *


class GDAX_Bot:               # Starts each instance of GDAX_Bot
  def __init__(self, master): # Start_bot tkinter project
    frame = Frame(master)     # Box for GUI
    frame.pack()              # Tell tkinter to pack the frame

    # Each buttons function
    self.update_ws  = Button(frame, text='Webs Connect', command=self.btn_i)
    self.update_pub = Button(frame, text='Public Users', command=self.btn_ii)
    self.update_acc = Button(frame, text='User Account', command=self.btn_iii)
    # Package and style each button
    self.update_ws.pack(side=LEFT)
    self.update_pub.pack(side=LEFT)
    self.update_acc.pack(side=RIGHT)

  # Execute each time the corresponding button is pressed
  def btn_i(self):    # Associate: btn_i with the function that updates websocket
    start_websocket() # Accesses : Websocket the order book in sequential order
  def btn_ii(self):   # Associate: btn_ii with the function that updates public information
    public_account()  # Accesses : information available to everyone
  def btn_iii(self):  # Associate: btn_iii with the function that updates user account information
    access_account()  # Accesses : accounts using login credentials

root = Tk()           # Creates variable using tkinter import
bot  = GDAX_Bot(root) # Creates variable using root class GDAX_Bot

# Style section for Tkinter root
root.title('Stock Syndrome')
root.geometry('500x400')
root.mainloop()
