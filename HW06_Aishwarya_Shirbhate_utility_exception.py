# Homework Assignment 06
# from Aishwarya Shirbhate 20005242
# Pseudocode #
# define five_letter_word() function
# {
# open word_list.txt file to read
# store all the words with length 5 in words list
# close file
# open 5letterwords.txt file to write
# for element in words list
# write every 5 letter word in word list into file
# close text file
# return words

import sys


def five_letter_word():
    """
    function to filter 5 letter words from word_list and return those words.
    :return words:
    """
    try:

        string = open("word_list.txt", "r")   # opens word list file to read
        words = [word for word in string.read().split() if len(word) == 5]
        string.close()                       # close file
        textfile = open("5letterwords.txt", "w")   # opens file to write 5 letter words
        for element in words:
            textfile.write(element + "\n")
        textfile.close()
        return words
    except:
        print("Error:", sys.exc_info()[0], " in five_letter_word function")

