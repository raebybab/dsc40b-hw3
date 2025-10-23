def swap_sum(A, B):
    """
    Given two sorted integer arrays A and B,
    return a pair of indices (i, j) such that
    swapping A[i] and B[j] makes:
        sum(B) == sum(A) + 10
    If multiple pairs exist, return any one of them.
    If no such pair exists, return None.
    """

    sumA = sum(A)
    sumB = sum(B)
    diff = (sumB - sumA - 10) / 2

    i, j = 0, 0
    nA, nB = len(A), len(B)

    while i < nA and j < nB:
        current = A[i] - B[j]
        if current == diff:
            return (i, j)
        elif current < diff:
            i += 1
        else:
            j += 1

    return None