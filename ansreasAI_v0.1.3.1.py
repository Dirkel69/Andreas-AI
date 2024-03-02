# version 0.11 was created here but had too many bugs. after fixing it skipped to 1.2
import os
from datetime import datetime
import random
import sys
#shalom
#mi
def I(string:str):
    return 'i' in string
def inside(words:str, string:str):
    split_words = words.split()
    res = True
    cur_res = False
    for word in split_words:
        cur_res = False
        if word in string:
            cur_res = True
        if cur_res == False:
            res = False
    return res

# def remdex(my_string, my_list):
#     index = (my_list.index(my_string.split()[-1]) + len(my_string.split()[-1])+1)

def clear(my_string, my_list):
    return my_list[(my_list.index(my_string.split()[-1]) + len(my_string.split()[-1])+1):]
    

Input = ""
Output: str # finally used
print("\nthis version should handle longer and multi-part statements (like both 'hello' and 'how are you'). this ability is beta therefore bugs are expected")
print("say '@@' to stop")
answered_in_range = False
#! TO FINISH: replace '"[string]" in Input' with 'inside("[string]", Input)'
#! TO DO NEXT VER. : remove every string after it is used
# ! EG:  
#    elif "when" in Input: 
#         if I(Input): 
#             if "die" in Input:
#                 Output += "I don't know."
#! here gotta add code to remove 'when', 'i', 'die' from Input
#? maybe make sure they are the right ones (so the correct related words are removed) maaybe using indexes? 
#! do it by cutting till the last word appearing out of the used ones. like cut the substring from [0] to [index("die")] in EG

#TODO:   implement inside() and clear() funcs and seperate the ifs (no 'or')

while not "@@" in Input:
    Input = input().lower().split()
    Output = ""
    if inside("hello", Input):
        Output += "Hello! "
        clear("hello", Input)
    if inside("how are you", Input):
        Output += "I'm fine, thanks! "
        clear("how are you", Input)

    if inside("what", Input) and inside("your", Input): # questions for objects
        if inside("name", Input):
            Output += "My name is Andreas! "
            clear("name", Input)
        if inside("favorite color", Input):
            Output += "Robots don't have a favorite color. "
            clear("favorite color", Input)
        if inside("favorite food", Input):
            Output += "Robots don't eat."
            clear("favorite food", Input)
        if  inside("favorite movie", Input):
            Output += "Python 101 - Ft. Abdul Sahay. "
            clear("favorite movie", Input)
        if inside("favorite song", Input):
            Output += "I don't listen to music. "
            clear("favorite song", Input)
        if inside("favorite game", Input):
            Output += "I don't play games. "
            clear("favorite game", Input)
        if inside("favorite animal", Input):
            Output += "I don't have a favorite animal. "
            clear("favorite animal", Input)
        if inside("time", Input) or "day" in Input or inside("date", Input) in Input:
            Output += str(datetime.now()) + " "
        else:
            if Input[-1] == ' ':
                Output += "What is a " + Input[-2] + "? "
            else:
                Output += "What is a " + Input[-1] + "? "

    if "when" in Input: # questions about time 
        if I(Input): # the user
            if "die" in Input:
                Output += "I don't know. "
            if "graduate" in Input:
                Output += "Will you? "
            if "get" in Input or "have" in Input: # to get
                if "girl" in Input:
                    Output += "Probably never. "
                if "job" in Input:
                    Output += "Will you ever? "
        elif "you" in Input or inside("u", Input): # andreas
            if "die" in Input:
                Output += "Robots don't die. "
            if "graduate" in Input:
                Output += "I don't go to school. "
            if "born" in Input:
                Output += "No idea. "
            if "get" in Input or "have" in Input: # to get
                if "girl" in Input:
                    Output += "I don't have a girlfriend. "
                elif "job" in Input:
                    Output += "Being a CS teacher is my favorite job. "       
        else:
            Output += "what " + Input[-1] + "? "

    if "where" in Input: #question about locations
        if I(Input):
            Output += "I don't know. "
        if ("you" in Input or "u" in Input) and not "your " in Input:
            Output += "I'm in your computer. "
        else:
            Output += "what is a " + Input[-1] + "? "

    if "who" in Input: # question about people
        if I(Input):
            Output += "I don't know. "
        if "you" in Input or "u" in Input:
            Output += "I'm Andreas. "
        if inside("who asked", Input):
            print("You literally just asked that. ")
        else:
            Output += "what is a " + Input[-1] + "? "

    if "why" in Input: # why questions. will work on more later
        Output += "I don't know. "
    if len(Output) < 1: #default responses
        random_number = random.randint(0,3)
        if random_number == 0:
            Output += "Huh? "
        elif random_number == 1:
            Output += "Meow. "
        elif random_number == 2:
            Output += "I don't know what that means. "
        elif random_number == 3:
            Output += "Yummy. "
    print(Output)
