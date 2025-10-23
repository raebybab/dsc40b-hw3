def histogram(points, bins):
    """
    Given:
      points: sorted list of n numbers
      bins:   sorted list of k tuples (a, b) defining bins [a, b)

    Returns:
      list of densities for each bin.
      Density = (# points in bin) / (n * (b - a))
    """

    n = len(points)
    densities = []
    i = 0  # pointer for points

    for (a, b) in bins:
        count = 0
        # move pointer forward while points fall inside current bin
        while i < n and points[i] < b:
            if points[i] >= a:
                count += 1
            i += 1
        width = b - a
        densities.append(count / (n * width))

    return densities