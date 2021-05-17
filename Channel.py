import numpy as np
import random

from numpy.core.fromnumeric import size

class Channel:
    def __init__(self, bits_array):
        self.bits = bits_array

    def random_error(self,intensity):          
        """generating mistakes randomly, number of mistakes depends of intensity parametr - proprtional to length of message
        """
        mistakes = len(self.bits)*intensity/100
        return Channel.random_error_number(self.bits, mistakes)
        
    
    def random_error_number(self, mistakes):     
        """generating mistakes randomly, number of mistakes given by "mistakes"
        """
        index_array = np.arange(len(self.bits))
        np.random.shuffle(index_array)
        mistakes_array = index_array[0:mistakes]
        for i in mistakes_array:
            self.bits[i] = (self.bits[i]+1)%2
        return self.bits


#SECOND GROUP OF NOISE IN THIS GROUP MISTAKES HAPPEN EVERY COUPLE BITS 
    def random_noise(self,space):                                 
        """generating single mistake averge every "space" in channel
        """
        while i < len(self.bits):
            corect = group = random.gauss(space, 1)
            self.bits[i] = (self.bits[i]+1)%2
            i = i + corect;
        return self.bits

    
    def group_noise(self,space, averge_group_size):        
        """generating group of mistakes averge every "space" in channel, size of group averge "averge_group_size"
        """
        group = random.gauss(averge_group_size, 1)
        while i < len(self.bits):
            corect = group = random.gauss(space, 1)
            for x in range(0, group):
                self.bits[x] = (self.bits[x]+1)%2
            i = i + group + corect;
        return self.bits

    def group_noise_signal(self,space, averge_group_size):      
        """generating group of signal 0/1 averge every "space" in channel, size of group averge "averge_group_size"
        """
        group = random.gauss(averge_group_size, 1)
        while i < len(self.bits):
            corect = group = random.gauss(space, 1)
            signal = random.randint(0, 1)
            for x in range(0, group):
                self.bits[x] = signal
            i = i + group + corect;
        return self.bits


