def run_is_balanced_tests(test_subject):
  # balanced
  assert test_subject("()"), "A single matching pair is balanced"
  assert test_subject("([{<>}])"), "Nested matching pairs are balanced"
  assert test_subject("()[]{}"), "Consecutive matching pairs are balanced"
  assert test_subject("5*(1+4)"), "Maths Expression is balanced"

  # unbalanced
  assert not test_subject("("), "A single bracket is unbalanced"
  assert not test_subject("(]"), "A mismatched pair is unbalanced"
  assert not test_subject("([)]"), "Interleaving brackets are unbalanced"
  assert not test_subject(
      ")("), "An 'inside-out' matching pair is unbalanced"
  assert not test_subject("5*(1+4"), "Maths Expression is unbalanced"

  print(f"[{test_subject.__name__}] Tests passed!")


def run_balance_tests(test_subject):
  # no brackets
  assert test_subject("") == "", "Balance an empty string"
  assert test_subject("5") == "5", "Balance an expression without brackets"

  # opening brackets only
  assert test_subject("(") == "()", "Balance a single opening bracket"
  assert test_subject("<<") == "<<>>", "Balance a sequence of identical opening brackets"
  assert test_subject("<{[(") == "<{[()]}>", "Balance a sequence of different opening brackets"
  assert test_subject("(2+[4x3") == "(2+[4x3])", "Balance Maths Expression starting with bracket"
  assert test_subject("5-(2+[4x3") == "5-(2+[4x3])", "Balance Maths Expression starting with non-bracket"

  # opening and closing brackets
  assert test_subject("[{}]<(") == "[{}]<()>", "Balance line starting with an already-balanced expression"
  assert test_subject("([{}]<(") == "([{}]<()>)", "Balance line containing an already-balanced expression"

  print(f"[{test_subject.__name__}] Tests passed!")