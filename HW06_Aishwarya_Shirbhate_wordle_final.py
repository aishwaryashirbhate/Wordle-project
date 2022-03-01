# Homework Assignment 06
# from Aishwarya Shirbhate 20005242
# pseudocode #
# Define a function with given word and guessed word as input
# In word guesser function {
# initialise ansList and input answer into this list
# initialise guessList and input guessed word into this list
# initialise arr_guess array with clue marks defined
# for i in range and length of ansList
#   if ansList[i] is equal to guessList[i] position
#       update arr_guess[i] to ' '
#       update ansList[i] to 'done'
# for i in range and length of guessList
#   for j in range and length of ansList
#       if arr_guess[i] is not equal to ' ' and ansList[j] is equal to guessList[i]
#           update arr_guess[i] to '`'
# print arr_guess
# join all items in arr_guess to a string  and assign it to clue
# print clue
# if length of clue is 0
#   return true
# end
#   }

# function to print the clue aby comparing the answer and guessed word


def wordGuesser(theAns, theGuess):
    """
    This function takes Answer and guessed word as input parameters and returns true if the word matches.
    This function prints the clue on the console.
    :param theAns:
    :param theGuess:
    """
    try:
        ansList = list(theAns)
        guessList = list(theGuess)
        arr_guess = ['"', '"', '"', '"', '"']
        for i in range(len(ansList)):
            if ansList[i] == guessList[i]:
                arr_guess[i] = ' '
                ansList[i] = 'done'

        for i in range(len(guessList)):
            for j in range(len(ansList)):
                if arr_guess[i] != ' ' and ansList[j] == guessList[i]:
                    arr_guess[i] = '`'

        print(arr_guess)
        clue = ''.join(arr_guess)
        print(clue)
        if len(clue.strip()) == 0:
            return True, clue
        else:
            return False, clue

    except:
        print("Error:", sys.exc_info()[0], " in wordGuesser function")











