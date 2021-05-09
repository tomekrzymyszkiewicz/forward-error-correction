from Channel import Channel
from Message import Image_message
from Message import CorectionCodes

test_image_file_name = "test_image.jpeg"
saved_test_image = "save_image.jpeg"

def main():
    image = Image_message(test_image_file_name)
    trippled_message = image.bits_trippling()
    trippled_message_with_errors = Channel.random_error_number(trippled_message, 400000)
    decoded__message = Image_message.decode_trippled_bits(image,trippled_message_with_errors)
    image.image_bits = decoded__message
    image.save(saved_test_image)
    
    #moja propozycja organizacji - rozbicie kodow korekcyjnych na dodatkowa klase#
    
    message = Image_message(test_image_file_name) #bez korekcji
    message_with_errors = Channel.random_error_number(message.image_bits, 400000)
    message.image_bits = message_with_errors
    message.save(saved_test_image)
    
    message = Image_message(test_image_file_name) #hamming(7,4)
    haming_coded_message = CorectionCodes.hamming_code(message.image_bits)
    haming_coded_message_with_errors = Channel.random_error_number(haming_coded_message, 400000)
    decoded_haming_coded_message = CorectionCodes.decode_hamming_code(haming_coded_message_with_errors)
    message.image_bits = decoded_haming_coded_message
    message.save(saved_test_image)
    


main()