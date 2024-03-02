# version 0.11 was created here but had too many bugs. after fixing it skipped to 1.2
import os
from datetime import datetime
import random

def I(string:str):
    words = string.split()
    return 'i' in words
    

Input = ""
Output: str # not currently used
#! make statements not print, but added to output var so "hello" and "how are you" can both be answered
#! example: print("Hello")  ->  Output += "Hello"     //    print it at the end and reset to "" at every start
print("still bugs around multiple statements")
print("say '@@' to stop")
while Input != '@@':
    Input = input().lower()

    if "hello" in Input:
        print("Hello!")
    elif "how are you" in Input:
        print("I'm fine, thanks!")
    elif "what" in Input or "your" in Input: # questions for objects
        if "name" in Input:
            print("My name is Andreas!")
        elif "favorite color" in Input:
            print("Robots don't have a favorite color.")
        elif "favorite food" in Input:
            print("Robots don't eat.")
        elif  "favorite movie" in Input:
            print("Python 101 - Ft. Abdul Sahay")
        elif "favorite song" in Input:
            print("I don't listen to music.")
        elif "favorite game" in Input:
            print("I don't play games.")
        elif "favorite animal" in Input:
            print("I don't have a favorite animal.")
        elif "time" in Input or "day" in Input or "date" in Input:
            print(datetime.now())
        else:
            if Input.split(" ")[-1] == ' ':
                print("What is a " + Input.split(" ")[-2] + "?")
            else:
                print("What is a " + Input.split(" ")[-1] + "?")
    elif "when" in Input: # questions about time 
        if I(Input): # the user
            if 'die' in Input:
                print("I don't know.")
            elif 'graduate' in Input:
                print("Will you?")
            elif "get" in Input or "have" in Input: # to get
                if "girl" in Input:
                    print("Probably never.")
                elif "job" in Input:
                    print("Will you ever?")
        elif "you" in Input or "u" in Input: # andreas
            if "die" in Input:
                print("Robots don't die.")
            elif "graduate" in Input:
                print("I don't go to school.")
            elif "born" in Input:
                print("No idea.")
            elif "get" in Input or "have" in Input: # to get
                if "girl" in Input:
                    print("I don't have a girlfriend.")
                elif "job" in Input:
                    print("Being a CS teacher is my favorite job.")       
        else:
            print("what " + Input.split(" ")[-1] + "?")
    elif "where" in Input: #question about locations
        if I(Input):
            print("I don't know.")
        elif ("you" in Input or "u" in Input) and not "your" in Input:
            print("I'm in your computer.")
        else:
            print("what is a " + Input.split(" ")[-1] + "?")
    elif "why" in Input: # why questions. will work on more later
        print("I don't know.")
    else: #default responses
        random_number = random.randint(0,3)
        if random_number == 0:
            print("Huh?")
        elif random_number == 1:
            print("Meow.")
        elif random_number == 2:
            print("I don't know what that means.")
        elif random_number == 3:
            print("Yummy.")
