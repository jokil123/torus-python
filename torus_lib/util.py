def remap(low1, high1, low2, high2, value):
    return low2 + (value - low1) * (high2 - low2) / (high1 - low1)


def clamp(min_v, max_v, value):
    return max(min_v, min(max_v, value))
