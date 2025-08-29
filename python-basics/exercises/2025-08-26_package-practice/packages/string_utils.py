def most_occurred_char(s: str):
    """
    Returns the most occurred character and its frequency in a string.
    """
    if not s:
        return None, 0

    freq = {}
    for char in s:
        if char != " ":
            freq[char] = freq.get(char, 0) + 1
    most_char = max(freq, key=freq.get)
    return most_char, freq[most_char]