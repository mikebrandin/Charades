import json
from PyDictionary import PyDictionary
import requests


def generate_random_word():
    return str((requests.get('https://random-word-api.herokuapp.com/word?number=1&swear=0').json())).replace('\'', '').replace('[','').replace(']','')

def print_word_info(word):
    dictionary = PyDictionary()
    print("Word Info:")
    print(dictionary.meaning(word))
    

word = generate_random_word()
print(word)
print_word_info(word)
