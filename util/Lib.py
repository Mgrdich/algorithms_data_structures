import math


class Lib:
    def __init__(self):
        return

    @staticmethod
    def isPrime(n) -> bool:
        if n == 1 or n == 0 or n % 2 == 0:
            return False

        limit = math.ceil(math.sqrt(n))
        for i in range(3, limit, 2):
            if n % i == 0:
                return False

        return True

