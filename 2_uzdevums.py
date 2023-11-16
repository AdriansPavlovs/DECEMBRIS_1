def find_first_square_over_1000():
    num = 1
    while num**2 <= 1000:
        num += 1
    return num