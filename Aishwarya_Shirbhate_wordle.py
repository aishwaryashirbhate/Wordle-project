# Homework Assignment 02
# from Aishwarya Shirbhate 20005242
# pseudocode #

# Define a function with given word and guessed word as input
# In word guesser function {
# initialise position of letter in word a 0 and clue as 0
# start a for loop to check if position of given word and guessed word is same or not
#  if position is same and letter is same
#    then green is printed in place of that particular letter
#  else if position is same and letter is different
#     then yellow is printed in place of that particular letter
#  else,
#      print __
#  increment the position
#  return the clue
#  end
#   }
#
#  Initialise variables maximum attempts and user inputs.
#  Define symbol list which needs to be excluded from the user input.
#  In the main function {
#  While maximum attempts < 6,
#     ask for user input.
#  if length of user input is 5,
#    if symbols not in user input
#      if user input is uniquer than previous responses,
#            call wordguesser function
#      else print prompt "Provided word is used previously. Please enter a new word"
#    else print prompt "Input word contains symbols/characters. Please input words with alphabets only"
#  else print prompt "Input word length needs to be 5 alphabets long"
#
#  if all alphabets are in correct order,
#       game is over. print 'Woah! You guessed it right in attempt" with maximum attempts used to the user
#  if input word is not same as given word
#     then continue function till maximum attempts are <= 6
#  else game is over. print "You have used up your guesses" and the correct word to the user.
#  end
# }

# Wordle code
print("*** WORDLE GAME ***")

# list of instructions/rules for this game
print("INSTRUCTIONS:\n 1]Guess a five letter word in 6 guess attempts \n 2]Input a word to guess")
print(" 3]Green indicates correct letter at correct position \n 4]Yellow indicates correct letter in wrong position"
      "\n 5]__ indicates wrong letter \n")
print("RULES: \n 1]Only Alphabets can be used in input word \n 2]No Symbols/Numbers are allowed in input word "
      "\n 3]Input word needs to be strictly 5 letters long "
      "\n 4]Enter unique word to guess. Re-using same word will throw error \n")

# function to guess correct word
def wordguesser(theanswer, theguess):
    position = 0
    clue = ""
    for letter in theguess:
        if letter == theanswer[position]:
            clue += "-GREEN-"
        elif letter in theanswer:
            clue += "-YELLOW-"
        else:
            clue += "-__-"
        position += 1
    print(clue)
    return clue == "-GREEN--GREEN--GREEN--GREEN--GREEN-"

# fixed input constraints


answer = "sonar"

symbol_list = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}',
               '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/', '1', '2', '3', '4', '5', '6', '7', '8', '9',
               '0'}
# array for user input
user_inputs = []

maximum_guesses = 0
correct_guess = False

# while loop for maximum guesses
while maximum_guesses < 6 and not correct_guess:
    guess = input("Please enter a 5 letter word and press Enter:")
    print("Word you have entered to guess is", guess)
    res = [ele for ele in symbol_list if (ele in guess)]
    bool_res = bool(res)

    if len(guess) == 5:
        if bool_res is False:
            if guess not in user_inputs:
                user_inputs.append(guess)
                maximum_guesses += 1
                lower_guess = guess.lower()
                correct_guess = wordguesser(answer, lower_guess)  # calling above function
            else:
                print("Provided word is used previously. Please enter a new word")
        else:
            print("Input word contains symbols/characters. Please input words with alphabets only")
    else:
        print("Input word length needs to be 5 alphabets long")

if correct_guess:
    print("Woah! You guessed it right in attempt", maximum_guesses)
else:
    print("You have used up your guesses")
    print("The correct answer is", answer)
