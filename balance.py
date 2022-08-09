# Read in a line with any number of opening brackets (, [, {, <; in any order.
# Print out the second half of the line that properly closes every bracket.

OPEN_TO_CLOSE = {
  "(" : ")",
  "[" : "]",
  "{" : "}",
  "<" : ">",
}

def balance(line):
  closed_brackets = ""
  for char in reversed(line):
    if char in OPEN_TO_CLOSE.values():
      break
    if char in OPEN_TO_CLOSE:
      closed_brackets += OPEN_TO_CLOSE[char]
  print(line + closed_brackets)
