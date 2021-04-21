import Channel
from Channel import Channel as channel
import Message 

def main():
    wiadomosc = Message.image_to_binary_string("test_image.jpeg")
    wiadomosc_zakodowana = Message.bits_trippling(wiadomosc)
    kanal = channel(wiadomosc_zakodowana)
    otrzymana_wiadomosc = kanal.random_error_number(6)
    wiadomosc_zdekodowana = Message.decode_trippled_bits(otrzymana_wiadomosc)
    Message.binary_string_to_image(wiadomosc_zdekodowana,"zapisana_grafika.jpg")

main()