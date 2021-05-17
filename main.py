from Results import Results
from Channel import Channel
from Message import Image_message
import numpy as np
import komm as komm


test_image_file_name = "test_image.jpeg"
saved_test_image = "save_image.jpeg"
results = Results()
results_file_name = 'test_result_file.csv'

def main():
    image = Image_message(test_image_file_name)

    # encoded_message = image.bits_trippling_1() # bits trippling
    # encoded_message = image.bits_trippling_2() # bits trippling
    # encoded_message = image.hamming_encode(10)
    encoded_message = image.BCH_encode(10,2)
    # encoded_message = image.ParityCheck_encode(10)

    number_of_arrays = len(encoded_message)
    concated = np.concatenate(encoded_message)
    
    channel = Channel(encoded_message) # bits trippling
    channel = Channel(concated)
    encoded_message_with_errors = channel.random_error_number(100) 
    encoded_meassage_with_error_to_decode = image.array_to_decode(number_of_arrays,encoded_message_with_errors)

    # decoded_message = image.decode_trippled_bits(encoded_message_with_errors,'F') # bits trippling decode AAABBBCCC
    # decoded_message = image.decode_trippled_bits(encoded_message_with_errors,'C') # bits trippling decode ABCABCABC
    # decoded_message = image.hamming_decode(encoded_meassage_with_error_to_decode,10)
    decoded_message = image.BCH_decode(encoded_meassage_with_error_to_decode,10,2)
    # decoded_message = image.ParityCheck_decode(encoded_meassage_with_error_to_decode,10)
    image.image_bits = decoded_message

    image.save(saved_test_image)

    results.add_result(image.image_bits,concated,decoded_message,'BCD',100)
    results.print_results()
    results.save_to_file(results_file_name)
    
main()