#!/usr/bin/python

import argparse


def find_max_profit(prices):
  max_profit = 0
  for i in range(0, len(prices)):
    cur_arr = prices[0:i]
    if max_profit == 0 and len(prices) - 1 == i:
      max_profit = prices[i] - prices[i - 1]
    if not not cur_arr:
      if prices[i] - min(cur_arr) > max_profit:
        max_profit = prices[i] - min(cur_arr)
  return max_profit
  

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))