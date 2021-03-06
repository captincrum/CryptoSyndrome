# Name       : Shawn McCrum
# Date       : 2017/10/29
# Description: Create a flexible and organized environment. This file contains the most basic of actions.
import os
import pandas as pd

# # # Import os section # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def create_project_dir(directory):  # Definition that looks for existing folder. Name = directory
  if not os.path.exists(directory): # Look for existing folder. Only continue is it doesn't exist
    os.makedirs(directory)          # Create folder at specified location
  else:                             # Continue if folder exists
    print(directory, 'exists')      # Updates the user to ensure create_project_dir isn't being over-called
    pass

def append_to_file(path, data): # Add data onto an existing file
  with open(path, 'a') as file:
    file.write(data + '\n')

# # # Import os Finished  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # Upkeep Section Start  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def clean_data(dirty_line): # Only use is a cleaner output of information
  clean_line = str(dirty_line).replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace(", ", "\n").replace("'id'", "\n'id'")
  print(clean_line)

def keys_values(arg): # Return all keys and values for a given argument

#  count   = 0         # Defined variable   # 1st parameter for while loop
#  len_arg = len(arg)  # Length of argument # 2nd parameter for while loop
#  array = []

#  while count < len_arg: # While count is less then len_arg # Use count to iterate each key and its corresponding values
  try:    # For correctly formatted data
    arg_key   = arg.keys()
    arg_value = arg.values()
  except: # For improperly formatted data
    arg_key   = arg[0].keys()
    arg_value = arg[0].values()

  print(arg_key)
#  write_file('Data/User', arg_key, arg_value)
#    count += 1

# # # Upkeep Section Finish  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # Managing Funds # # # # # # # # # # # # # # # # # # # # # # Gdax & Coinbase # # #

def deposit_funds(auth_client, account_id, deposit_size): # Deposit from GDAX into Coinbase Wallet
  depositParams = {
          'amount': deposit_size,            # Currency is determined by the account specified
          'coinbase_account_id': account_id  # Id associated with specified wallet
  }
  auth_client.deposit(depositParams)

def withdraw_funds(auth_client, account_id, withdraw_size): # Withdraw from GDAX into Coinbase Wallet
  withdrawParams = {
          'amount': withdraw_size,            # Currency is determined by the account specified
          'coinbase_account_id': account_id   # Id associated with specified wallet
  }
  auth_client.withdraw(withdrawParams)

# # # Finished Managing Funds  # # # # # # # # # # # # # # # # # Gdax & Coinbase # # #
# # # LIVE TRADING START # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def buy_order(auth_client, exchange, buy_size, trigger):      # Buy 'some_amount' BTC @ 'some_price' USD
  auth_client.buy(price      = trigger,    # Price to buy at  # USD
                  size       = buy_size,   # Amount to buy    # BTC
                  product_id = exchange)   # Currency ID      # 'BTC-USD'

def sell_order(auth_client, exchange, sell_size, trigger):    # Sell 'some_amount' BTC @ 'some_price' USD
  auth_client.sell(price      = trigger,   # Price to sell at # USD
                   size       = sell_size, # Amount to sell   # BTC
                   product_id = exchange)  # Currency ID      # 'BTC-USD'

def cancel_all_orders(auth_client, exchange_type): # Cancel all existing orders on for all accounts # exchange_type references possible exchanges
  for trade in exchange_type:
    auth_client.cancel_all(product=trade)
    print('Cancel all open orders for ' + trade + ': Success')

# # # LIVE TRADING END # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #