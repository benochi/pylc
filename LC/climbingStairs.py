# bottom up dynamic approach O(n)
def climbStairs(n):
    # set variables for amount of options, stairs 1 or 2 steps only
    one, two = 1, 1
    # we only want to iterate n-1 times.
    for i in range(n - 1):
        # store one value
        temp = one
        # increment one
        one = one + two
        # set two after addition to new value of one.
        two = temp

    # return total options.
    return one


print(climbStairs(5))
