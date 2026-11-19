"""Q7: Diagnose and redesign Q6 using memoisation and an iterative O(1)-space loop."""

from functools import lru_cache
import time

calls = 0
def original_naive(n):
    global calls
    calls += 1
    if n <= 1:
        return 1
    return original_naive(n - 1) + original_naive(n - 2)

memo_calls = 0
@lru_cache(maxsize=None)
def redesigned_memo(n):
    global memo_calls
    memo_calls += 1
    if n <= 1:
        return 1
    return redesigned_memo(n - 1) + redesigned_memo(n - 2)

def redesigned_loop(n):
    if n <= 1:
        return 1
    a = b = 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def timed(fn, n):
    start = time.perf_counter()
    result = fn(n)
    return result, time.perf_counter() - start

if __name__ == "__main__":
    n = 30
    calls = 0
    old, old_time = timed(original_naive, n)
    print(f"Original naive: n={n}, answer={old}, calls={calls}, time={old_time:.6f}s")
    redesigned_memo.cache_clear()
    memo_calls = 0
    new, memo_time = timed(redesigned_memo, n)
    print(f"Redesigned memo: n={n}, answer={new}, calls={memo_calls}, time={memo_time:.6f}s")
    loop, loop_time = timed(redesigned_loop, n)
    print(f"Redesigned loop: n={n}, answer={loop}, time={loop_time:.6f}s")
    print("All answers equal:", old == new == loop)
