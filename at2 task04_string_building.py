"""Q4: Compare +=, list + join, and f-string line construction."""

import time
import statistics

def build_plus(parts):
    text = ""
    for p in parts:
        text += p + ";"
    return text

def build_join(parts):
    return "".join(p + ";" for p in parts)

def build_fstring(rows):
    # Each line is formatted with an f-string, then joined once.
    return "".join(f"{item};" for item in rows)

def measure(fn, parts, repeats=3):
    durations = []
    for _ in range(repeats):
        start = time.perf_counter()
        result = fn(parts)
        durations.append(time.perf_counter() - start)
    return statistics.mean(durations), result

if __name__ == "__main__":
    for n in (1_000, 10_000, 200_000):
        items = [f"Item{i}:Rs{i % 50}" for i in range(n)]
        t_plus, a = measure(build_plus, items)
        t_join, b = measure(build_join, items)
        t_f, c = measure(build_fstring, items)
        print(f"\nLines: {n:,} | equal: {a == b == c} | chars: {len(a)}")
        print(f"+= average: {t_plus:.6f}s | join: {t_join:.6f}s | f-string+join: {t_f:.6f}s")
