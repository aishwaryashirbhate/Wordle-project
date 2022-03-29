# Homework Assignment 07
# from Aishwarya Shirbhate 20005242
import sys
from csv import writer


def occurrence_stats() -> None:
    """
    function to calculate occurrence statistics:occurrence statistics of each
    letter at a particular index from the filtered dictionary.
    letter likelihood is obtained by counting the number of times a particular letter appears
    in a given index and divide the count by the number of dictionary words
    Results should be stored in the letterFrequency.csv
    """
    try:
        occurrence_dict = {}
        for i in range(97, 123):  # taking  ASCII values of alphabets
            occurrence_dict[chr(i)] = [0, 0, 0, 0, 0]  # initialise dictionary with each alphabet and position list

        try:
            wordlist = open("5letterwords.txt", "r")  # opens filtered dictionary
        except:  # catches error if file is not present
            print("Error:", sys.exc_info()[0], " no file found with name 5letterwords.txt")

        words = [word for word in wordlist.read().split()]
        total_words = len(words)  # calculates total number of words in filtered dictionary

        # updates occurrence dictionary
        for word in words:
            for i in range(len(word)):
                occurrence_dict[word[i]][i] += 1  # updates occurrence dictionary with letter index

        # writes to letterFrequency.csv file
        with open("letterFrequency.csv", 'a+', newline='') as write_obj:  # opens letterFrequency.csv file
            write_obj.truncate(0)
        for letter in occurrence_dict:  # calls csv file write function
            Add_to_freq_file('letterFrequency.csv', [letter] + occurrence_dict[letter])

        Convert_list_to_tuple(occurrence_dict)  # Prints Converted Tuple
        try:
            Parse_file_to_tuple("letterFrequency.csv")
            # Prints Parsed file to dictionary of tuples
        except:
            print("Error:", sys.exc_info()[0], " letterFrequency.csv not found")

        l = find_ranks(words, occurrence_dict, total_words)

        sorted_list = sorted(l.items(), key=lambda x: eval(x[1]), reverse=True)  # Sort words according to the ranks

        with open("wordRank.csv", 'a+', newline='') as write_obj:
            write_obj.truncate(0)
        Add_to_rank_file("wordRank.csv", sorted_list)  # add ranks of words and weights into csv file
        wordlist.close()
    except:
        print("Error:", sys.exc_info()[0], " in occurrence_stats function")

    return occurrence_dict, total_words, words

def Add_to_freq_file(file_name, list_of_elem) -> None:
    """
    Function to write occurrence stats to .csv file
    :param file_name:
    :param list_of_elem:
    """
    try:
        with open(file_name, 'a+', newline='') as write_obj:  # Open file in append mode
            csv_writer = writer(write_obj)
            csv_writer.writerow(list_of_elem)
    except:
        # catches error if file is not present
        print("Error:", sys.exc_info()[0], "in Add_to_freq_file function")


def Convert_list_to_tuple(d) -> dict:
    """
    Function to convert occurrence dictionary of list to dictionary of tuple
    :param d:
    :return d:
    """
    try:
        for i in d:  # takes input dictionary
            d[i] = tuple(d[i])

        return d
    except:
        print("Error:", sys.exc_info()[0], "in Convert_list_to_tuple function")


def Parse_file_to_tuple(file_name) -> dict:
    """
        Function to parse statistics file to dictionary of tuple
        :param file_name:
        :return d:
    """
    try:
        word_list = open(file_name, "r")
        entries = [word for word in word_list.read().split('\n')]  # opens letterFrequency.csv file
        d = {}
        for entry in entries:
            l = entry.split(',')
            if l[0] not in d:
                d[l[0]] = tuple([int(i) for i in l[1:]])  # parses dictionary of list as dictionary of tuple in csv file

        return d
    except:
        print("Error:", sys.exc_info()[0], "in Parse_file_to_tuple function")


def find_ranks(words, occur_dict, n) -> dict:
    """
    Function to calculate ranks of words based on weights calculated
    @param words:
    @param occur_dict:
    @param n:
    @return: ans
    """
    try:
        ans = {}
        for word in words:
            res = 1
            for i in range(len(word)):
                res = res * occur_dict[word[i]][i]  #

            if word not in ans:
                ans[word] = str(res) + '/' + str(n ** 5)

        return ans

    except:
        print("Error:", sys.exc_info()[0], "in find_ranks function")


def Add_to_rank_file(file_name, l) -> None:
    """
    Adds calculated ranks of words rank wise in wordRank.csv file
    @param file_name:
    @param l:
    """
    try:
        for i in range(len(l)):
            with open(file_name, 'a+', newline='') as write_obj:
                csv_writer = writer(write_obj)
                csv_writer.writerow([i + 1] + list(l[i]))
    except:
        print("Error:", sys.exc_info()[0], "in Add_to_rank_file function")


if __name__ == '__main__':
    occurrence_stats()
