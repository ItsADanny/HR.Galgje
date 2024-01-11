__author__ = 'Danny de Snoo'

usableWord = False

while usableWord == False:
    word = input("Word : ")
    if len(word) > 1:
        usableWord = True

#prepare the global game variables
    #Booleans
game = True
    #Integers
wrongAwnsers = 0
guessedLetters = 0
    #Arrays
wrongLetters = []
letterSpaces = []

#Generate a
for i in word:
    letterSpaces += "_"

#game function
def game_galgje():
    #aquire the global variables inside the function
    global game
    global wrongAwnsers
    global guessedLetters
    global wrongLetters
    global letterSpaces

    rightLetter = False
    print(letterSpaces)
    #Ask the player for a letter input
    guess = input("Guess a letter : ")
    if len(guess) == 1:
        #loop through the letters in the word
        for e in range(len(word)):
            #if the letter is in the chosen word, then update the letter in the location of the letterspace
            #After that print a list with the letters that have already been guessed
            if guess == word[e]:
                letterSpaces[e] = guess
                rightLetter = True
                guessedLetters += 1
                print("Used letters : " + str(wrongLetters))
        #If the guess provided isn't the right letter, then add it as a wrong awnser
        if rightLetter == False:
            #do a small calculation to see how many wrong guesses the player has left
            #after that print a message to the player with the amount of wrong guess and how many he/she has left
            #then print a list of letters that have already been guessed
            wrongAwnsers += 1
            wrongLetters += guess
            wrongAwnsersLeft = 8 - wrongAwnsers
            print("Wrong awnser, you currently have " + str(wrongAwnsers) + " wrong guesses, you have " + str(wrongAwnsersLeft) + " wrong guesses left")
            print("Used letters : " + str(wrongLetters))
        #If the player guessed all the letters in the word, then print a congratulations message and exit the program.
        if guessedLetters == len(word):
            print("Congratulations, you have won the game! The word was: " + word)
            game = False
        #If the player has reached the maximum allowed wrong guesses, then print a game over message and exit the program
        if wrongAwnsers >= 8:
            print("Game over, you have lost. the word was: " + word)
            game = False
    else:
        print("Wrong, you didn't guess with 1 letter, please use only 1 letter")

#run the game
while game:
    game_galgje()