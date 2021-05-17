from PIL import Image
import numpy as np
import komm as komm

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

    def bits_trippling_1(self):
        """Function which return trippled bits in order aaabbbccc
        """
        bits = np.array((self.image_bits))
        trippled_binary_image_bits = np.repeat(bits, 3)
        return trippled_binary_image_bits
    #TODO: Statystyki Potrajanie bitów metodą AAABBBCCC - zakodowana potrojona wiadomość

    def bits_trippling_2(self):
        """Function which return trippled bits in order abcabcabc
        """
        bits = np.array((self.image_bits))
        trippled_bits = np.append(bits,[bits,bits])
        return trippled_bits
    #TODO: Statystyki Potrajanie bitów metodą ABCABCABC - zakodowana potrojona wiadomość 

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
     #TODO: Statystyki Potrajanie bitów metodą ABCABCABC i AAABBBCCC - w zaleności od parametru order stosowana jest dla danej metody, zwraca odkodowny ciąg bitów (dla AAABBBCCC order_char jest F, dla ABCABCABC order_char jest C)

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
    #TODO: Statystyki Hamming - zwraca wiadomość z nadmiarem informacyjnym i posiada dodatkowe zera na końcu (gdy długość nie jest podzelna przez długość potrzebną do zakodowania) 

        elif (len(bits)%code.dimension == 0):
            number_of_arrays = int(len(bits)/code.dimension)
            parts_to_encode = np.reshape(bits,(number_of_arrays,-1),order ='C')

            encoded_parts =[]
            for i in range (0, len(parts_to_encode)):
                encoded_part =  code.encode(parts_to_encode[i])
                encoded_parts.append(encoded_part)
            encoded_parts = np.array(encoded_parts)

            return encoded_parts
    #TODO: Statystyki Hamming - zwraca wiadomość z nadmiarem informacyjnym (bez dodatkowych zer bo iwadomość jest podzielna przez długość potrzebną do zakodowania)
    
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
        #TODO: Statystyki Hamming- odkodowana wiadomość i usunięte dodatkowe zera 

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
        #TODO: Statystyki BCH - zwraca wiadomość z nadmiarem informacyjnym i posiada dodatkowe zera na końcu (gdy długość nie jest podzelna przez długość potrzebną do zakodowania) 

        elif (len(bits)%code.dimension == 0):
            number_of_arrays = int(len(bits)/code.dimension)
            parts_to_encode = np.reshape(bits,(number_of_arrays,-1),order ='C')

            encoded_parts =[]
            for i in range (0, len(parts_to_encode)):
                encoded_part =  code.encode(parts_to_encode[i])
                encoded_parts.append(encoded_part)
            encoded_parts = np.array(encoded_parts)

            return encoded_parts
        #TODO: Statystyki BCH - zwraca wiadomość z nadmiarem informacyjnym (bez dodatkowych zer bo iwadomość jest podzielna przez długość potrzebną do zakodowania)

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

        #TODO: Statystyki BCH- odkodowana wiadomość i usunięte dodatkowe zera 
    
    def ParityCheck_encode(self,parameter):
        """ Single Parity Check encoding method 
        """

        bits = np.array(self.image_bits)
        code = komm.SingleParityCheckCode(parameter)
        
        if (len(bits)%code.dimension > 0):
            bits = np.append(bits, [np.zeros(self.calculate_zeros_addition_Single_Parity_Check(parameter),dtype = np.uint8)])
            number_of_arrays = int(len(bits)/code.dimension)
            parts_to_encode = np.reshape(bits,(number_of_arrays,-1),order ='C')

            encoded_parts =[]
            for i in range (0, len(parts_to_encode)):
                encoded_part =  code.encode(parts_to_encode[i])
                encoded_parts.append(encoded_part)
            encoded_parts = np.array(encoded_parts)

            return encoded_parts
        #TODO: Statystyki BCH - zwraca wiadomość z nadmiarem informacyjnym i posiada dodatkowe zera na końcu (gdy długość nie jest podzelna przez długość potrzebną do zakodowania) 
        elif (len(bits)%code.dimension == 0):
           
            number_of_arrays = int(len(bits)/code.dimension)
            parts_to_encode = np.reshape(bits,(number_of_arrays,-1),order ='C')

            encoded_parts =[]
            for i in range (0, len(parts_to_encode)):
                encoded_part =  code.encode(parts_to_encode[i])
                encoded_parts.append(encoded_part)
            encoded_parts = np.array(encoded_parts)

            return encoded_parts
        #TODO: Statystyki ParityCheck - zwraca wiadomość z nadmiarem informacyjnym (bez dodatkowych zer bo wiadomość jest podzielna przez długość potrzebną do zakodowania)

    def ParityCheck_decode(self,encoded_parts,parameter):
            """Single Parity Check decoding method 
            """
            code = komm.SingleParityCheckCode(parameter)
            decoded_parts = []
            for i in range (0, len(encoded_parts)):
                decoded_part = code.decode(encoded_parts[i])
                decoded_parts.append(decoded_part)
            
            decoded_parts = np.array(decoded_parts)
            decoded_parts = np.concatenate(decoded_parts)
            if(len(self.image_bits)%code.dimension != 0):
                for i in range(0,self.calculate_zeros_addition_Single_Parity_Check(parameter)):
                    decoded_parts = np.delete(decoded_parts,len(decoded_parts)-1)
            
            return decoded_parts
     #TODO: Statystyki ParityCheck- odkodowana wiadomość i usunięte dodatkowe zera 

    def array_to_decode(self,number_of_arrays, array):
        decode_array = np.reshape(array,(number_of_arrays,-1),order ='C')
        return decode_array