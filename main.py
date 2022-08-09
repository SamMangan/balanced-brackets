from tests import run_tests
from balance import balance

if __name__ == "__main__":
  run_tests()
  line = input("Enter a line with brackets that need closing: ") 
  balance(line)