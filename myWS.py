# Name       : Shawn McCrum
# Date       : 2017/11/01
# Description: GDAX API -- work with information from the live order book.
import gdax, time
from equation import *
from general import append_to_file


# Stream of live order book data
def start_websocket(fld, ticker_id):

  start_time  = time.time()               # Mark start time
  ws_file     = fld + 'websocket.txt'     # Create file name/path
  append_to_file(ws_file, fld)            # Append creates file if it doesn't exist or appends to existing file
  ws_url      = 'wss://ws-feed.gdax.com/' # Connection for website API
  limit       = 100                       # Defines size of data set
  b_ord_price = []                        # Buy order information gathered for further equations
  s_ord_price = []                        # Sell order information gathered for further equations
  ord_seq     = []                        # Information gathered for further equations

  # Websocket for each ws_product
  class myWebsocketClient(gdax.WebsocketClient):

    # Called once: immediately before the socket connection is made. This is where initial parameters are set.
    def on_open(self):
      self.url      = ws_url
      self.products = ticker_id
      print('Lets count the messages!')

    # Called once: for every message that arrives and accepts one argument that contains the message of dict type.
    def on_message(self, msg):
      self.msg_seq  = msg['sequence'] # Values: increasing integer values for each product with every new message
      self.msg_type = msg['type']     # Values: open, done, received
      self.msg_side = msg['side']     # Values: buy, sell

      # Continue with buy orders
      if 'price' in msg and 'buy' in self.msg_side:
        # Gather variables for each message
        msg_price = msg['price']
        # Add information for calculations
        ord_seq.append(self.msg_seq)
        b_ord_price.append(msg_price)

      # Continue with sell orders
      if 'price' in msg and 'sell' in self.msg_side:
        msg_price = msg['price']
        ord_seq.append(self.msg_seq)
        s_ord_price.append(msg_price)

    # Called after is connection is closed # Used to perform mathematical operations
    def on_close(self):
      time_limit = (time.time() - start_time) # Records time taken (before calculations) to meet qualifications set by limit
      mean(b_ord_price)
      mean(s_ord_price)# Mean, median, mode

  # Associate classes and start class
  wsClient = myWebsocketClient()
  wsClient.start()

  # Parameters for websocket once the connection limit is met
  while (len(ord_seq) < limit):
    time.sleep(.4) # Interval to wait before reconnecting
  wsClient.close() # Method to close the websocket connection
#  start_websocket() # Begin connection # Becomes an issue with tkinter; create toggle switch
