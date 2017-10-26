# Name       : Shawn McCrum
# Date       : 2017/10/26
# Description: File specifically for mathematical equations
import statistics

def mean(array):
  try:
    a_mean   = statistics.mean(map(float, array))
    a_median = statistics.median(map(float, array))
    a_mode   = statistics.mode(map(float, array))
    print('Size  :', len(array), '\nMean  :', a_mean, '\nMedian:', a_median, '\nMode  :', a_mode)
  except:
    print('Common Value:', float(array[0]))
    pass