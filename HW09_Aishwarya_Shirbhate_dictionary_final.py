# Homework Assignment 09
# from Aishwarya Shirbhate 20005242
# Pseudocode #
# import random library
# define function func_dictionary
# in the function {
# initialise word_list array
# open word_list.txt file s word_file
# lower case all word extracted from dictionary
# for random_word in word_file
#   strip and append word_list
# return word_list
# end
# }
# define function english word
# in the function {
# while true
#   chose random word from above funct_dict function and assign it to dict_answer
#   if length of dict_answer = 5
#       break
# return dict_answer
# end}

import HW09_Aishwarya_Shirbhate_utility_final as utility
import random
import sys


# function to open word_list.txt and store it into word list array


class dictionary:
    def __init__(self):
        self.random_word=""

    def __str__(self):
        print(self.random_word)

    def get_variables(self):
        return self.random_word

    def set_variable(self,word):
        self.random_word=word

    def func_dict(self) -> list:
        """
        Returns word list array with all the words from word_list.txt.
        """
        try:
            word_list = []

            # opening dictionary file

            with open("word_list.txt") as word_file:
                english_words = set(word.strip().lower() for word in word_file)
            word_file = open("word_list.txt")  # opening word_list.txt
            for random_word in word_file:
                word_list.append(random_word.strip())
            return word_list  # return word list
        except:
            print("Error:", sys.exc_info()[0], " in func_dict function")

    def func_englishword(self) -> str:
        """
        Returns random english word from the word list array.
        """
        try:
            self.set_variable(random.choice(utility.Fiveletterwords().five_letter_word()))
            return self.random_word  # returns random english word
        except:
            print("Error:", sys.exc_info()[0], " in func_englishword function")


