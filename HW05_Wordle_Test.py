import unittest
from unittest.mock import patch

import HW05_Aishwarya_Shirbhate_dictionary as dict
import HW05_Aishwarya_Shirbhate_wordle as w
import HW05_Aishwarya_Shirbhate_ui as ui


class wordle_test(unittest.TestCase):

    # @patch('builtins.input', return_value=)
    def test_case1(self):                            #guess is the answer
        theAns = "honey"
        theGuess = "honey"
        # clue = wordGuesser(theAns, theGuess)
        self.assertEqual(w.wordGuesser(theAns, theGuess)[0], True)

    def test_case2(self):                            #guess is not the answer
        theAns = "balls"
        theGuess = "babes"
        # clue = wordGuesser(theAns, theGuess)
        res = w.wordGuesser(theAns, theGuess)
        self.assertEqual(''.join(res[1]), '  "" ')


    def test_case3(self):
        theAns = "aaron"
        theGuess = "stats"                          #guess is of multiple repeated characters
        # clue = wordGuesser(theAns, theGuess)
        res= w.wordGuesser(theAns, theGuess)

        self.assertEqual(''.join(res[1]), '""`""')


    @patch('builtins.input', side_effect=['', "balls"])
    def test_case4(self, input):                   # when you pass empty input
        theAns = "balls"
        theGuess = ""
        number_of_wins = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        history = {"won": 0, "loss": 0}

        self.assertEqual(ui.input_check("play", theAns, number_of_wins, history)[0], "exit")

    @patch('builtins.input', side_effect=['small', "balls"])
    def test_case5(self, input):                   # when you pass incorrect input
        theAns = "balls"
        theGuess = "small"
        number_of_wins = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        history = {"won": 0, "loss": 0}

        self.assertEqual(ui.input_check("play", theAns, number_of_wins, history)[0], "play")

    @patch('builtins.input', side_effect=['small', "balls"])
    def test_case6(self, input):                   # when you pass correct input (to check main function)
        theAns = "balls"
        theGuess = "balls"
        number_of_wins = {1: 0, 2: 1, 3: 0, 4: 0, 5: 0, 6: 0}
        history = {"won": 0, "loss": 0}

        self.assertEqual(ui.input_check("play", theAns, number_of_wins, history)[0], "play")

    @patch('builtins.input', side_effect=['balls', "balls"])
    def test_case7(self, input):                  # when you pass correct input(check history)
        theAns = "balls"
        theGuess = "balls"
        number_of_wins = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        history = {"won": 0, "loss": 0}
        self.assertEqual(ui.input_check("play", theAns, number_of_wins, history)[2], {'loss': 0, 'won': 1})

    @patch('builtins.input', side_effect=['stats', 'human', 'viral', 'along', 'among', 'small'])
    def test_case8(self, input):                 # when user loses game (check history)
        theAns = "honey"
        theGuess = "balls"
        number_of_wins = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        history = {"won": 0, "loss": 0}
        res = ui.input_check("play", theAns, number_of_wins, history)
        print(res)
        self.assertEqual(res[2]['loss'], 1)

    @patch('builtins.input', side_effect=['stats', 'human', 'viral', 'along', 'among', 'small',
                                          'stats', 'human', 'viral', 'along', 'among', 'small',
                                          'stats', 'human', 'viral', 'along', 'among', 'small'])
    def test_case9(self, input):  # when user plays multiple games and check history is maintained for the same
        theAns = "honey"
        theGuess = "balls"
        number_of_wins = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        history = {"won": 0, "loss": 0}
        res = ui.input_check("play", theAns, number_of_wins, history)
        history = res[2]
        print(res)

        theAns = "viral"
        theGuess = "balls"
        res = ui.input_check("play", theAns, number_of_wins, history)
        history = res[2]
        print(res)

        theAns = "small"
        theGuess = "balls"
        res = ui.input_check("play", theAns, number_of_wins, history)
        history = res[2]
        print(res)
        self.assertEqual(res[2], {'loss': 1, 'won': 2})

    def test_case10(self):    # checks if word list contains same number of letters as in word list file
        i = 0
        with open("word_list.txt") as word_file:
            data = word_file.read()
            lines = data.split()
            i += len(lines)
            self.assertEqual(len(dict.func_dict()), i, True)

    def test_case11(self):      # checks if input letter is of length 5
        self.assertEqual(len(dict.func_englishword()), 5)

    @patch('builtins.input', side_effect=[{'loss': 0, 'won': 0} ])
    def test_case12(self, input):      # checks if stats are displayed correctly if user has lost and won games
        history = {'loss': 1, 'won': 1}
        self.assertEqual(ui.game_stats(history), (2, 50.0))

    @patch('builtins.input', side_effect=[{'loss': 0, 'won': 0}])
    def test_case13(self, input):      # checks if stats are displayed correctly if games are won
        history = {'loss': 0, 'won': 1}
        self.assertEqual(ui.game_stats(history), (1, 100.0))

    @patch('builtins.input', side_effect=[{'loss': 0, 'won': 0}])
    def test_case14(self, input):      # checks if stats are displayed correctly if games are lost
        history = {'loss': 1, 'won': 0}
        self.assertEqual(ui.game_stats(history), (1, 0.0))


if __name__ == '__main__':
    unittest.main()


