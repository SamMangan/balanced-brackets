from tests import run_balance_tests, run_is_balanced_tests
from is_balanced_solutions import string_solution, recursive_solution, stack_solution
from balance_solutions import balance

def main():
  # Tests for warm-up problem
  print('Running tests for warm up problem...')
  run_balance_tests(balance)
  print()
  
  # Tests for main problem
  print('Running tests for main problem...')
  run_is_balanced_tests(string_solution)
  run_is_balanced_tests(stack_solution)
  run_is_balanced_tests(recursive_solution)
  print()

  # Interactive Demo
  # line = input("Enter an expression to validate: ")
  # is_valid = stack_solution(line)
  # print(f"{line} is {'' if is_valid else 'not'} well formatted!")
  # print()

  # # Warmup excercise to complete valid expressions
  # # e.g. "[{<" gives ">}]"
  # line = input("Enter a line with brackets that need closing: ")
  # balance(line)
  # print()

main()