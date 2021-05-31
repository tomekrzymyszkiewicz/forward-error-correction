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

    