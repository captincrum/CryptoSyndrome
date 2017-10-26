# Name       : Shawn McCrum
# Date       : 2017/10/18
# Description: GDAX API -- work with information from the live order book.
import gdax, time
from equation import *


# Stream of live order book data
def start_websocket():
  start_time = time.time()               # Mark start time
  ws_product = ['BTC-USD']               #, 'ETH-BTC', 'ETH-USD'] # Information will be gathered for each ticker in the array
  ws_url     = 'wss://ws-feed.gdax.com/' # Connection for website API
  limit      = 32                        # Gathers variables for duration in seconds
  ord_price  = []
  ord_seq    = []

  # Websocket for each ws_product
  class myWebsocketClient(gdax.WebsocketClient):

    # Called once: immediately before the socket connection is made. This is where initial parameters are set.
    def on_open(self):
      self.url           = ws_url
      self.products      = ws_product
      print('Lets count the messages!')

    # Called once: for every message that arrives and accepts one argument that contains the message of dict type.
    def on_message(self, msg):
      self.msg_seq  = msg['sequence'] # Values: increasing integer values for each product with every new message
      self.msg_type = msg['type']     # Values: open, done, received
      self.msg_side = msg['side']     # Values: buy, sell

      # Continue if stated price for the buy order side
      if 'price' in msg and 'buy' in self.msg_side:
        # Gather variables for each message
        msg_price = msg['price']
        # Add information for calculations
        ord_seq.append(self.msg_seq)
        ord_price.append(msg_price)

    # Called after is connection is closed # Used to perform mathematical operations
    def on_close(self):
      time_limit = (time.time() - start_time) # Records time taken (before calculations) to meet qualifications set by limit
      mean(ord_price)                         # Mean, median, mode
      print(time_limit)

  wsClient = myWebsocketClient() # Create value passed to myWebsocket
  wsClient.start()               # Open connection

  # Parameters for websocket once the connection limits are met
  while (len(ord_seq) < limit):
    pass
  wsClient.close()  # Method to close the websocket connection
  time.sleep(0.3)   # Interval to wait before reconnecting
  start_websocket() # Begin connection