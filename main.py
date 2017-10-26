# Name         : Shawn McCrum
# Date         : 2017/10/18
# Description  : Use Gdax API. Set up account access.
# Documentation: https://github.com/danpaquin/gdax-python
from tkinter import *
from myWS import *
from publicConnect import *
from privateConnection import *


# Begins project
class GDAX_Bot:
  # Initialize for each instance of GDAX_Bot
  def __init__(self, master):
    frame = Frame(master) # Box for GUI # Associate root with master
    frame.pack()          # Pack the frame

    # Each buttons function
    self.update_ws  = Button(frame, text='Update Websocket', command=self.button_one)
    self.update_pub = Button(frame, text='Update Public Connection', command=self.button_two)
    self.update_acc = Button(frame, text='Update User Account', command=self.button_three)
    # Package and style each button
    self.update_ws.pack(side=LEFT)
    self.update_pub.pack(side=LEFT)
    self.update_acc.pack(side=RIGHT)

  # Execute each time the corresponding button is pressed
  def button_one(self):
    start_websocket() # Accesses: Websocket the order book in sequential order
  def button_two(self):
    public_account()  # Accesses: information available to everyone
  def button_three(self):
    access_account()  # Accesses: accounts using login credentials
#  def record_data(self): # Create def to record and save retrieved data
#    create_project_dir('Project Files')

root      = Tk()
stare_bot = GDAX_Bot(root)

root.title('Stock Syndrome')
root.geometry('500x400')
root.mainloop()