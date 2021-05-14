from Channel import Channel
from Message import Image_message
import komm as komm

test_image_file_name = "test_image.jpeg"
saved_test_image = "save_image.jpeg"

def main():
    image = Image_message(test_image_file_name)
    #trippled_message = image.bits_trippling_1()
    encoded_message = image.hamming_encode()

    # channel = Channel(trippled_message)
   # trippled_message_with_errors = channel.random_error_number(500000)
   # decoded__message = Image_message.decode_trippled_bits(image,trippled_message_with_errors,'F')
    decoded_hamming_message = image.hamming_decode(encoded_message)
    image.image_bits = decoded_hamming_message
    image.save(saved_test_image)

main()