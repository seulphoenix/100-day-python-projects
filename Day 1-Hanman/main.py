#Step 1 
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
from Hangman_wrds import word_list
from hangman_art import stages,logo
import random
#TO choose a ranfom var from a list 
word = random.choice(word_list)
print(logo)
game_over = False
win = False
blanks =["_" for _ in word]
wrong_let = 0
lives = 6
guess = 0
while not (game_over or win):
    letter = (input("Please Input a letter")).lower()
    guess += 1
        #! Hint : string is not callable so, you have to use str.index() method
        #! Hint  : but index method just retun the First Occurance!
        #! Hint : Can use enumerate
    for index, let in enumerate(word):
        if let == letter :
            blanks[index] = letter
    if letter not in word :
        print("False")
        lives -=1
        print(stages[lives])
        if lives == 0 :
            print("Game Over!")
    print(f"{' '.join(blanks)}")
    if not "_" in blanks or guess == len(word) + 3:
        print("Winner !")
        win = True 
