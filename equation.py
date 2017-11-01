# Name       : Shawn McCrum
# Date       : 2017/10/28
# Description: File specifically for mathematical equations
import statistics

def mean(array):
  try:
    a_mean   = statistics.mean(map(float, array))
    a_median = statistics.median(map(float, array))
    a_mode   = statistics.mode(map(float, array))
    print('Size  :', len(array), '\nMean  :', a_mean, '\nMedian:', a_median, '\nMode  :', a_mode)

  except:
    x = sum(map(float, array)) / len(array)
    print(len(array), 'common value @', x)
    pass

#def user_wallet(account_currency, account_hold, account_balance):
#  balance  = float(account_balance)
#  min_move = .01 # 1 cent # 1%
#
#  if min_move < balance:
#    percent_roi = min_move * balance
#    print(account_currency, percent_roi)