def all_sums(total:int, summands:int, max_summand:int) -> int:
    """List all representations of integer total
         as a sum of summands summands,
         with each summand being at most max_summand.
       Each representation is a non-ascending summands-tuple.
       The list of representations is sorted in reversed order.
    """
    if not 0 <= total <= max_summand*summands: return []
    if total == 0: return [(0,)*summands]
    return [(max_summand,)+s for s in all_sums(total-max_summand, summands-1, max_summand)] \
           + all_sums(total, summands, max_summand-1)

def success_probability(n:int, d:int) -> float:
    """Return E[share of a most frequent component
                in a vector sampled uniformly from N_d^n]
    """
    factorial = [1]
    for k in range(max(n,d)):
        factorial.append(factorial[-1] * (k+1))
    result = 0
    for s in all_sums(n, d, n):
        number_of_cases = factorial[n] * factorial[d]
        histogram = [0] * (n+1)
        for summand in s:
            number_of_cases //= factorial[summand]
            histogram[summand] += 1
        for count in histogram:
            number_of_cases //= factorial[count]
        result += s[0] * number_of_cases
    return float(result) / d**n / n

print(success_probability(40, 5))