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

class CorectionCodes:
    def __init__(self):
        """Load message bits
        """

    def __init__(self,message_bits):
        """Load message bits
        """
        self.message_bits = message_bits


    def hamming_code(self, message_bits):
        """Hamming code(7,4) 
        """
        haming_coded_bits = []
        i = 0
        j = 0
        while i < len(message_bits):
            if i + 3 >= len(message_bits):
                break
            for x in range(0, 7):
                haming_coded_bits.append(0)
        
            haming_coded_bits[j] = message_bits[i]
            haming_coded_bits[j + 1] = message_bits[i + 1]
            haming_coded_bits[j + 2] = message_bits[i + 2]
            haming_coded_bits[j + 4] = message_bits[i + 3]

            redundancy = 0
            iterator = 0
            for x in range(7, 0, -1):
                if haming_coded_bits[j + iterator] == 1:
                    redundancy = redundancy ^ x
                iterator += 1    
        
            haming_coded_bits[j + 3] = int(redundancy & 4 > 0)
            haming_coded_bits[j + 5] = int(redundancy & 2 > 0)
            haming_coded_bits[j + 6] = int(redundancy & 1 > 0)
            
            i += 4
            j += 7
        while i < len(message_bits):
            haming_coded_bits.append(0)
            haming_coded_bits[j] = message_bits[i]
            haming_coded_bits[j] = message_bits[i]
            i += 1


    def decode_hamming_code(self, haming_coded_bits):
        """decode Hamming code(7,4) 
        """
        decoded_haming_coded_bits = []
        i = 0
        j = 0
        while i < len(haming_coded_bits):
            if i + 6 >= len(haming_coded_bits):
                break
            for x in range(0, 4):
                decoded_haming_coded_bits.append(0)
    
            decoded_haming_coded_bits[j] = haming_coded_bits[i]
            decoded_haming_coded_bits[j + 1] = haming_coded_bits[i + 1]
            decoded_haming_coded_bits[j + 2] = haming_coded_bits[i + 2]
            decoded_haming_coded_bits[j + 3] = haming_coded_bits[i + 4]
    
            detection = 0
            iterator = 0
            for x in range(7, 0, -1):
                if haming_coded_bits[i + iterator] == 1:
                    detection = detection ^ x
                iterator += 1    

            if detection == 7:
                decoded_haming_coded_bits[i] =  int(not decoded_haming_coded_bits[i])
            if detection == 6:
                decoded_haming_coded_bits[i + 1] =  int(not decoded_haming_coded_bits[i])
            if detection == 5:
                decoded_haming_coded_bits[i + 2] =  int(not decoded_haming_coded_bits[i])
            if detection == 3:
                decoded_haming_coded_bits[i + 3] =  int(not decoded_haming_coded_bits[i])
              
            i += 7
            j += 4

        while i < len(haming_coded_bits):          #NIE WIELOKROTNOSCI 4/7
            decoded_haming_coded_bits.append(0)
            decoded_haming_coded_bits[j] = haming_coded_bits[i]
            decoded_haming_coded_bits[j] = haming_coded_bits[i]
            i += 1



            

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
