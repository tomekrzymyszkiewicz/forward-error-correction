from Results import Results
from Channel import Channel
from Message import Image_message
from CorectionCodes import CorectionCodes
from Generator import Generator
import numpy as np
import komm as komm


test_image_file_name = "image.jpg"
saved_test_image = "save_image.jpeg"
results = Results()
results_file_name = 'hamming_10.csv'

def main():
    # for num_of_err in range(10000,100001,10000):
    #     image = Image_message(test_image_file_name)
    #     corectionCodes = CorectionCodes(image.image_bits)
    #     encoded_message = corectionCodes.hamming_encode(3)
    #     encoded_message_with_errors = Channel.random_error_number(np.concatenate(encoded_message), num_of_err) 
    #     encoded_meassage_with_error_to_decode = corectionCodes.array_to_decode(len(encoded_message),encoded_message_with_errors)
    #     decoded_message = corectionCodes.hamming_decode(encoded_meassage_with_error_to_decode, 3)
    #     results.add_result(image.image_bits,np.concatenate(encoded_message),decoded_message,'hamming_7-4',num_of_err)
    #     results.print_results()
    # for num_of_err in range(10000,100001,10000):
    #     image = Image_message(test_image_file_name)
    #     corectionCodes = CorectionCodes(image.image_bits)
    #     encoded_message = corectionCodes.hamming_encode(4)
    #     encoded_message_with_errors = Channel.random_error_number(np.concatenate(encoded_message), num_of_err) 
    #     encoded_meassage_with_error_to_decode = corectionCodes.array_to_decode(len(encoded_message),encoded_message_with_errors)
    #     decoded_message = corectionCodes.hamming_decode(encoded_meassage_with_error_to_decode, 4)
    #     results.add_result(image.image_bits,np.concatenate(encoded_message),decoded_message,'hamming_15-11',num_of_err)
    #     results.print_results()
    # for num_of_err in range(10000,100001,10000):
    #     image = Image_message(test_image_file_name)
    #     corectionCodes = CorectionCodes(image.image_bits)
    #     encoded_message = corectionCodes.hamming_encode(5)
    #     encoded_message_with_errors = Channel.random_error_number(np.concatenate(encoded_message), num_of_err) 
    #     encoded_meassage_with_error_to_decode = corectionCodes.array_to_decode(len(encoded_message),encoded_message_with_errors)
    #     decoded_message = corectionCodes.hamming_decode(encoded_meassage_with_error_to_decode, 5)
    #     results.add_result(image.image_bits,np.concatenate(encoded_message),decoded_message,'hamming_31-26',num_of_err)
    #     results.print_results()
    # for num_of_err in range(10000,100001,10000):
    #     image = Image_message(test_image_file_name)
    #     corectionCodes = CorectionCodes(image.image_bits)
    #     encoded_message = corectionCodes.hamming_encode(6)
    #     encoded_message_with_errors = Channel.random_error_number(np.concatenate(encoded_message), num_of_err) 
    #     encoded_meassage_with_error_to_decode = corectionCodes.array_to_decode(len(encoded_message),encoded_message_with_errors)
    #     decoded_message = corectionCodes.hamming_decode(encoded_meassage_with_error_to_decode, 6)
    #     results.add_result(image.image_bits,np.concatenate(encoded_message),decoded_message,'hamming_63-57',num_of_err)
    #     results.print_results()
    # for num_of_err in range(10000,100001,10000):
    #     image = Image_message(test_image_file_name)
    #     corectionCodes = CorectionCodes(image.image_bits)
    #     encoded_message = corectionCodes.hamming_encode(7)
    #     encoded_message_with_errors = Channel.random_error_number(np.concatenate(encoded_message), num_of_err) 
    #     encoded_meassage_with_error_to_decode = corectionCodes.array_to_decode(len(encoded_message),encoded_message_with_errors)
    #     decoded_message = corectionCodes.hamming_decode(encoded_meassage_with_error_to_decode, 7)
    #     results.add_result(image.image_bits,np.concatenate(encoded_message),decoded_message,'hamming_127-120',num_of_err)
    #     results.print_results()
    for num_of_err in range(100000,600000,100000):
        image = Image_message(test_image_file_name)
        corectionCodes = CorectionCodes(image.image_bits)
        encoded_message = corectionCodes.hamming_encode(8)
        encoded_message_with_errors = Channel.random_error_number(np.concatenate(encoded_message), num_of_err) 
        encoded_meassage_with_error_to_decode = corectionCodes.array_to_decode(len(encoded_message),encoded_message_with_errors)
        decoded_message = corectionCodes.hamming_decode(encoded_meassage_with_error_to_decode, 8)
        results.add_result(image.image_bits,np.concatenate(encoded_message),decoded_message,'hamming_255-247',num_of_err)
        results.print_results()
    results.save_to_file("hamming_test.csv")

    # image = Image_message(test_image_file_name)
    # corectionCodes = CorectionCodes(image.image_bits)
    # image_with_errors = Channel.random_error_number(image.image_bits, 100000) 
    # image.image_bits = image_with_errors
    # image.save("grafika 100k bledow.jpg")

    # image = Image_message(test_image_file_name)
    # corectionCodes = CorectionCodes(image.image_bits)
    # encoded_message = corectionCodes.bits_trippling_2()
    # encoded_message_with_errors = Channel.random_error_number(encoded_message, 100000) 
    # encoded_meassage_with_error_to_decode = corectionCodes.array_to_decode(len(encoded_message),encoded_message_with_errors)
    # decoded_message = corectionCodes.decode_trippled_bits(encoded_meassage_with_error_to_decode,'C')
    # image.image_bits = decoded_message
    # image.save("grafika 100k bledow tripling.jpg")

    # image = Image_message(test_image_file_name)
    # corectionCodes = CorectionCodes(image.image_bits)
    # encoded_message = corectionCodes.hamming_encode(3)
    # encoded_message_with_errors = Channel.random_error_number(np.concatenate(encoded_message), 100000) 
    # encoded_meassage_with_error_to_decode = corectionCodes.array_to_decode(len(encoded_message),encoded_message_with_errors)
    # decoded_message = corectionCodes.hamming_decode(encoded_meassage_with_error_to_decode, 3)
    # image.image_bits = decoded_message
    # image.save("grafika 100k bledow hamming.jpg")

    # for num_of_err in range(10000,100001,10000):
        # image = Image_message(test_image_file_name)
        # corectionCodes = CorectionCodes(image.image_bits)
        # encoded_message = corectionCodes.bits_trippling_1()
        # encoded_message_with_errors = Channel.random_error_number(encoded_message, num_of_err) 
        # encoded_meassage_with_error_to_decode = corectionCodes.array_to_decode(len(encoded_message),encoded_message_with_errors)
        # decoded_message = corectionCodes.decode_trippled_bits(encoded_meassage_with_error_to_decode,'F')
        # results.add_result(image.image_bits,encoded_message,decoded_message,'tripling_abc',num_of_err)
        # results.print_results()
    # for num_of_err in range(10000,100001,10000):
    #     image = Image_message(test_image_file_name)
    #     corectionCodes = CorectionCodes(image.image_bits)
    #     encoded_message = corectionCodes.bits_trippling_2()
    #     encoded_message_with_errors = Channel.random_error_number(encoded_message, num_of_err) 
    #     encoded_meassage_with_error_to_decode = corectionCodes.array_to_decode(len(encoded_message),encoded_message_with_errors)
    #     decoded_message = corectionCodes.decode_trippled_bits(encoded_meassage_with_error_to_decode,'C')
    #     results.add_result(image.image_bits,encoded_message,decoded_message,'tripling_aaa',num_of_err)
    #     results.print_results()
    # results.save_to_file("tripling.csv")

    # for num_of_err in range(100,1001,100):
    #     bits = Generator.generate_bits(3000)
    #     corectionCodes = CorectionCodes(bits)
    #     encoded_message = corectionCodes.BCH_encode(5,3)
    #     encoded_message_with_errors = Channel.random_error_number(np.concatenate(encoded_message), num_of_err) 
    #     encoded_meassage_with_error_to_decode = corectionCodes.array_to_decode(len(encoded_message),encoded_message_with_errors)
    #     decoded_message = corectionCodes.BCH_decode(encoded_meassage_with_error_to_decode,5,3)
    #     results.add_result(bits,np.concatenate(encoded_message),decoded_message,'bch 5-3',num_of_err)
    #     results.print_results()
    # results.save_to_file("bch.csv")

    #encoded_message = corectionCodes.BCH_encode(10,2) #strasznie wolne dlatego zakomentowane
    #encoded_message_with_errors = Channel.random_error_number(np.concatenate(encoded_message), 100000) 
    #encoded_meassage_with_error_to_decode = corectionCodes.array_to_decode(len(encoded_message),encoded_message_with_errors)
    #decoded_message = corectionCodes.BCH_decode(encoded_meassage_with_error_to_decode,10,2)
    #image.image_bits = decoded_message
    #image.save(saved_test_image)

    # encoded_message = corectionCodes.hamming_encode(10)
    # encoded_message_with_errors = Channel.random_error_number(np.concatenate(encoded_message), 100000) 
    # encoded_meassage_with_error_to_decode = corectionCodes.array_to_decode(len(encoded_message),encoded_message_with_errors)
    # decoded_message = corectionCodes.hamming_decode(encoded_meassage_with_error_to_decode, 10)
    # image.image_bits = decoded_message
    # #image.save(saved_test_image)

    # results.add_result(image.image_bits,encoded_message,decoded_message,'Hamming10',100000)

    # encoded_message = corectionCodes.bits_trippling_1()
    # encoded_message_with_errors = Channel.random_error_number(encoded_message, 100000) 
    # encoded_meassage_with_error_to_decode = corectionCodes.array_to_decode(len(encoded_message),encoded_message_with_errors)
    # decoded_message = corectionCodes.decode_trippled_bits(encoded_message_with_errors,'F')
    # image.image_bits = decoded_message
    # #image.save(saved_test_image)

    # results.add_result(image.image_bits,encoded_message,decoded_message,'triplingaabbcc',100000)

    # encoded_message = corectionCodes.bits_trippling_2()
    # encoded_message_with_errors = Channel.random_error_number(encoded_message, 100000) 
    # encoded_meassage_with_error_to_decode = corectionCodes.array_to_decode(len(encoded_message),encoded_message_with_errors)
    # decoded_message = corectionCodes.decode_trippled_bits(encoded_message_with_errors,'c')
    # image.image_bits = decoded_message
    # #image.save(saved_test_image)

    # results.add_result(image.image_bits,encoded_message,decoded_message,'triplingabcabcabc',100000)

    # encoded_message = CorectionCodes.encode_hamming(image.image_bits)
    # encoded_message_with_errors = Channel.random_error_number(encoded_message, 100000)
    # decoded__message = CorectionCodes.decode_hamming(encoded_message_with_errors)
    # image.image_bits = decoded__message
    # image.save(saved_test_image)

    # results.add_result(image.image_bits,encoded_message,decoded_message,'hamming(7,4)',100000)

    # results.print_results()
    # results.save_to_file(results_file_name)
  

main()