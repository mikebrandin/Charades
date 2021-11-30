import json

import requests


def generate_random_word():
    return str((requests.get('https://random-word-api.herokuapp.com/word?number=1&swear=0').json())).replace('\'', '').replace('[','').replace(']','')


print(generate_random_word())