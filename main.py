from Channel import Channel
from Message import Image_message
import komm as komm


test_image_file_name = "test_image.jpeg"
saved_test_image = "save_image.jpeg"

def main():
    image = Image_message(test_image_file_name)
    encoded_message = image.ParityCheck_encode(5)

    # channel = Channel(encoded_message)
    # encoded_message_with_errors = channel.random_error_number(100)

    decoded_message = image.ParityCheck_decode(encoded_message,5)
    image.image_bits = decoded_message

    image.save(saved_test_image)
    
  
main()