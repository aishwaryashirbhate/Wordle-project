import unittest
from unittest.mock import patch
import os
import HW10_Aishwarya_Shirbhate_dictionary_final as dict
import HW10_Aishwarya_Shirbhate_wordle_final as w
import HW10_Aishwarya_Shirbhate_ui_final as ui
import HW10_Aishwarya_Shirbhate_occurence_stats_final as oss
import HW10_Aishwarya_Shirbhate_utility_final as uf

class wordle_test(unittest.TestCase):

    # @patch('builtins.input', return_value=)
    def test_case1(self):                            #guess is the answer
        theAns = "honey"
        theGuess = "honey"
        # clue = wordGuesser(theAns, theGuess)
        self.assertEqual(w.word_guess(theAns, theGuess).wordGuesser()[0], True)

    def test_case2(self):                            #guess is not the answer
        theAns = "balls"
        theGuess = "babes"
        # clue = wordGuesser(theAns, theGuess)
        res = w.word_guess(theAns, theGuess).wordGuesser()
        self.assertEqual(''.join(res[1]), '  "" ')


    def test_case3(self):
        theAns = "aaron"
        theGuess = "stats"                          #guess is of multiple repeated characters
        # clue = wordGuesser(theAns, theGuess)
        res= w.word_guess(theAns, theGuess).wordGuesser()

        self.assertEqual(''.join(res[1]), '""`""')


    @patch('builtins.input', side_effect=['', "balls"])
    def test_case4(self, input):                   # when you pass empty input
        theAns = "balls"
        theGuess = ""
        number_of_wins = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        history = {"won": 0, "loss": 0}
        obj=ui.UI()
        obj.input_check(theAns)
        self.assertEqual(obj.get_variables()[0], "exit")

    @patch('builtins.input', side_effect=['small', "balls"])
    def test_case5(self, input):                   # when you pass incorrect input
        theAns = "balls"
        theGuess = "small"
        number_of_wins = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        history = {"won": 0, "loss": 0}
        obj = ui.UI()
        obj.input_check(theAns)
        self.assertEqual(obj.get_variables()[0], "play")

    @patch('builtins.input', side_effect=['small', "balls"])
    def test_case6(self, input):                   # when you pass correct input (to check main function)
        theAns = "balls"
        theGuess = "balls"
        number_of_wins = {1: 0, 2: 1, 3: 0, 4: 0, 5: 0, 6: 0}
        history = {"won": 0, "loss": 0}
        obj = ui.UI()
        obj.set_variables("play",number_of_wins,history,[])
        obj.input_check(theAns)
        self.assertEqual(obj.get_variables()[0], "play")

    @patch('builtins.input', side_effect=['balls', "balls"])
    def test_case7(self, input):                  # when you pass correct input(check history)
        theAns = "balls"
        theGuess = "balls"
        number_of_wins = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        history = {"won": 0, "loss": 0}
        obj = ui.UI()
        obj.set_variables("play", number_of_wins, history, [])
        obj.input_check(theAns)
        self.assertEqual(obj.get_variables()[1], {'loss': 0, 'won': 1})

    @patch('builtins.input', side_effect=['stats', 'human', 'viral', 'along', 'among', 'small'])
    def test_case8(self, input):                 # when user loses game (check history)
        theAns = "honey"
        theGuess = "balls"
        number_of_wins = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        history = {"won": 0, "loss": 0}
        obj = ui.UI()
        obj.set_variables("play", number_of_wins, history, [])
        obj.input_check(theAns)
        self.assertEqual(obj.get_variables()[1]['loss'], 1)

    @patch('builtins.input', side_effect=['stats', 'human', 'viral', 'along', 'among', 'small',
                                          'stats', 'human', 'viral', 'along', 'among', 'small',
                                          'stats', 'human', 'viral', 'along', 'among', 'small'])
    def test_case9(self, input):  # when user plays multiple games and check history is maintained for the same
        theAns = "honey"
        theGuess = "balls"
        number_of_wins = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        history = {"won": 8, "loss": 4}
        obj = ui.UI()
        obj.set_variables("play", number_of_wins, history, [])
        obj.input_check(theAns)

        history = obj.get_variables()[1]


        theAns = "viral"
        theGuess = "balls"
        obj.set_variables("play", number_of_wins, history, [])
        obj.input_check(theAns)
        history = obj.get_variables()[1]


        theAns = "small"
        theGuess = "balls"
        obj.set_variables("play", number_of_wins, history, [])
        obj.input_check(theAns)
        history = obj.get_variables()[1]
        self.assertEqual(obj.get_variables()[1], {'loss': 5, 'won': 10})

    def test_case10(self):    # checks if word list contains same number of letters as in word list file
        i = 0
        with open("word_list.txt") as word_file:
            data = word_file.read()
            lines = data.split()
            i += len(lines)
            self.assertEqual(len(dict.dictionary().func_dict()), i, True)

    def test_case11(self):      # checks if input letter is of length 5
        self.assertEqual(len(dict.dictionary().func_englishword()), 5)

    @patch('builtins.input', side_effect=[{'loss': 0, 'won': 0} ])
    def test_case12(self, input):      # checks if stats are displayed correctly if user has lost and won games
        history = {'loss': 1, 'won': 1}
        obj=ui.UI()
        obj.set_variables("play", {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}, history, [])
        self.assertEqual(obj.game_stats(), (2, 50.0))

    @patch('builtins.input', side_effect=[{'loss': 0, 'won': 0}])
    def test_case13(self, input):      # checks if stats are displayed correctly if games are won
        history = {'loss': 0, 'won': 1}
        obj = ui.UI()
        obj.set_variables("play", {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}, history, [])
        self.assertEqual(obj.game_stats(), (1, 100.0))

    @patch('builtins.input', side_effect=[{'loss': 0, 'won': 0}])
    def test_case14(self, input):      # checks if stats are displayed correctly if games are lost
        history = {'loss': 1, 'won': 0}
        obj = ui.UI()
        obj.set_variables("play", {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}, history, [])
        self.assertEqual(obj.game_stats(), (1, 0.0))

    def test_case15(self):  # checks if all 5-letter words are returned to the function
        self.assertEqual(len(uf.Fiveletterwords().five_letter_word()), 1379)

    def test_case16(self):  # checks if Add_to_freq_file works correctly
        tmp_file = 'tmp.csv'
        elements = ["a"] + [1, 2, 3, 4, 5]
        oss.occ_stats().Add_to_freq_file(tmp_file, elements)
        my_file = open("tmp.csv", "r")
        content = my_file.read()
        self.assertEqual(content, "a,1,2,3,4,5\n")
        os.remove(tmp_file)

    def test_case17(self):  # checks if Add_to_rank_file works correctly
        tmp_file = 'tmp1.csv'
        elements = [('sales', '327814032000/4986792881682899'), ('bones', '227449999296/4986792881682899')]
        oss.occ_stats().Add_to_rank_file(tmp_file, elements)
        my_file = open("tmp1.csv", "r")
        content = my_file.read()
        self.assertEqual(content, "1,sales,327814032000/4986792881682899\n2,bones,227449999296/4986792881682899\n")
        os.remove(tmp_file)

    def test_case18(self):  # checks if Convert_list_to_tuple works correctly
        d = {"a": [1, 2, 3, 4, 5]}
        obj = oss.occ_stats()
        obj.set_variables(d)
        self.assertEqual(obj.Convert_list_to_tuple(), {'a': (1, 2, 3, 4, 5)})

    def test_case19(self):  # checks if Parse_file_to_tuple works correctly
        file = 'tmp2.csv'
        f = open(file, "a")
        f.write("a,1,2,3,4,5")
        f.close()
        oss.occ_stats().Parse_file_to_tuple(file)
        my_file = open("tmp2.csv", "r")
        content = my_file.read()
        self.assertEqual(content, ("a,1,2,3,4,5"))
        os.remove(file)

    def test_case20(self):  # checks if find_ranks works correctly
        words = ["a"]
        occur_dict = {'a': (78, 230, 171, 89, 51)}
        n = 1379
        obj = oss.occ_stats()
        obj.set_variables(occur_dict)
        a = obj.find_ranks(words, n)
        self.assertEqual(a, {'a': '78/4986792881682899'})


if __name__ == '__main__':
    unittest.main()


