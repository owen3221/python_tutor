# ========== Exercise 1 (basic): sum_list_for ==========
def sum_list_for(nums: list[int]) -> int:
    """Return the sum of nums using a for-loop (don't use built-in sum)."""
    # TODO
    sum = 0
    for i in nums:
        sum += i
    return sum
    raise NotImplementedError


# ========== Exercise 2 (basic): index_value_pairs ==========
def index_value_pairs(lst: list) -> list[tuple[int, object]]:
    """Return [(index, value), ...] using for + range(len(lst))."""
    # TODO
    
    raise NotImplementedError


# ========== Exercise 3 (basic): count_vowels ==========
def count_vowels(s: str) -> int:
    """Return # of vowels in s (a e i o u, case-insensitive)."""
    # TODO
    raise NotImplementedError


# ========== Exercise 4 (dict + loop) ==========
def char_frequency(text: str) -> dict[str, int]:
    """Return {char: count} using a dict and a loop (use d[c] = d.get(c,0)+1)."""
    # TODO
    raise NotImplementedError


# ========== Exercise 5 (slightly advanced): centered_pyramid ==========
def centered_pyramid(rows: int, ch: str = "*") -> list[str]:
    """
    Return a centered pyramid (list of lines) using string * int.
    rows=4 -> ["   *","  ***"," *****","*******"]
    Hint: spaces = " "*(rows-i), stars = ch*(2*i-1)
    """
    # TODO
    raise NotImplementedError


# ========== Exercise 6 (while + search) ==========
def first_over_threshold_while(nums: list[int], threshold: int) -> tuple[int | None, int]:
    """
    Using a while-loop, return (value, index) of first element > threshold.
    If none, return (None, -1).
    """
    # TODO
    raise NotImplementedError


# ========== Minimal test harness ==========
def _expect(name: str, got, expected):
    ok = (got == expected)
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        print(" expected:", expected, "\n got     :", got)

def main():
    # Only small, direct tests—kept short and readable.
    try:
        _expect("sum_list_for", sum_list_for([1,2,3,4]), 10)
    except NotImplementedError:
        print("SKIP sum_list_for (NotImplemented)")

    try:
        _expect("index_value_pairs", index_value_pairs(["a","b","c"]),
                [(0,"a"),(1,"b"),(2,"c")])
    except NotImplementedError:
        print("SKIP index_value_pairs (NotImplemented)")

    try:
        _expect("count_vowels", count_vowels("Programming"), 3)  # o, a, i
    except NotImplementedError:
        print("SKIP count_vowels (NotImplemented)")

    try:
        _expect("char_frequency", char_frequency("banana"), {"b":1,"a":3,"n":2})
    except NotImplementedError:
        print("SKIP char_frequency (NotImplemented)")

    try:
        _expect("centered_pyramid",
                centered_pyramid(4, "*"),
                ["   *","  ***"," *****","*******"])
    except NotImplementedError:
        print("SKIP centered_pyramid (NotImplemented)")

    try:
        _expect("first_over_threshold_while #1",
                first_over_threshold_while([3,7,2,9], 8), (9,3))
        _expect("first_over_threshold_while #2",
                first_over_threshold_while([1,2,3], 10), (None,-1))
    except NotImplementedError:
        print("SKIP first_over_threshold_while (NotImplemented)")

if __name__ == "__main__":
    main()

