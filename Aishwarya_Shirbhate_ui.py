# Homework Assignment 03
# from Aishwarya Shirbhate 20005242
# Pseudocode #
# Define input_check function with check and answer input
# In the function {
# Initialise variables maximum attempts and user inputs.
#  Define symbol list which needs to be excluded from the user input.
#  While maximum attempts < 6,
#     ask for user input.
#  if length of user input = 0
#   update check as exit
#       break
#  if length of user input is 5,
#    if symbols not in user input
#      if user input is uniquer than previous responses,
#            call wordGuesser function
#      else print prompt "Provided word is used previously. Please enter a new word"
#    else print prompt "Input word contains symbols/characters. Please input words with alphabets only"
#  else print prompt "Input word length needs to be 5 alphabets long"
#
#  if all alphabets are in correct order,
#       game is over. print "Woah! You guessed it right in attempt" with maximum attempts used to the user
#  if length of user input = 0
#       then print "you have now ended the game. Thank you for playing Wordle "
#  if input word is not same as given word
#     then continue function till maximum attempts are <= 6
#  else game is over. print "You have used up your guesses" and the correct word to the user.
# return check
#  end
# }
# define main wordle function
# in the main function {
# initialise check = "play"
# while check = "play"
#   call dictionary module and assign englishword to answer
#   call input_check function
# end }
# call wordle function

import HW03_Aishwarya_Shirbhate_dictionary as Module_dictionary
import HW03_Aishwarya_Shirbhate_wordle as Module_wordle

print("*** WORDLE GAME ***")


def input_check(check, answer):

    """
    Checks user input is in proper format and implement word_guesser function.
    :param check:
    :param answer:
    :return check:
    """

    symbol_list = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}',
                   '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/', ' ', '1', '2', '3', '4', '5', '6', '7',
                   '8',
                   '9',
                   '0'}             # symbol list that needs to be excluded
    # array for user input
    user_inputs = []
    maximum_guesses = 0
    correct_guess = False

    # while loop for maximum guesses
    while maximum_guesses < 6 and not correct_guess:
        guess = input("Please enter a 5 letter word and press Enter:")
        if len(guess) == 0:
            check = "exit"
            break
        symbol_check = [ele for ele in symbol_list if (ele in guess)]
        bool_symbolcheck = bool(symbol_check)
        if len(guess) == 5:
            if bool_symbolcheck is False:
                if guess not in user_inputs:
                    if guess in Module_dictionary.func_dict():
                        user_inputs.append(guess)
                        maximum_guesses += 1
                        lower_guess = guess.lower()
                        correct_guess = Module_wordle.wordGuesser(answer, lower_guess)  # calling above function
                    else:
                        print("please provide a valid dictionary word")
                else:
                    print("Provided word is used previously. Please enter a new word")
            else:
                print("Input word contains symbols/characters. Please input words with alphabets only")
        else:
            print("Input word length needs to be 5 alphabets long")

    if correct_guess:
        print("Woah! You guessed it right in attempt", maximum_guesses)

    elif len(guess) == 0:
        print("You have now ended the game\n Thank you for playing Wordle\n ")

    else:
        print("You have used up your guesses")
        print("The correct answer is", answer)

    return check


def wordle():

    """
    Checks for check value and executes wordle game by calling input_check function.
    """

    check = "play"
    while check == "play":
        answer = Module_dictionary.func_englishword()            # assign english word to answer
        check = input_check(check, answer)                       # assign check to input_check function


wordle()
