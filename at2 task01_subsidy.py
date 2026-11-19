"""Q1: Electricity subsidy decisions using separate ifs and if-elif-else."""

def separate_if(units, ration_card, senior_above_80):
    results = []
    if units <= 100:
        results.append("FULL subsidy")
    if 101 <= units <= 200 and ration_card:
        results.append("PARTIAL subsidy")
    if units > 200 and senior_above_80:
        results.append("EXCEPTION subsidy")
    if not results:
        results.append("NO subsidy")
    return " + ".join(results)

def chained(units, ration_card, senior_above_80):
    if units <= 100:
        return "FULL subsidy"
    elif 101 <= units <= 200:
        if ration_card:
            return "PARTIAL subsidy"
        else:
            return "NO subsidy"
    elif units > 200:
        if senior_above_80:
            return "EXCEPTION subsidy"
        else:
            return "NO subsidy"

def match_case(units, ration_card, senior_above_80):
    # Guarded match cases require Python 3.10+.
    match units:
        case x if x <= 100:
            return "FULL subsidy"
        case x if 101 <= x <= 200 and ration_card:
            return "PARTIAL subsidy"
        case x if 101 <= x <= 200:
            return "NO subsidy"
        case x if x > 200 and senior_above_80:
            return "EXCEPTION subsidy"
        case _:
            return "NO subsidy"

def lookup_loop(units, ration_card, senior_above_80):
    slabs = [(100, "FULL subsidy"), (200, "CHECK CARD"), (float("inf"), "CHECK SENIOR")]
    for upper, decision in slabs:
        if units <= upper:
            if decision == "CHECK CARD":
                return "PARTIAL subsidy" if ration_card else "NO subsidy"
            if decision == "CHECK SENIOR":
                return "EXCEPTION subsidy" if senior_above_80 else "NO subsidy"
            return decision

if __name__ == "__main__":
    households = [
        ("H1", 99, False, False), ("H2", 100, False, False),
        ("H3", 101, True, False), ("H4", 150, False, False),
        ("H5", 200, True, False), ("H6", 201, False, True),
        ("H7", 201, False, False), ("H8", 80, True, True)
    ]
    print("Household | Units | Card | Age>80 | Separate-if | if-elif-else")
    for name, units, card, senior in households:
        print(f"{name:9} | {units:5} | {str(card):4} | {str(senior):6} | "
              f"{separate_if(units, card, senior):15} | {chained(units, card, senior)}")
    print("\nBoundary checks (100, 101, 200, 201):")
    for u in (100, 101, 200, 201):
        print(u, "=>", chained(u, True, u == 201))
