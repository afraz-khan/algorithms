"""
This represents the upper limit for calculating prime numbers.
"""
MAX: int = 1000000


class SieveOfEratosthenes:
    """
    This provides the methods to find the prime numbers and their positions using the
    "Sieve of Eratosthenes" algorithm.

    - Make sure to set up the max number allowed as per your machine resources(1M is supposed to be standard).
    """

    @staticmethod
    def get_numbers(num=None):
        """
        Prepares a list of all prime numbers less than or equal to a given number.

        - TIME: O(nlog(log(n))) https://www.geeksforgeeks.org/how-is-the-time-complexity-of-sieve-of-eratosthenes-is-nloglogn/

        - SPACE:O(n)
        https://www.geeksforgeeks.org/sieve-of-eratosthenes/

        :param num: This integer value serves as a basis for computing prime numbers up to a
            certain limit.
        :return: List of Prime numbers.
        """
        limit = SieveOfEratosthenes.__check_limit(num)
        primes = [True for _ in range(limit + 1)]
        p = 2
        while p*p <= limit:
            if primes[p]:
                # Update all multiples of p that are greater than or equal to p square.
                for i in range(p*p, limit+1, p):
                    primes[i] = False
            p += 1
        return [p for p in range(2, limit+1) if primes[p]]

    @staticmethod
    def get_positions(num=None):
        """
        Prepares a list of prime number positions.

        - TIME: O(nlog(n))
        - SPACE:O(n)
        https://www.geeksforgeeks.org/find-the-position-of-the-given-prime-number/

        :param num: This integer value serves as a basis for computing prime number positions
             up to a certain limit.
        :return: List of Prime number positions.
        """
        limit = SieveOfEratosthenes.__check_limit(num)
        prime_positions = [0] * (limit+1)
        position = 0

        # '0' & '1' are not prime numbers
        prime_positions[0] = -1
        prime_positions[1] = -1

        for i in range(2, limit+1):
            if prime_positions[i] == 0:
                position += 1
                prime_positions[i] = position
                for j in range(i*2, limit+1, i):
                    prime_positions[j] = -1

        return prime_positions

    @staticmethod
    def __check_limit(num=None):
        if num:
            if num > MAX:
                raise Exception('Number is too big.')
            return num
        return MAX
