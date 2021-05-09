from bitarray import bitarray
from random import randint


class Filter:
    def __init__(self, size, values_count):
        self._size = size
        self._functions_count = 10  # todo

        self._generate_hash_functions()
        self._bits = bitarray(self._size)

    def _generate_hash_functions(self):
        self._hash_functions = []
        self._rand_values = []

        for i in range(self._functions_count):
            rand_value = randint(0, 99)
            self._rand_values.append(rand_value)

            def hash_function(string, k):
                s = 0
                v = self._rand_values[k]
                for c in range(len(string)):
                    s += ord(string[c])
                return (s + v) % self._size
            self._hash_functions.append(hash_function)

    def _get_hash_value(self, string, k):
        print(self._hash_functions[k](string, k))
        return self._hash_functions[k](string, k)

    def add(self, values):
        for i in range(len(values)):
            string = values[i]
            print(string)
            for k in range(self._functions_count):
                self._bits[self._get_hash_value(string, k)] = 1

    def exists(self, string):
        for k in range(self._functions_count):
            index = self._get_hash_value(string, k)
            if self._bits[index] == 0:
                return False
        return True

