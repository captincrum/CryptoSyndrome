# Name       : Shawn McCrum
# Date       : 2017/10/26
# Description: GDAX API -- work with information available to public account
#            : Useful with specific information; like connection limitations
import gdax
from equation import *
from general import *

# Public connection
def public_account(fld, ticker_id):
  pub_file = fld + 'public.txt'   # Create file name/path
  append_to_file(pub_file, fld)   # Append creates file if it doesn't exist or appends to existing file

  pub_connect  = gdax.PublicClient() # Open connection with public host
  pub_ob       = pub_connect.get_product_order_book(ticker_id, level=2) # Connects to live order book (public)
  ticker_bid   = pub_ob['bids']
  ticker_ask   = pub_ob['asks']
  ask_array    = []
  bid_array    = []

  for ask in ticker_ask:
    ask_price = ask[0]
    ask_size  = ask[1]
    ask_num   = ask[2]
    ask_array.append(ask_price)
  print(ask_array)

#  print(ticker_price)
  for bid in ticker_bid:
    bid_price = bid[0]
    bid_size  = bid[1]
    bid_num   = bid[2]
    bid_array.append((bid_price))
  print(bid_array)
#    print(bid_price, bid_size, bid_order)

#  keys_values(ticker_bid)
#  len_order    = len(ticker_bid)    # 50
#  len_ticker   = len(ticker_bid[0]) # 3
#  count_i      = 0
#  count_ii     = 0
#  bid_volume   = []
#  ask_volume   = []
#  while count_ii < len_ticker:
#    while count_i < len_order:
#      bid_volume.append(ticker_bid[count_i][0])
#      bid_volume.append(ticker_bid[count_i][1])
#      ask_volume.append(ticker_ask[count_i][0])
#      ask_volume.append(ticker_ask[count_i][1])
#      count_i += 1
#    count_ii  += 1
#    print(bid_volume, '\n', ask_volume)
#
#    count_i *= 0