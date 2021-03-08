import math


class Lib:
    def __init__(self):
        return

    """
        Checks a number whether it is prime or not
    """

    @staticmethod
    def isPrime(n: int) -> bool:
        if n == 1 or n == 0 or n % 2 == 0:
            return False

        limit = math.ceil(math.sqrt(n))
        for i in range(3, limit, 2):
            if n % i == 0:
                return False

        return True

    """
        Gets the next prime after a given parameter
    """
    @staticmethod
    def getPrime(n: int) -> int:
        if n % 2 == 0:
            n += 1

        while not Lib.isPrime(n):
            n += 2

        return n
