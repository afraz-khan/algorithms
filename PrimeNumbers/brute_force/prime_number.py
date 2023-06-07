import sys


class PrimeNumber:
    """
    It provides the methods to work with Prime Numbers.
    All methods are implemented using Brute Force algorithms.
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

        num = 2
        position_counter = 1

        while position_counter < position:
            num += 1
            if PrimeNumber.is_prime(num):
                position_counter += 1

        return num

    @staticmethod
    def find_position(num):
        """
        Returns the position of a Prime number in Prime number sequence.

        :param num: Prime number.
        :return: Prime number position.
        """
        if not (1 < num <= sys.maxsize):
            raise Exception('Invalid Number')

        i = current_prime_num = 2
        position_counter = 1

        while i < num:
            i += 1
            if PrimeNumber.is_prime(i):
                current_prime_num = i
                position_counter += 1

        if current_prime_num != num:
            raise Exception('Invalid Number')

        return position_counter

    @staticmethod
    def is_prime(num):
        """
        Verifies if a number is prime or not.

        :param num: A positive integer.
        :return: Boolean, True or False
        """
        if num < 2:
            raise Exception('Invalid Number')

        for i in range(2, num):
            if num % i == 0:
                return False
        return True
