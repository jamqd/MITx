from itertools import combinations, chain

def powerSet(items):
    return chain.from_iterable(combinations(items, r) for r in range(len(items) + 1))

