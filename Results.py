import csv
import numpy as np
from os import write

class Results:
    def __init__(self):
        """The class that stores information about the results of FEC testing in the transmission of messages over the interference channel\n
        - message length
        - name of used code
        - code rate
        - number of errors in message ()
        - number of correctly fixed errors
        - optional comment about test
        """
        
        self.results = []
    def add_result(self,original_message, encoded_message, decoded_message, code, number_of_errors, comment = ''):
        """Adds information about a single test to the results\n
        Passed arguments:
        - original_message - original message as numpy array of bits
        - encoded_message - encoded message as numpy array of bits
        - decoded_message - decoded message as numpy array of bits
        - code - name of used code as string
        - number_of_errors - number of errors as int
        - comment - (optional) comment
        """
        self.results.append({'message_length': len(original_message),'code': code,'rate': len(original_message)/len(encoded_message),'number_of_errors': number_of_errors,'number_of_fixed_errors':(number_of_errors - np.count_nonzero(np.logical_xor(original_message,decoded_message))),'comment': comment})
    def print_results(self):
        """Displays the content of all results
        """
        for result in self.results:
            print('message_length:', result['message_length'],'code:', result['code'],'rate:', result['rate'],'number_of_errors:', result['number_of_errors'],'number_of_fixed_errors:',result['number_of_fixed_errors'],'comment:', result['comment'])
    def save_to_file(self,file_name):
        """Saves all results to a csv file
        """
        with open(file_name,newline='',mode='w') as results_file:
            field_names = ['message_length','code','rate','number_of_errors','number_of_fixed_errors','comment']
            writer = csv.DictWriter(results_file,fieldnames=field_names)
            writer.writeheader()
            writer.writerows(self.results)
    