from fibonacci import fib_memo, fib_fast_doubling

def test_fib_memo_small():
    assert fib_memo(0) == 0
    assert fib_memo(1) == 1
    assert fib_memo(10) == 55

def test_fib_fast_doubling_small():
    assert fib_fast_doubling(0) == 0
    assert fib_fast_doubling(1) == 1
    assert fib_fast_doubling(10) == 55

def test_fib_equivalence():
    for n in [0, 1, 5, 20, 100, 1000]:
        assert fib_memo(n) == fib_fast_doubling(n)

