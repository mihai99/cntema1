def run_addition():
    print("task 2")
    u = 1
    not_equal = True
    while not_equal:
        pre = pow(10, -u)
        a = 1.0
        b = pre / 10
        c = pre / 10
        not_equal = bool((a + b) + c == a + (b + c))
        u = u + 1
    return u
