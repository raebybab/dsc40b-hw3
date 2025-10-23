def swap_sum(A, B):
    """
    Given two sorted integer arrays A and B, return indices (i, j) so that
    swapping A[i] and B[j] makes: sum(B) == sum(A) + 10.
    If none exists, return None. Runs in Θ(n).
    """
    sumA = sum(A)
    sumB = sum(B)
    numer = sumA - sumB + 10
    if numer % 2 != 0:
        return None
    diff = numer // 2

    i, j = 0, 0
    nA, nB = len(A), len(B)

    while i < nA and j < nB:
        cur = A[i] - B[j]
        if cur == diff:
            return (i, j)
        if cur < diff:
            i += 1
        else:
            j += 1

    return None