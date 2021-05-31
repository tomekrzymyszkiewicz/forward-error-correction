from random import seed
from random import randint

class Generator:
    def generate_bits(bits_number):
        bits = []
        for x in range(0, bits_number):
            value = randint(0, 1)
            bits.append(value)
        print(bits)
        return bits

