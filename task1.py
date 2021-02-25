def run():
    print("task 1")
    u = 1
    not_equal = True
    while not_equal:
        result = 1.0 + pow(10, -u)
        not_equal = bool(result != 1.0)
        u = u+1
    print("Precizia masina: ", u)
    return u
