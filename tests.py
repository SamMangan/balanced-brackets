from solutions import is_balanced


def run_tests():
  assert is_balanced("()"), "A single matching pair is balanced"
  assert is_balanced("([{<>}])"), "Nested matching pairs are balanced"
  assert is_balanced("()[]{}"), "Consecutive matching pairs are balanced"
  
  assert not is_balanced("("), "A single bracket is unbalanced"
  assert not is_balanced("(]"), "A mismatched pair is unbalanced"
  assert not is_balanced("([)]"), "Interleaving brackets are unbalanced"
  assert not is_balanced(")("), "An 'inside-out' matching pair is unbalanced"

  print("Tests passed!")