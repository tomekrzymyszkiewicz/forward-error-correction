  
import numpy as np
import random

from numpy.core.fromnumeric import size
from numpy.random import random_integers

class Channel:
    def __init__(self, bits_array):
        self.bits = bits_array

    def random_error(bits, intensity):          
        """generating mistakes randomly, number of mistakes depends of intensity parametr - proprtional to length of message
        """
        mistakes = len(bits)*intensity/100
        return Channel.random_error_number(bits, mistakes)
        
    
    def random_error_number(bits, mistakes):     
        """generating mistakes randomly, number of mistakes given by "mistakes"
        """
        index_array = np.arange(len(bits))
        np.random.shuffle(index_array)
        mistakes_array = index_array[0:mistakes]
        for i in mistakes_array:
            bits[i] = (bits[i]+1)%2
        return bits


#SECOND GROUP OF NOISE IN THIS GROUP MISTAKES HAPPEN EVERY COUPLE BITS 
    def random_noise(bits, space):                                 
        """generating single mistake averge every "space" in channel
        """
        i = 0
        while i < len(bits):
            corect = int(random.gauss(space, 1))
            bits[i] = (bits[i]+1)%2
            i = i + corect;
        return bits

    
    def group_noise(bits, space, averge_group_size):        
        """generating group of mistakes averge every "space" in channel, size of group averge "averge_group_size"
        """
        i = 0
        while i < len(bits):
            group = int(random.gauss(averge_group_size, 1))
            if (group < 0):
                group = 0;
            space = int(random.gauss(space, 1))
            if (space < 0):
                space = 0

            for x in range(0, group):
                if (i + x >= len(bits)):
                    return bits
                bits[i + x] = (bits[i + x]+1)%2
            i = i + group + space;
        return bits

    def group_noise_signal(bits, space, averge_group_size):      
        """generating group of signal 0/1 averge every "space" in channel, size of group averge "averge_group_size"
        """
        i = 0
        while i < len(bits):
            group = int(random.gauss(averge_group_size, 1))
            if (group < 0):
                group = 0;
            space = int(random.gauss(space, 1))
            if (space < 0):
                space = 0

            signal = int(random.randint(0, 1))
            for x in range(0, group):
                if (i + x >= len(bits)):
                    return bits
                bits[i + x] = signal
            i = i + group + space;
        return bits

