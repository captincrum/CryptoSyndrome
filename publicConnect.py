# Name       : Shawn McCrum
# Date       : 2017/10/27
# Description: GDAX API -- work with information available to public account
#            : Useful with specific information; like connection limitations
import gdax


# Public connection
def public_account():

  ticker_ids  = ['BTC-USD']#, 'ETH-USD', 'ETH-BTC'] # Each relevant ticker
  pub_connect = gdax.PublicClient()                 # Open connection with public host
#  pub_product = pub_connect.get_products()
#    keys_values(ticker_id, pub_product[0])

  for ticker_id in ticker_ids:
    pub_ob     = pub_connect.get_product_order_book(ticker_id, level=2) # Connects to live order book (public)
    ticker_bid = pub_ob['bids']
    ticker_ask = pub_ob['asks']

    for ask_group in ticker_ask:
      ask_price  = ask_group[0]
      ask_size   = ask_group[1]
      ask_volume = ask_group[2]
      print('\n', ticker_id, '\nAsk Price:', ask_price, '\nOrder Size:', ask_size, '\nVolume at Price:', ask_volume, '\n')

    for bid_group in ticker_bid:
      bid_price  = bid_group[0]
      bid_size   = bid_group[1]
      bid_volume = bid_group[2]
      print('\n', ticker_id, '\nBid Price:', bid_price, '\nOrder Size:', bid_size, '\nVolume at Price:', bid_volume, '\n')
