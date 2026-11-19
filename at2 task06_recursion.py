"""Q6: Staircase count with naive recursion, memoisation and iteration."""

from functools import lru_cache
import sys
import time

naive_calls = 0
def ways_naive(n):
    global naive_calls
    naive_calls += 1
    if n <= 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)

memo_calls = 0
@lru_cache(maxsize=None)
def ways_memo(n):
    global memo_calls
    memo_calls += 1
    if n <= 1:
        return 1
    return ways_memo(n - 1) + ways_memo(n - 2)

def ways_loop(n):
    if n <= 1:
        return 1
    prev2, prev1 = 1, 1
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev1 + prev2
    return prev1

if __name__ == "__main__":
    print("Hand-check values:")
    for n in range(1, 7):
        print(n, ways_loop(n))
    print("\nCall counts:")
    for n in (10, 20, 25, 30):
        naive_calls = 0
        answer = ways_naive(n)
        print(f"naive n={n}: answer={answer}, calls={naive_calls}")
        ways_memo.cache_clear()
        memo_calls = 0
        answer2 = ways_memo(n)
        print(f"memo  n={n}: answer={answer2}, calls={memo_calls}")
    print("\nRecursion limit:", sys.getrecursionlimit())
    ways_memo.cache_clear()
    try:
        print("memo n=1000:", ways_memo(1000))
    except RecursionError as exc:
        print("memo n=1000 raised RecursionError:", exc)
    print("loop n=1000 digit count:", len(str(ways_loop(1000))))
