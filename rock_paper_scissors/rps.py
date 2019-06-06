#!/usr/bin/python

import sys
import math

def rock_paper_scissors(n):
  pool = ['rock', 'paper', 'scissors']
  choices = [0] * int(math.pow(len(pool), n))
  interator_arr = []
  for i in range(1, n + 1):
    interator_arr.append(int(math.pow(len(pool), i)))
  for j in range(len(choices)):
    choices[j] = [*interator_arr]
    for k in range(len(choices[j])):
      index = math.floor(j/int(interator_arr[len(interator_arr) - 1]/interator_arr[0]) * math.pow(interator_arr[0], k) + 0.000000001)
      choices[j][k] = pool[index % interator_arr[0]]
  return choices
    




if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')