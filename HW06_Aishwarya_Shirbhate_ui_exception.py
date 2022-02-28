# Homework Assignment 06
# from Aishwarya Shirbhate 20005242
# Pseudocode #
# Define input_check function with check, answer, number of wins and history input
# In the function
# {
# Initialise variables maximum attempts and user inputs.
#  Define symbol list which needs to be excluded from the user input.
#  While maximum attempts < 6,
#     ask for user input.
#  if length of user input = 0
#   print "You have now ended the game\n Thank you for playing Wordle\n "
#   call gameStats function
#   for i in history[i] = 0
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
#               if maximum_guesses in number_of_wins:
#             number_of_wins[maximum_guesses] += 1
#         else:
#             number_of_wins[maximum_guesses] = 1
#
#         update history[won] by 1
#         print "Guess Distribution is:" and number_of_wins
#  if length of user input = 0
#       then print "you have now ended the game. Thank you for playing Wordle "
#       print "Guess Distribution is:" and number_of_wins
#  if input word is not same as given word
#     then continue function till maximum attempts are <= 6
#  else game is over. print "You have used up your guesses" and the correct word to the user.
#       update history["loss"] by 1
#         print "Guess Distribution is:" and number_of_wins
#         call game_stats(history) function
# open gameplaylog.txt
# write user input, no of wins and answer
# close the file
# return check, number_of_wins, history
#  end
# }
# define gameStats function with history as input
#   let lost_games = history["loss"]
#   let won_games = history["won"]
#   let total_games = won_games + lost_games
#   let win_prec = (won_games/total_games) * 100
#   print "total no of games won are:" and won_games
#   print "total no of games lost are:" and lost_games
#   print "winning percentage are:" and win_prec
#   open gameplaylog.txt file
#   write total games and win perc
#   close the file

# define main wordle function
# in the main function {
# initialise check = "play"
# let number_of_wins = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
# let history = {"won": 0, "loss": 0}
# define valid words list
# while check = "play"
#   call dictionary module and assign englishword to answer
#             if type(answer) == 'NoneType'
#                 raise Exception
# if answer is not in valid_words
#   valid_words.append(answer)
#   call input_check function
#   print('*' * 100)
# if len(valid_words) == 1379 then
#   valid_words = []
# end }
# call wordle function

import HW06_Aishwarya_Shirbhate_dictionary_exception as Module_dictionary
import HW06_Aishwarya_Shirbhate_wordle_exception as Module_wordle
import json
import sys

print("*** WORDLE GAME ***")


def input_check(check, answer, number_of_wins, history):
    """
    Checks user input is in proper format and implement word_guesser function.
    :param history:
    :param number_of_wins:
    :param check:
    :param answer:
    :return check:
    :return number_of_wins
    :return history
    """
    try:
        symbol_list = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`',
                       '}',
                       '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/', ' ', '1', '2', '3', '4', '5', '6',
                       '7',
                       '8',
                       '9',
                       '0'}  # symbol list that needs to be excluded
        # array for user input
        user_inputs = []
        maximum_guesses = 0
        correct_guess = False

        # while loop for maximum guesses
        while maximum_guesses < 6 and not correct_guess:
            guess = input("Please enter a 5 letter word and press Enter:")
            if len(guess) == 0:
                print("You have now ended the game\n Thank you for playing Wordle\n ")
                game_stats(history)
                for i in history:
                    history[i] = 0
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
                            correct_guess = Module_wordle.wordGuesser(answer, lower_guess)[0]  # calling above function
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
            if maximum_guesses in number_of_wins:
                number_of_wins[maximum_guesses] += 1
            else:
                number_of_wins[maximum_guesses] = 1
            history["won"] += 1
            print("Guess Distribution is:", number_of_wins)  # displays guess distribution of the game
            game_stats(history)

        elif len(guess) == 0:
            print("Guess Distribution is:", number_of_wins)  # displays guess distribution of the game
            print("You have now ended the game\nThank you for playing Wordle\n ")

        else:
            print("You have used up your guesses")
            print("The correct answer is", answer)
            history["loss"] += 1
            print("Guess Distribution is:", number_of_wins)  # displays guess distribution of the game
            game_stats(history)

        textfile = open("gameplaylog.txt", "a")
        textfile.write("\nuser inputs:\n")
        for element in user_inputs:
            textfile.write(" " + element)
        textfile.write("\nactual answer:\n" + answer)
        textfile.write("\nnumber of games won is: \n")
        textfile.write(json.dumps(number_of_wins))
        textfile.close()

        return [check, number_of_wins, history]
    except:
        print("Error:", sys.exc_info()[0], " in input check function")


def game_stats(history):
    """
    displays statistics for current session of the game
   :param history:
    """
    try:
        lost_games = history["loss"]
        won_games = history["won"]
        total_games = won_games + lost_games
        print("total no of games played are:", total_games)  # displays total number of games played
        if total_games != 0:
            win_prec = (won_games / total_games) * 100
            print("winning percentage are:", win_prec)  # displays winning percentage
            textfile = open("gameplaylog.txt", "a")
            textfile.write("\n****************************************************************\n")
            textfile.write("Total games played: \n" + str(total_games))
            textfile.write("\nwin percentage: \n" + str(win_prec))
            textfile.close()
            return total_games, win_prec
        else:
            win_prec = 0
            print("winning percentage are:", 0)  # displays winning percentage
            textfile = open("gameplaylog.txt", "a")
            textfile.write("\n****************************************************************\n")
            textfile.write("\nTotal games played \n" + str(total_games))
            textfile.write("\nwin percentage \n" + str(win_prec))
            textfile.close()
            return total_games, win_prec
    except:
        print("Error:", sys.exc_info()[0], " in game stats function")

def wordle():
    """
    Checks for check value and executes wordle game by calling input_check function.
    """
    try:
        check = "play"
        number_of_wins = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        history = {"won": 0, "loss": 0}
        valid_words = []
        while check == "play":
            answer = Module_dictionary.func_englishword()  # assign english word to answer
            if type(answer) == 'NoneType':
                raise Exception("not valid word")           # raise exception if file is not present
            if answer not in valid_words:
                valid_words.append(answer)
                check, number_of_wins, history = input_check(check, answer, number_of_wins, history)
                print('*' * 100)
            if len(valid_words) == 1379:                    # if all words are used reset the word list
                valid_words = []
    except:
        print("Error:", sys.exc_info()[0], " in wordle function")

if __name__ == '__main__':
    wordle()
