from tests import run_tests
from solutions import string_solution, recursive_solution, stack_solution
from balance import balance

def main():
    run_tests(string_solution)
    run_tests(stack_solution)
    run_tests(recursive_solution)

    # Interactive Demo
    line = input("Enter an expression to validate: ")
    is_valid = stack_solution(line)
    print(f"{line} is {'' if is_valid else 'not'} well formatted!")

    # Warmup excercise to complete valid expressions
    # e.g. "[{<" gives ">}]"
    line = input("Enter a line with brackets that need closing: ")
    balance(line)

main()