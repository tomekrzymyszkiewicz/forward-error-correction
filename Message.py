from PIL import Image
import numpy as np
from functools import reduce
from operator import xor

test_image_file_name = "test_image.jpeg"
saved_test_image = "save_image.jpeg"

class Image_message:
    def __init__(self,file_name):
        """Load data from file and get size and pixel data (as 'image_bits')
        """
        try:
            image  = Image.open(file_name)
        except IOError:
            print("Image loading error")
        self.size = image.size
        pixels = np.asarray(image, dtype=np.uint8)
        self.image_bits = np.unpackbits(pixels)

    def save(self,file_name):
        """Save image to file with current pixel data (as 'image_bits')
        """
        packed_bits = np.packbits(self.image_bits)
        packed_bits_reshaped = np.reshape(packed_bits,(self.size[1],self.size[0],3))
        image = Image.fromarray(packed_bits_reshaped)
        image.save(file_name)

    def bits_trippling(self):
        """Function which return trippled bits of image pixels
        """
        #spróbować abcabcabc
        trippled_binary_image_bits = np.array((self.image_bits,self.image_bits,self.image_bits))
        trippled_binary_image_bits = np.reshape(trippled_binary_image_bits,3*len(self.image_bits),order='F')
        return trippled_binary_image_bits
        
    def decode_trippled_bits(self, trippled_binary_array):
            """Function that decodes trippled binary
            """
            separated_binary_array = np.reshape(trippled_binary_array,(3,-1),order='F')
            first = np.array(separated_binary_array[0])
            second = np.array(separated_binary_array[1])
            third = np.array(separated_binary_array[2])
            decoded_binary_image_bits = np.zeros(len(self.image_bits),dtype=np.uint8)
            for i in range(0, len(self.image_bits)):
                if(first[i] == second[i] == third[i]):
                    decoded_binary_image_bits[i] = first[i]
                elif(first[i] == second[i]):
                    decoded_binary_image_bits[i] = first[i]
                else:
                    decoded_binary_image_bits[i] = third[i]
            return decoded_binary_image_bits


def hamming_code(self, binary_string):
    """Hamming code - error corection code finding single error 
    """
    decoded_string=""
    temp_list = list(binary_string)
    int_list_binary = list(map(int, temp_list))
   
    mistake = reduce(
        xor, [i for i, bit in enumerate(int_list_binary) if bit])
    if mistake != 0:
        print('Mistake found at the position ', mistake, ' and corrected')
        if(int_list_binary[mistake] == 1):
            int_list_binary[mistake] = 0
        else:
            int_list_binary[mistake] = 1
        
        for i in int_list_binary:
            decoded_string += str(i)
        return(decoded_string)
    else:
        print("No mistake found !")
        for i in int_list_binary:
            decoded_string += str(i)
        return(decoded_string)
