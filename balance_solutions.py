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

def matches(closing, opening):
  return opening in OPEN_TO_CLOSE and closing == OPEN_TO_CLOSE[opening]
  
def is_closing(bracket):
  return bracket in OPEN_TO_CLOSE.values()

def balance(line):
  
  closed_brackets = ""
  wait_to_open = None # closing bracket which we're waiting for the opening match of
  
  for char in reversed(line):
    
    if wait_to_open:
      # ignore everything until we find what we're waiting for
      if matches(wait_to_open, char):
        # RESUME adding closing brackets
        wait_to_open = None 
      
    elif is_closing(char):
      # line is assumed balance-able, so we know that everything between this char
      # and its opening match is already balanced, so we PAUSE adding closing brackets
      wait_to_open = char
      
    elif char in OPEN_TO_CLOSE:
      closed_brackets += OPEN_TO_CLOSE[char]
      
  return line + closed_brackets