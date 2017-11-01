# Name       : Shawn McCrum
# Date       : 2017/10/18
# Description: GDAX API -- connect to the users account and wallets using the generated API key on the GDAX website.
import gdax
from general import *

# Account Connection
def access_account(fld):

  usr_file = fld + 'user.txt'     # Create file name/path
  append_to_file(usr_file, fld)   # Append creates file if it doesn't exist or appends to existing file

  # Required information for Gdax login
  KEY       = ''
  BASE      = ''
  PHRASE    = ''
  client    = gdax.AuthenticatedClient(KEY, BASE, PHRASE) # Sandbox mode (requires unique api credentials): api_url="https://api-public.sandbox.gdax.com"
  login     = [_ for _ in client.get_accounts()]

  for account in login:
    keys_values(account)
