# Diamond Pattern
#   *
#  ***
# *****
#  ***
#   *

def print_diamond(N):
    n = N
    num_spaces = n // 2

    for r in range(0, n):
        val = ""
        for c in range(0, num_spaces):
            val += " "
        for st in range(0, n - (2 * num_spaces)):
            val += "*"

        # print(val, num_spaces, r)
        print(val)

        if r >= n // 2:
            num_spaces += 1
        else:
            num_spaces -= 1


if __name__ == '__main__':
    print_diamond(5)
    print_diamond(7)
    print_diamond(9)
    print_diamond(11)
