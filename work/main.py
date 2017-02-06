def is_prime(number):
    for number in range(1, 8):
        for x in range(2, number):
            if number % x == 0:
                return False

    return True
