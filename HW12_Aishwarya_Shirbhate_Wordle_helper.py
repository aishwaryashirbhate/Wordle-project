# Homework Assignment 10
# from Aishwarya Shirbhate 20005242
import csv
from operator import itemgetter


class List:
    def __init__(self, val):
        self.next = None
        self.val = val


class Wordle_Helper:
    def __init__(self, good, bad):
        self.good = good
        self.bad = bad

    def create_linked_list(self, clue, guess):
        h = List(0)
        t = h
        for i in range(5):
            p = List((clue[i], guess[i]))
            h.next = p
            h = p
        return t.next

    def get_good_bad_letters(self, clue, guess):
        print("Please enter good letters")
        good_list = list(input())
        print("Please enter bad letters")
        bad_list = list(input())

        for i in good_list:
            if i in bad_list:
                bad_list.remove(i)

        return good_list, bad_list + self.bad

    def top_fifty(self):
        n = 51

        get_columns = itemgetter('rank', 'words')
        with open('wordRank.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile.readlines()[0:n])
        return [get_columns(row) for row in reader]

    def find_words(self, clue, guess):
        head = self.create_linked_list(clue, guess)
        get_columns = itemgetter('rank', 'words')
        # itemgetter returns a callable object that fetches item from its operand
        words = []
        r = []
        with open('wordRank.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile.readlines()[0:])

            [words.append(get_columns(row)) for row in reader]
        good, bad = self.get_good_bad_letters(clue, guess)
        if not good and not bad:
            return self.top_fifty(), good, bad

        for rank, word in words:
            flag = True
            c = 0
            for i in range(len(word)):
                if good:
                    if word[i] in good:  # check if letter exits in good letter
                        c += 1
            if c != len(good):
                flag = False

            for i in range(len(word)):
                if bad:
                    if word[i] in bad:  # check if letter exits in good letter
                        flag = False
                        break

            if flag:
                t = True
                for j in range(
                        len(word)):  # here means all good letters are taken now we check green position letters too
                    if clue[j] == " ":
                        if word[j] != guess[j]:
                            t = False
                            break
                if t:  # all 3 checks pass then add
                    r.append(word)
        return r, good, bad

# if __name__ == '__main__':
# FOR TESTING
# Wordle_Helper().find_words("```\"\"", "honey")
