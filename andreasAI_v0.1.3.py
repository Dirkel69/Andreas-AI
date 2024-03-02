# version 0.11 was created here but had too many bugs. after fixing it skipped to 1.2
import os
from datetime import datetime
import random

def I(string:str):
    words = string.split()
    return 'i' in words
    

Input = ""
Output: str # not currently used
print("this version uses a different method of output building but it is beta so bugs are expected")
print("say '@@' to stop")
while Input != '@@':
    Input = input().lower()
    Output = ""
    if "hello" in Input:
        Output += "Hello!"
    elif "how are you" in Input:
        Output += "I'm fine, thanks!"
    elif "what" in Input or "your" in Input: # questions for objects
        if "name" in Input:
            Output += "My name is Andreas!"
        elif "favorite color" in Input:
            Output += "Robots don't have a favorite color."
        elif "favorite food" in Input:
            Output += "Robots don't eat."
        elif  "favorite movie" in Input:
            Output += "Python 101 - Ft. Abdul Sahay"
        elif "favorite song" in Input:
            Output += "I don't listen to music."
        elif "favorite game" in Input:
            Output += "I don't play games."
        elif "favorite animal" in Input:
            Output += "I don't have a favorite animal."
        elif "time" in Input or "day" in Input or "date" in Input:
            Output += str(datetime.now())
        else:
            if Input.split(" ")[-1] == ' ':
                Output += "What is a " + Input.split(" ")[-2] + "?"
            else:
                Output += "What is a " + Input.split(" ")[-1] + "?"
    elif "when" in Input: # questions about time 
        if I(Input): # the user
            if 'die' in Input:
                Output += "I don't know."
            elif 'graduate' in Input:
                Output += "Will you?"
            elif "get" in Input or "have" in Input: # to get
                if "girl" in Input:
                    Output += "Probably never."
                elif "job" in Input:
                    Output += "Will you ever?"
        elif "you" in Input or "u" in Input: # andreas
            if "die" in Input:
                Output += "Robots don't die."
            elif "graduate" in Input:
                Output += "I don't go to school."
            elif "born" in Input:
                Output += "No idea."
            elif "get" in Input or "have" in Input: # to get or to have
                if "girl" in Input:
                    Output += "I don't have a girlfriend."
                elif "job" in Input:
                    Output += "Being a CS teacher is my favorite job."       
        else:
            Output += "what " + Input.split(" ")[-1] + "?"
    elif "where" in Input: #question about locations
        if I(Input):
            Output += "I don't know."
        elif ("you" in Input or "u" in Input) and not "your" in Input:
            Output += "I'm in your computer."
        else:
            Output += "what is a " + Input.split(" ")[-1] + "?"
    elif "why" in Input: # why questions. will work on more later
        Output += "I don't know."
    else: #default responses
        random_number = random.randint(0,3)
        if random_number == 0:
            Output += "Huh?"
        elif random_number == 1:
            Output += "Meow."
        elif random_number == 2:
            Output += "I don't know what that means."
        elif random_number == 3:
            Output += "Yummy."
    print(Output)
