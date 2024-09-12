def new_format(string):

    string = list(string)
    for i in range(len(string) - 3, 0, -3):
        string.insert(i, ".")
    return "".join(string)

assert (new_format("1000000") == "1.000.000")
assert (new_format("100") == "100")
assert (new_format("1000") == "1.000")
assert (new_format("100000") == "100.000")
assert (new_format("10000") == "10.000")
assert (new_format("0") == "0")
