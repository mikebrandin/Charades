import json
from PyDictionary import PyDictionary
import requests
import time

def generate_random_word():
    return str((requests.get('https://random-word-api.herokuapp.com/word?number=1&swear=0').json())).replace('\'', '').replace('[','').replace(']','')

def print_word_info(word):
    dictionary = PyDictionary()
    print("Word Info: ")
    print(dictionary.meaning(word))
    
gameRunning = True

while gameRunning:
    val = input("Is it your turn? y/n (or enter x to end the game): ")

    #If the game is over
    if val == "x" or val == "X":
        gameRunning = False
    
    #If it is their turn, give them a word a start a 30 second timer
    if val == "y" or val == "Y":
        word = generate_random_word()
        print("Your word is ", word)
        print_word_info(word)
        print()
        
        ready = input("You have 30 seconds. When you are ready, hit the enter key!")
        print("Timer has started, good luck!")

        #Start the timer
        now = time.time()
        future = now + 30
        while time.time() < future:
            pass

        print()
        print("Times Up! If your team answered correctly, give yourself a point!")
        print()

    #If it is not their turn, pass
    if val == "n" or val == "N":
        pass
