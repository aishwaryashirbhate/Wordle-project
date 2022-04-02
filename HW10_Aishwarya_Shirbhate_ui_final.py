# Homework Assignment 10
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
# log user input, no of wins and answer
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
#   log total games and win perc


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

import HW10_Aishwarya_Shirbhate_dictionary_final as Module_dictionary
import HW10_Aishwarya_Shirbhate_wordle_final as Module_wordle
import HW10_Aishwarya_Shirbhate_occurence_stats_final as Module_stats
import HW10_Aishwarya_Shirbhate_Wordle_helper as wordle_helper
import HW10_Aishwarya_Shirbhate_Wordle_Solver as wordle_solver
import csv
from operator import itemgetter
import sys
import logging

import traceback

print("*** WORDLE GAME ***")

logging.basicConfig(filename='gameplay.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


class UI:
    def __init__(self):
        self.check = "play"
        self.number_of_wins = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        self.history = {"won": 0, "loss": 0}
        self.valid_words = []
        self.good = []
        self.bad = []
        self.rank_list = []
        get_columns = itemgetter('rank', 'words')
        with open('wordRank.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile.readlines()[0:])
        self.rank_list = [get_columns(row) for row in reader]

    def __str__(self):
        print(self.check)
        print(self.history)
        print(self.number_of_wins)
        print(self.valid_words)

    def set_variables(self, check, number_of_wins, history, valid_words):
        self.check = check
        self.number_of_wins = number_of_wins
        self.history = history
        self.valid_words = valid_words

    def get_variables(self):
        return [self.check, self.history, self.number_of_wins, self.valid_words]

    def input_check(self, answer):
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
            symbol_list = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<',
                           '`',
                           '}',
                           '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/', ' ', '1', '2', '3', '4', '5',
                           '6',
                           '7',
                           '8',
                           '9',
                           '0'}  # symbol list that needs to be excluded
            # array for user input
            user_inputs = []
            maximum_guesses = 0
            correct_guess = False
            self.good = []
            self.bad = []
            get_columns = itemgetter('rank', 'words')
            with open('wordRank.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile.readlines()[0:])
            self.rank_list = [get_columns(row) for row in reader]
            # self.top_fifty()
            c = ""
            # while loop for maximum guesses
            while maximum_guesses < 6 and not correct_guess:

                guess = input("Please enter a 5 letter word and press Enter:")

                if len(guess) == 0:
                    print("You have now ended the game\n Thank you for playing Wordle\n ")
                    self.game_stats()
                    for i in self.history:
                        self.history[i] = 0
                    self.set_variables("exit", self.number_of_wins, self.history, self.valid_words)
                    # self.check = "exit"
                    break
                symbol_check = [ele for ele in symbol_list if (ele in guess)]
                bool_symbolcheck = bool(symbol_check)
                if len(guess) == 5:
                    if bool_symbolcheck is False:
                        if guess not in user_inputs:
                            if guess in Module_dictionary.dictionary().func_dict():
                                user_inputs.append(guess)
                                maximum_guesses += 1
                                lower_guess = guess.lower()
                                correct_guess = Module_wordle.word_guess(answer, lower_guess).wordGuesser()[
                                    0]  # calling above function
                                c = Module_wordle.word_guess(answer, lower_guess).wordGuesser()[
                                    1]
                                if not correct_guess:
                                    # res = wordle_helper.Wordle_Helper(self.good, self.bad).find_words(c, guess)
                                    # self.good = res[1]
                                    # self.bad = res[2]
                                    # print("please try these word:", res[0])

                                    solver = wordle_solver.Wordle_Solver(self.rank_list).find_words(c, guess)
                                    self.rank_list = solver
                                    print(solver)
                                    print("SOLVER RECOMMENDS THIS WORD:", solver[0][1])
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
                if maximum_guesses in self.number_of_wins:
                    self.number_of_wins[maximum_guesses] += 1
                else:
                    self.number_of_wins[maximum_guesses] = 1
                self.history["won"] += 1
                print("Guess Distribution is:", self.number_of_wins)  # displays guess distribution of the game
                self.game_stats()

            elif len(guess) == 0:
                print("Guess Distribution is:", self.number_of_wins)  # displays guess distribution of the game
                print("You have now ended the game\nThank you for playing Wordle\n ")

            else:
                print("You have used up your guesses")
                print("The correct answer is", answer)
                self.history["loss"] += 1
                print("Guess Distribution is:", self.number_of_wins)  # displays guess distribution of the game
                self.game_stats()

            logging.info("Input words: " + str(user_inputs))
            logging.info("\nactual answer:\n" + str(answer))
            logging.info("\nnumber of games won is: \n")
            logging.info(str(self.number_of_wins))

            return correct_guess, user_inputs
        except:
            print("Error:", traceback.print_exc(), " in input check function")

    def game_stats(self):
        """
        displays statistics for current session of the game
       :param history:
        """
        try:
            lost_games = self.history["loss"]
            won_games = self.history["won"]
            total_games = won_games + lost_games
            print("total no of games played are:", total_games)  # displays total number of games played
            if total_games != 0:
                win_prec = (won_games / total_games) * 100
                print("winning percentage are:", win_prec)  # displays winning percentage
                logging.info("\n****************************************************************\n")
                logging.info("Total games played: " + str(total_games))
                logging.info("\nwin percentage: " + str(win_prec))
                return total_games, win_prec
            else:
                win_prec = 0
                print("winning percentage are:", 0)  # displays winning percentage
                logging.info("\n****************************************************************\n")
                logging.info("Total games played: " + str(total_games))
                logging.info("\nwin percentage: " + str(win_prec))
                return total_games, win_prec
        except:
            print("Error:", sys.exc_info(), " in game stats function")

    def wordle(self):
        """
        Checks for check value and executes wordle game by calling input_check function.
        """

        try:
            self.set_variables("play", {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}, {"won": 0, "loss": 0}, [])

            while self.check == "play":
                answer = Module_dictionary.dictionary().func_englishword()  # assign english word to answer
                if type(answer) == 'NoneType':
                    raise Exception("not valid word")  # raise exception if file is not present
                if answer not in self.valid_words:
                    self.valid_words.append(answer)
                    self.input_check(answer)
                    print('*' * 100)
                if len(self.valid_words) == 1379:  # if all words are used reset the word list
                    self.valid_words = []
        except:
            print("Error:", traceback.print_exc(), " in wordle function")


if __name__ == '__main__':
    Module_stats.occ_stats().occurrence_stats()
    UI().wordle()
