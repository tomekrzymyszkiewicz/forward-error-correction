from PIL import Image
import numpy as np
import komm as komm

class CorectionCodes:

    def __init__(self,bits):
        """Load data from file and get size and pixel data (as 'image_bits')
        """
        self.image_bits = bits

    def bits_trippling_1(self):
        """Function which return trippled bits in order aaabbbccc
        """
        bits = np.array((self.image_bits))
        trippled_binary_image_bits = np.repeat(bits, 3)
        return trippled_binary_image_bits


    def bits_trippling_2(self):
        """Function which return trippled bits in order abcabcabc
        """
        bits = np.array((self.image_bits))
        trippled_bits = np.append(bits,[bits,bits])
        return trippled_bits


    def decode_trippled_bits(self, trippled_binary_array,order_char):
            """Function that decodes trippled bits
            order_char for bits_trippling_1 = 'F' - Fortran order
            order_char for bits_trippling_2 = 'C' - C order
            """
            separated_binary_array = np.reshape(trippled_binary_array,(3,-1), order = order_char)
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
     

    def calculate_zeros_addition_Hamming(self,parameter):
        bits = np.array(self.image_bits)
        code = komm.HammingCode(parameter)
        additional_zeros =  (int(len(bits)/code.dimension+1) * code.dimension) - len(bits)
        return additional_zeros

    def calculate_zeros_addition_BCH(self,parameter,correcting_capability):
            bits = np.array(self.image_bits)
            code = komm.BCHCode(parameter,correcting_capability)
            additional_zeros =  (int(len(bits)/code.dimension+1) * code.dimension) - len(bits)
            return additional_zeros

    def calculate_zeros_addition_Single_Parity_Check(self,parameter):
            bits = np.array(self.image_bits)
            code = komm.SingleParityCheckCode(parameter)
            additional_zeros =  (int(len(bits)/code.dimension+1) * code.dimension) - len(bits)
            return additional_zeros

    def hamming_encode(self,parameter):
        """ Hamming code encoding method for image pixels
        """

        bits = np.array(self.image_bits)
        code = komm.HammingCode(parameter)
        
        if (len(bits)%code.dimension > 0):
            
            bits = np.append(bits, [np.zeros(self.calculate_zeros_addition_Hamming(parameter),dtype = np.uint8)])
            number_of_arrays = int(len(bits)/code.dimension)
            parts_to_encode = np.reshape(bits,(number_of_arrays,-1),order ='C')

            encoded_parts =[]
            for i in range (0, len(parts_to_encode)):
                encoded_part =  code.encode(parts_to_encode[i])
                encoded_parts.append(encoded_part)
            encoded_parts = np.array(encoded_parts)

            return encoded_parts

        elif (len(bits)%code.dimension == 0):
            number_of_arrays = int(len(bits)/code.dimension)
            parts_to_encode = np.reshape(bits,(number_of_arrays,-1),order ='C')

            encoded_parts =[]
            for i in range (0, len(parts_to_encode)):
                encoded_part =  code.encode(parts_to_encode[i])
                encoded_parts.append(encoded_part)
            encoded_parts = np.array(encoded_parts)

            return encoded_parts
    
    def hamming_decode(self,encoded_parts,parameter):
            """Decoding method for Hamming code
            """
            code = komm.HammingCode(parameter)
            decoded_parts = []
            for i in range (0, len(encoded_parts)):
                decoded_part = code.decode(encoded_parts[i])
                decoded_parts.append(decoded_part)
            
            decoded_parts = np.array(decoded_parts)
            decoded_parts = np.concatenate(decoded_parts)
            if(len(self.image_bits)%code.dimension != 0):
                for i in range(0,self.calculate_zeros_addition_Hamming(parameter)):
                    decoded_parts = np.delete(decoded_parts,len(decoded_parts)-1)
            
            return decoded_parts

    def BCH_encode(self,parameter,correcting_capability):
        """ BCH code encoding method 
        1 <= correcting_capability < 2^(parameter -1)
        """

        bits = np.array(self.image_bits)
        code = komm.BCHCode(parameter,correcting_capability)
        
        if (len(bits)%code.dimension > 0):
            
            bits = np.append(bits, [np.zeros(self.calculate_zeros_addition_BCH(parameter,correcting_capability),dtype = np.uint8)])
            number_of_arrays = int(len(bits)/code.dimension)
            parts_to_encode = np.reshape(bits,(number_of_arrays,-1),order ='C')

            encoded_parts =[]
            for i in range (0, len(parts_to_encode)):
                encoded_part =  code.encode(parts_to_encode[i])
                encoded_parts.append(encoded_part)
            encoded_parts = np.array(encoded_parts)

            return encoded_parts

        elif (len(bits)%code.dimension == 0):
            number_of_arrays = int(len(bits)/code.dimension)
            parts_to_encode = np.reshape(bits,(number_of_arrays,-1),order ='C')

            encoded_parts =[]
            for i in range (0, len(parts_to_encode)):
                encoded_part =  code.encode(parts_to_encode[i])
                encoded_parts.append(encoded_part)
            encoded_parts = np.array(encoded_parts)

            return encoded_parts

    def BCH_decode(self,encoded_parts,parameter,correcting_capability):
            """Decoding method for cyclic BCH code
            """
            code = komm.BCHCode(parameter,correcting_capability)
            decoded_parts = []
            for i in range (0, len(encoded_parts)):
                decoded_part = code.decode(encoded_parts[i])
                decoded_parts.append(decoded_part)
            
            decoded_parts = np.array(decoded_parts)
            decoded_parts = np.concatenate(decoded_parts)
            if(len(self.image_bits)%code.dimension != 0):
                for i in range(0,self.calculate_zeros_addition_BCH(parameter,correcting_capability)):
                    decoded_parts = np.delete(decoded_parts,len(decoded_parts)-1)
            
            return decoded_parts

    

    def array_to_decode(self,number_of_arrays, array):
        decode_array = np.reshape(array,(number_of_arrays,-1),order ='C')
        return decode_array

    def encode_hamming(message_bits): #compare with haming from library, our implementation
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

        return haming_coded_bits

    def decode_hamming(haming_coded_bits):
        """Decode Hamming code(7,4) 
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
                decoded_haming_coded_bits[j] =  int(not decoded_haming_coded_bits[j])
            if detection == 6:
                decoded_haming_coded_bits[j + 1] =  int(not decoded_haming_coded_bits[j + 1])
            if detection == 5:
                decoded_haming_coded_bits[j + 2] =  int(not decoded_haming_coded_bits[j + 1])
            if detection == 3:
                decoded_haming_coded_bits[j + 3] =  int(not decoded_haming_coded_bits[j + 1])
              
            i += 7
            j += 4

        while i < len(haming_coded_bits): 
            decoded_haming_coded_bits.append(0)
            decoded_haming_coded_bits[j] = haming_coded_bits[i]
            decoded_haming_coded_bits[j] = haming_coded_bits[i]
            i += 1

        return decoded_haming_coded_bits