def run_tests(test_subject):
    assert test_subject("()"), "A single matching pair is balanced"
    assert test_subject("([{<>}])"), "Nested matching pairs are balanced"
    assert test_subject("()[]{}"), "Consecutive matching pairs are balanced"
    assert test_subject("5*(1+4)"), "Maths Expression is balanced"

    assert not test_subject("("), "A single bracket is unbalanced"
    assert not test_subject("(]"), "A mismatched pair is unbalanced"
    assert not test_subject("([)]"), "Interleaving brackets are unbalanced"
    assert not test_subject(
        ")("), "An 'inside-out' matching pair is unbalanced"
    assert not test_subject("5*(1+4"), "Maths Expression is unbalanced"

    print(f"[{test_subject.__name__}] Tests passed!")
