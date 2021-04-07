from collections import Counter
import re

def main():
    return True

def prepare_input(input_string):
    input_string = input_string.lower()
    input_string = re.sub(r'[^\w\s]','',input_string)
    return input_string.split(" ")

def count_words(words): 
    return Counter(words)

def filter_bans(input_dict, banned):
    return {key: value for key, value in input_dict.items() if key not in banned}

