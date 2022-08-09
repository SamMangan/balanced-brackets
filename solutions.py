'''
This file contains our solutions
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

'''
1. String manipulation
'''
def string_solution(line):
  prev_length = None
  length = len(line)
  while prev_length is None or length < prev_length:
    prev_length = len(line)
    line = line.replace("()", "").replace("[]", "")\
               .replace("{}", "").replace("<>", "")
    length = len(line)
  return length == 0

'''
2. Stacks
'''
def stack_solution(line):
  stack = [] # back of list == "top" of stack
  for char in line:
    if len(stack) > 0:
      top = stack[-1] # peek at top of stack
      if matches(char, top):
        stack.pop() # pop from stack
        continue
    stack.append(char) # push to stack
  
  return len(stack) == 0

'''
3. Recursion (hard)
'''
def recursive_solution(line):

  def find_closing_index(opening_bracket, line):
    closing_index = 1
    opening_count = 1 # unclosed copies of opening_bracket seen so far 
    
    while closing_index < len(line):
      bracket = line[closing_index]
      if bracket == opening_bracket:
        opening_count += 1
      if matches(bracket, opening_bracket):
        opening_count -= 1
        if opening_count == 0:
          break
      closing_index += 1
      
    return closing_index

  
  length = len(line)

  if length == 0:
    return True # an empty string is balanced
  if length == 1:
    return False # a single bracket is unbalanced 
  if is_closing(line[0]):
    return False # a line beginning with a closing bracket is unbalanced

  closing_index = find_closing_index(line[0], line)

  if closing_index == length:
    # the opening bracket is never closed
    return False

  # substring between the matching brackets
  between = line[1:closing_index]
  # substring after the matching brackets
  after = line[closing_index+1:]
  return recursive_solution(between) and recursive_solution(after)
    
  
'''
Test Harness
'''
def is_balanced(line):
  print(line)
  return recursive_solution(line)