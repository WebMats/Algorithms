#!/usr/bin/python

import sys

def making_change(amount, denominations = [1, 5, 10, 25, 50]):
  den_in_play = [num for num in denominations if num <= amount ]
  ways = [0] * (amount + 1)
  ways[0] = 1
  for coin in den_in_play:
    for i in range(coin, len(ways)):
      owed = i - coin
      ways[i] += ways[owed]
  return ways[amount]




if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")