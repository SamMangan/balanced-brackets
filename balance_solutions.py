'''
WARMUP
This file contains our solutions to the warm-up problem:

Read in a line with any number of opening brackets in any order. It may also contain closing brackets, provided the line could potentially be made valid (e.g. [](< is okay, but [(]< is not).
Close any brackets necessary to balance the line, and return the full balanced line.

We assume that the input string can be balanced.
'''


OPEN_TO_CLOSE = {
  "(" : ")",
  "[" : "]",
  "{" : "}",
  "<" : ">",
}

def balance(line):
  closed_brackets = ""
  for char in reversed(line):
    if char in OPEN_TO_CLOSE:
      closed_brackets += OPEN_TO_CLOSE[char]
  return line + closed_brackets
