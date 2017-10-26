# Name       : Shawn McCrum
# Date       : 2017/10/26
# Description: Create a flexible and organized environment. This file contains the most basic of actions.
import os


# # # Import os section # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# Create a project folder for project
def create_project_dir(directory):
  if not os.path.exists(directory):
    os.makedirs(directory)
  else:
    return (os.path.getmtime(directory))
#    print(os.path.getmtime(directory)) # When was file last updated
#    print(directory, 'already exists')
    pass

# Save parsed data to file
def save_project(file_location, row_data):
  if not os.path.isfile(file_location):
    row_data.to_csv(file_location)
  else:
    pass

# Create a new file
def write_file(path, data):
  with open(path, 'wb') as f:
    f.write(data)

# Add data onto an existing file
def append_to_file(path, data):
  with open(path, 'a') as file:
    file.write(data + '\n')

    
# # # Import os Finished  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # Upkeep Section Start  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# Only use is a cleaner output of information
def clean_data(dirty_line):
  clean_line = str(dirty_line).replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace(", ", "\n").replace("'id'", "\n'id'")
  print(clean_line) # Return only the last result

# Return all keys and values for a given argument
def keys_values(arg):
  count   = 0            # Defined variable   # 1st parameter for while loop
  len_arg = len(arg)     # Length of argument # 2nd parameter for while loop
  array = []

  while count < len_arg: # While count is less then len_arg # Use count to iterate each key and its corresponding values
    try:                 # For correctly formatted data
      arg_key   = [_ for _ in arg.keys()][count]
      arg_value = [_ for _ in arg.values()][count]
    except:              # For improperly formatted data
      arg_key   = [_ for _ in arg[0].keys()][count]
      arg_value = [_ for _ in arg[0].values()][count]

    print(arg_key, arg_value)
    count += 1


# # # Upkeep Section Finish  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # Managing Funds # # # # # # # # # # # # # # # # # # # # # # Gdax & Coinbase # # #


# Deposit from GDAX into Coinbase Wallet
def deposit_funds(auth_client, account_id, deposit_size):
  depositParams = {
          'amount': deposit_size,             # Currency is determined by the account specified
          'coinbase_account_id': account_id
  }
  auth_client.deposit(depositParams)


# Withdraw from GDAX into Coinbase Wallet
def withdraw_funds(auth_client, account_id, withdraw_size):
  withdrawParams = {
          'amount': withdraw_size,            # Currency is determined by the account specified
          'coinbase_account_id': account_id
  }
  auth_client.withdraw(withdrawParams)

  
# # # Finished Managing Funds  # # # # # # # # # # # # # # # # # Gdax & Coinbase # # #
# # # LIVE TRADING START # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# Buy 'some_amount' BTC @ 'some_price' USD
def buy_order(auth_client, exchange, buy_size, trigger):
  auth_client.buy(price      = trigger,    # Price to buy at  # USD
                  size       = buy_size,   # Amount to buy    # BTC
                  product_id = exchange)   # Currency ID      # 'BTC-USD'


# Sell 'some_amount' BTC @ 'some_price' USD
def sell_order(auth_client, exchange, sell_size, trigger):
  auth_client.sell(price      = trigger,   # Price to sell at # USD
                   size       = sell_size, # Amount to sell   # BTC
                   product_id = exchange)  # Currency ID      # 'BTC-USD'


# Cancel all existing orders on for all accounts # exchange_type references possible exchanges
def cancel_all_orders(auth_client, exchange_type):
  for trade in exchange_type:
    auth_client.cancel_all(product=trade)
    print('Cancel all open orders for ' + trade + ': Success')

    
# # # LIVE TRADING END # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
