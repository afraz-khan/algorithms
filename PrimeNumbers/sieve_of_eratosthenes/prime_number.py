from sieve_of_eratosthenes import SieveOfEratosthenes
import sys


class PrimeNumber:
    """
    It provides the methods to work with Prime Numbers. All methods are implemented using the
    "Sieve of Eratosthenes" algorithm.
    """

    @staticmethod
    def find_number(position):
        """
        Returns the Prime number at the input position.

        :param position: Should be a positive integer value.
        :return: A Prime number.
        """
        if position < 1:
            raise Exception('Invalid Position')

        primes = SieveOfEratosthenes.get_numbers()

        return primes[position - 1]

    @staticmethod
    def find_position(num):
        """
        Returns the position of a Prime number in Prime number sequence.

        :param num: Prime number.
        :return: Prime number position.
        """
        if not (1 < num <= sys.maxsize):
            raise Exception('Invalid Number')

        positions = SieveOfEratosthenes.get_positions()

        return positions[num]
