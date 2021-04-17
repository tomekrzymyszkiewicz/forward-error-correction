import base64
import binascii
from functools import reduce
from operator import xor

test_image_file_name = "test_image.jpeg"
test_binary_file_name = "binary_image.bin"
saved_test_image = "save_image.jpeg"


def image_file_to_bin_file(image_file_name, binary_file_name):
    """Load image file (.jpg), convert to bytes string then save to .bin file
    """
    with open(image_file_name, "rb") as loaded_image:
        image_as_string = base64.b64encode(loaded_image.read())
    with open(binary_file_name, "wb") as saved_binary:
        saved_binary.write(image_as_string)


def bin_file_to_image_file(image_file_name, binary_file_name):
    """Load .bin file then save as image file (.jpg)
    """
    binary_source = open(binary_file_name, "rb")
    file_bytes = binary_source.read()
    destination_image_file = open(image_file_name, "wb")
    destination_image_file.write(base64.b64decode((file_bytes)))
    destination_image_file.close()


def bytes_string_to_image_file(bytes_string, image_file_name):
    """Save byte string to image file (.jpg)
    """
    destination_image_file = open(image_file_name, "wb")
    destination_image_file.write(base64.b64decode((bytes_string)))
    destination_image_file.close()


def bin_file_to_bytes_string(binary_file_name):
    """Load .bin file then return as bytes string
    """
    binary_source = open(binary_file_name, "rb")
    file_bytes = binary_source.read().decode('utf-8')
    return file_bytes


def bytes_string_to_binary_string(text, encoding='utf-8', errors='surrogatepass'):
    """Convert bytes string (e.g. agO3;) to binary string (e.g. 100101001000) then return binary string
    """
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def binary_string_to_bytes_string(bits, encoding='utf-8', errors='surrogatepass'):
    """Convert binary string (e.g. 100100101) to bytes string (e.g. fE4%) then return bytes string
    """
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)


def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))


def image_to_binary_string(image_file_name):
    """Load image (e.g. jpg) and return as binary string
    """
    with open(image_file_name, "rb") as loaded_image:
        image_as_string = base64.b64encode(loaded_image.read()).decode('utf-8')
    return bytes_string_to_binary_string(image_as_string)


def binary_string_to_image(binary_string, image_file_name):
    """Save binary string as image (e.g. jpg)
    """
    bytes_to_save = binary_string_to_bytes_string(binary_string)
    destination_image_file = open(image_file_name, "wb")
    destination_image_file.write(base64.b64decode((bytes_to_save)))
    destination_image_file.close()


def bits_trippling(self, binary_string):
    """Function which tripple bits in the binary sting eg(101 -> 111000111)
    """
    trippled_binary_string = ""
    for i in binary_string:
        for j in range(0, 3):
            trippled_binary_string += i
    return(trippled_binary_string)

def decode_trippled_bits(self, trippled_binary_string):
        """Function that decodes trippled binary string eg.(111000111 -> 101)
        """
        decoded_binary_string = ""
        first = ""
        second = ""
        third = ""
        for i in range(0, int(len(trippled_binary_string)/3)):
            first += trippled_binary_string[3*i+0]
            second += trippled_binary_string[3*i+1]
            third += trippled_binary_string[3*i+2]

        for i, bit in enumerate(first):
            if(bit == second[i] and bit == third[i]):
                decoded_binary_string += bit
            else:
                count_0 = 0
                count_1 = 0

                if bit == '0':
                    count_0 += 1
                else:
                    count_1 += 1

                if second[i] == '0':
                    count_0 += 1
                else:
                    count_1 += 1

                if third[i] == '0':
                    count_0 += 1
                else:
                    count_1 += 1

                if count_0 > count_1:
                    decoded_binary_string += '0'
                elif count_0 < count_1:
                    decoded_binary_string += '1'

        return(decoded_binary_string)


def hamming_code(self, binary_string):
    """Forward error correction Hamming code binary_string = "1 0 0 0 1 0 1 0 0 1 1 1 0 1 1 0" 
    """
    temp_list = (binary_string.split())
    int_list_binary = list(map(int, temp_list))
    mistake = reduce(
        xor, [i for i, bit in enumerate(int_list_binary) if bit])
    if mistake != 0:
        print('Mistake found at the position ', mistake, ' and corrected')
        if(int_list_binary[mistake] == 1):
            int_list_binary[mistake] = 0
        else:
            int_list_binary[mistake] = 1
        print(int_list_binary)
    else:
        print("No mistake found !")
