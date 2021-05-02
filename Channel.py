import numpy as np
import random

from numpy.core.fromnumeric import size

class Channel:
    def __init__(self, bits_array):
        self.bits = bits_array

#FIRST GROUP OF NOISE IN THIS GROUP MISTAKES CAN OVERLAP SO IN RESULT CAN BE LESS AMOUNT OF MISTAKES
    def random_error(self, intensity):          #generating mistakes randomly, number of mistakes depends of intensity parametr - proprtional to length of message
        mistakes = len(self.bits)*intensity/100
        #mieszanie tablicy i  wybór n pierwszych elementów (losowanie bez powtórzeń)
        for i in range(0, mistakes):
            n = random.randint(0, len(self.bits) - 1) 
            if self.bits[n] == 0:
                self.bits[n] = 1
            else:
                 self.bits[n] = 0
        return str(self.bits)
    
    def random_error_number(self, mistakes):     #generating mistakes randomly, number of mistakes given by "mistakes"
        index_array = np.arange(len(self.bits))
        np.random.shuffle(index_array)
        mistakes_array = index_array[0:mistakes]
        for i in mistakes_array:
            self.bits[i] = (self.bits[i]+1)%2
        return self.bits

    def group_error(self, intensity):            #generating mistakes in groups, number of mistakes depends of "intensity" parametr - proprtional to length of message
        mistakes = len(self.bits)*intensity/100  #random size and number of groups
        while mistakes > 0:
            group_size = random.randint(1, mistakes)
            n = random.randint(0, len(self.bits) - 1)

            for i in range(n, n + group_size):
                if i > len(self.bits) - 1:
                    break

                if self.bits[n] == 0:
                    self.bits[n] = 1
                else:
                    self.bits[n] = 0

                mistakes -= 1
        return str(self.bits)

    def group_error_number(self, mistakes):      #generating mistakes in groups, number of mistakes given by "mistakes"
        while mistakes > 0:                      #random size and number of groups
            group_size = random.randint(1, mistakes)
            n = random.randint(0, len(self.bits) - 1)
            
            for i in range(n, n + group_size):
                if i > len(self.bits) - 1:
                    break

                if self.bits[n] == 0:
                    self.bits[n] = 1
                else:
                    self.bits[n] = 0

                mistakes -= 1
        return str(self.bits)


#SECOND GROUP OF NOISE IN THIS GROUP MISTAKES HAPPEN EVERY COUPLE BITS, DON'T OVERLAP 
    def random_noise(self, space):              #generating single mistake averge every "space" in channel
        pass
    
    def group_noise(self, space, size):         #generating group of mistakes averge every "number" in channel, size of group averge "size"
        pass


