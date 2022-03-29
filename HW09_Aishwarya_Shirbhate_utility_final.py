# Homework Assignment 09
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

class Fiveletterwords:
    def __init__(self):
        self.filename=""

    def __str__(self):
        print(self.filename)

    def get_variables(self):
        return self.filename

    def set_variables(self,f):
        self.filename=f

    def five_letter_word(self):
        """
        function to filter 5 letter words from word_list and return those words.
        :return words:
        """
        try:
            self.set_variables("word_list.txt")
            string = open(self.get_variables(), "r")   # opens word list file to read
            words = [word for word in string.read().split() if len(word) == 5]
            string.close()  # close file
            self.set_variables("5letterwords.txt")
            textfile = open(self.get_variables(), "w")   # opens file to write 5 letter words
            for element in words:
                textfile.write(element + "\n")
            textfile.close()
            return words
        except:
            print("Error:", sys.exc_info()[0], " in five_letter_word function")

