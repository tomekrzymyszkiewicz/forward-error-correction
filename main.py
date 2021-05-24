from Results import Results
from Channel import Channel
from Message import Image_message
from CorectionCodes import CorectionCodes
import numpy as np
import komm as komm


test_image_file_name = "test_image.jpeg"
saved_test_image = "save_image.jpeg"
results = Results()
results_file_name = 'test_result_file.csv'

def main():

    image = Image_message(test_image_file_name)
    corectionCodes = CorectionCodes(image.image_bits)

    #encoded_message = corectionCodes.BCH_encode(10,2) #strasznie wolne dlatego zakomentowane
    #encoded_message_with_errors = Channel.random_error_number(np.concatenate(encoded_message), 100000) 
    #encoded_meassage_with_error_to_decode = corectionCodes.array_to_decode(len(encoded_message),encoded_message_with_errors)
    #decoded_message = corectionCodes.BCH_decode(encoded_meassage_with_error_to_decode,10,2)
    #image.image_bits = decoded_message
    #image.save(saved_test_image)

    encoded_message = corectionCodes.hamming_encode(10)
    encoded_message_with_errors = Channel.random_error_number(np.concatenate(encoded_message), 100000) 
    encoded_meassage_with_error_to_decode = corectionCodes.array_to_decode(len(encoded_message),encoded_message_with_errors)
    decoded_message = image.hamming_decode(encoded_meassage_with_error_to_decode, 10)
    image.image_bits = decoded_message
    #image.save(saved_test_image)

    encoded_message = corectionCodes.ParityCheck_encode(10)
    encoded_message_with_errors = Channel.random_error_number(np.concatenate(encoded_message), 100000) 
    encoded_meassage_with_error_to_decode = corectionCodes.array_to_decode(len(encoded_message),encoded_message_with_errors)
    decoded_message = corectionCodes.ParityCheck_decode(encoded_meassage_with_error_to_decode,10)
    image.image_bits = decoded_message
    #image.save(saved_test_image)

    encoded_message = corectionCodes.bits_trippling_1()
    encoded_message_with_errors = Channel.random_error_number(encoded_message, 100000) 
    encoded_meassage_with_error_to_decode = corectionCodes.array_to_decode(len(encoded_message),encoded_message_with_errors)
    decoded_message = corectionCodes.decode_trippled_bits(encoded_message_with_errors,'F')
    image.image_bits = decoded_message
    #image.save(saved_test_image)

    encoded_message = corectionCodes.bits_trippling_2()
    encoded_message_with_errors = Channel.random_error_number(encoded_message, 100000) 
    encoded_meassage_with_error_to_decode = corectionCodes.array_to_decode(len(encoded_message),encoded_message_with_errors)
    decoded_message = corectionCodes.decode_trippled_bits(encoded_message_with_errors,'c')
    image.image_bits = decoded_message
    #image.save(saved_test_image)

    encoded_message = CorectionCodes.encode_hamming(image.image_bits)
    encoded_message_with_errors = Channel.random_error_number(encoded_message, 100000)
    decoded__message = CorectionCodes.decode_hamming(encoded_message_with_errors)
    image.image_bits = decoded__message
    image.save(saved_test_image)

#####################################################################################################################################
    #image = Image_message(test_image_file_name)

    # encoded_message = image.bits_trippling_1() # bits trippling
    # encoded_message = image.bits_trippling_2() # bits trippling
    # encoded_message = image.hamming_encode(10)
    #encoded_message = image.BCH_encode(10,2)
    # encoded_message = image.ParityCheck_encode(10)

    #number_of_arrays = len(encoded_message)
    #concated = np.concatenate(encoded_message)
    
    #channel = Channel(encoded_message) # bits trippling
    #channel = Channel(concated)
    #encoded_message_with_errors = Channel.random_error_number(concated, 100000) #tu concatenate
    #encoded_meassage_with_error_to_decode = image.array_to_decode(number_of_arrays,encoded_message_with_errors)

    # decoded_message = image.decode_trippled_bits(encoded_message_with_errors,'F') # bits trippling decode AAABBBCCC
    # decoded_message = image.decode_trippled_bits(encoded_message_with_errors,'C') # bits trippling decode ABCABCABC
    # decoded_message = image.hamming_decode(encoded_meassage_with_error_to_decode,10)
    #decoded_message = image.BCH_decode(encoded_meassage_with_error_to_decode,10,2) #to mozna dac wewnatrz kazdej funkcji
    # decoded_message = image.ParityCheck_decode(encoded_meassage_with_error_to_decode,10)
    #image.image_bits = decoded_message


    image.save(saved_test_image)

    results.add_result(image.image_bits,concated,decoded_message,'BCD',100)
    results.print_results()
    results.save_to_file(results_file_name)
    #image.save(saved_test_image)
  

main()