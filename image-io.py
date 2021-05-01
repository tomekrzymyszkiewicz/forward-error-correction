import base64
import binascii
from typing import Sized
from PIL import Image
import numpy as np
from bitstring import BitArray
import io

test_image_file_name = "test_image.jpeg"
test_binary_file_name = "binary_image.bin"
saved_test_image = "save_image.jpeg"

class Image_message:
    def __init__(self,file_name):
        try:
            image  = Image.open(file_name)
        except IOError:
            print("Image loading error")
        self.size = image.size
        pixels = np.asarray(image, dtype=np.uint8)
        self.image_bits = np.unpackbits(pixels)
        
    def print_bits(self):
        print(self.image_bits)

    def save(self):
        packed_bits = np.packbits(self.image_bits)
        packed_bits_reshaped = np.reshape(packed_bits,(self.size[1],self.size[0],3))
        image = Image.fromarray(packed_bits_reshaped)
        image.save(saved_test_image)

def main():

    image = Image_message(test_image_file_name)
    # image.print_bits()
    image.save()


main()