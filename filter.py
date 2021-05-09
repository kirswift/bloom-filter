from bitarray import bitarray
from random import randint
import math


class Filter:
    def __init__(self, size, values_count):
        self._size = size
        self._bits = bitarray(self._size)
        self._functions_count = round((size / values_count) * math.log(2))
        self._generate_hash_functions()

    def _generate_hash_functions(self):
        self._hash_functions = []
        self._rand_values = []

        for i in range(self._functions_count):
            rand_value = randint(0, 999)
            self._rand_values.append(rand_value)
            self._hash_functions.append(lambda string, k: (hash(string) + self._rand_values[k]) % self._size)

    def _get_hash_value(self, string, k):
        return self._hash_functions[k](string, k)

    def add(self, values):
        for i in range(len(values)):
            string = values[i]
            for k in range(self._functions_count):
                self._bits[self._get_hash_value(string, k)] = 1

    def exists(self, string):
        for k in range(self._functions_count):
            index = self._get_hash_value(string, k)
            if self._bits[index] == 0:
                return False
        return True

