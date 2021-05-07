from Channel import Channel
from Message import Image_message
from Message import CorectionCodes

test_image_file_name = "test_image.jpeg"
saved_test_image = "save_image.jpeg"

def main():
    image = Image_message(test_image_file_name)
    trippled_message = image.bits_trippling()
    channel = Channel(trippled_message)
    trippled_message_with_errors = channel.random_error_number(4000000)
    decoded__message = Image_message.decode_trippled_bits(image,trippled_message_with_errors)
    image.image_bits = decoded__message
    image.save(saved_test_image)
    
    #moja propozycja organizacji - rozbicie kodow korekcyjnych na dodatkowa klase#
    
    #message = Image_message(test_image_file_name)
    #haming_coded_message = CorectionCodes.hamming_code(message.image_bits)
    #haming_coded_message_with_errors = Channel.random_error_number(haming_coded_message, 4000000)
    #decoded_haming_coded_message = CorectionCodes.decode_hamming_code(haming_coded_message_with_errors)
    #message.image_bits = decoded_haming_coded_message
    #message.save(saved_test_image)

main()