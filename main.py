# Name         : Shawn McCrum
# Date         : 2017/11/01
# Description  : Use Gdax API. Set up account access.
# Documentation: https://github.com/danpaquin/gdax-python
from tkinter import *
from myWS import *
from publicConnect import *
from privateConnection import *

ticker_ids = ['BTC-USD']#, 'ETH-BTC', 'ETH-USD']] #, 'ETH-USD', 'ETH-BTC'] # Each relevant ticker
fld        = 'Data/'

class GDAX_Bot:               # Starts each instance of bot
  def __init__(self, master): # Definition to run first each time class is started
    create_project_dir(fld)   # Create fld for project data
    frame = Frame(master)     # Create box for GUI
    frame.pack()              # Packing frame tells tkinter to place

    # Each buttons function
    self.update_ws  = Button(frame, text='Webs Connect', command=self.btn_i)
    self.update_pub = Button(frame, text='Public Users', command=self.btn_ii)
    self.update_acc = Button(frame, text='User Account', command=self.btn_iii)
    # Package and style each button
    self.update_ws.pack(side=LEFT)
    self.update_pub.pack(side=LEFT)
    self.update_acc.pack(side=RIGHT)

  def btn_i(self):                    # Execute def each time the corresponding button is pressed
    for ticker_id in ticker_ids:      # Iterate each ticker id in ticker ids
      start_websocket(fld, ticker_id) # Accesses : Websocket the order book in sequential order
  def btn_ii(self):                   # Updates user public account information
    for ticker_id in ticker_ids:      # Iterate each ticker id in ticker ids
      public_account(fld, ticker_id)  # Accesses : information available to everyone
  def btn_iii(self):                  # Updates user account information
    access_account(fld)               # Accesses : accounts using login credentials

# Start instance for tkinter (GUI tool)
root = Tk()                   # Creates variable using tkinter import
bot  = GDAX_Bot(root)         # Creates variable using root class GDAX_Bot
# Style section for Tkinter root
root.title('Crypto Syndrome') # Program name
root.geometry('500x400')      # Size of program box (in pixels)
root.mainloop()               # Loop used to keep project open until user clicks close