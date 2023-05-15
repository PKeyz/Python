"""
Hangman Game
"""

"""
1.have a list of random words and choose one from the list to play the game
2.hangman ascii art for print / create a list of hangman symbols to iterate over
3.Ask user input for letter 
4.display amount of "_" for len(word)
5 while counter < hangman[]  Guess a letter: if letter in word : show all instances / else: counter +1 , print hangman[counter]
5 if letter in word[] display all letter in another array/string -> 1) array word_hidden -> 2) word_display -> 3)hangman_array
5 when counter == len(hangman) - "Game Over, Try again!"
@each letter toLowerCase() in both word array and input for comparisson
@display 1st letter asCapitalLetter()
@if more than 1 letter input - counter +1, if letter = number - counter +1 
"""
import random


#1.have a list of random words and choose one from the list to play the game

word_list=["bikes","crook","year","idea","birthday","fairies","wish","guide","drop","sun",
           "fact","carriage","baby","jelly","coal","man","advice","stretch","car","rock",
           "chicken","lamp","connection","color","rod","hammer","basketball","seed","sort",
           "reading","nest","waves","camp","waste","smoke","grade","ring","yam","wing","turn",
           "mouth","expert","furniture","school","notebook","badge","basin","motion","place",
           "calculator","ant","baboon","badger","bat","bear","beaver","camel","cat","clam","cobra",
           "cougar","coyote","crow","deer","dog","donkey","duck","eagle","ferret","fox","frog",
           "goat","goose","hawk","lion","lizard","llama","mole","monkey","moose","mouse","mule",
           "newt","otter","owl","panda","parrot","pigeon","python","rabbit","ram","rat","raven", 
            "rhino","salmon","seal","shark","sheep","skunk","sloth","snake","spider","stork","swan",
            "tiger","toad","trout","turkey","turtle","weasel","whale","wolf","wombat","zebra"]
random_number = random.randint(0,len(word_list)-1)

random_word = word_list[random_number]
random_array = list(random_word)
#2.hangman ascii art for print / create a list of hangman symbols to iterate over

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#introduce the game
print("""
We're playing:
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
""")
#counter to follow up with the game
counter = 0

#print the hangman status
print(HANGMANPICS[counter])

#4.display amount of "_" for len(word)
underscores = "_" * len(random_array)
underscores_array = list(underscores)
print(f"The word is: {underscores}\n")

#3.Ask user input for letter 

user_letter = input("Guess a letter: ").lower()

#if more than 1 letter input - counter +1, if letter = number - counter +1 
# while counter < hangman[]  Guess a letter: if letter in word : show all instances / else: counter +1 , print hangman[counter]
# if letter in word[] display all letter in another array/string -> 1) array word_hidden -> 2) word_display -> 3)hangman_array
# when counter == len(hangman) - "Game Over, Try again!"



while counter in range(0,8):

#check for letters in random_word
  if user_letter in random_array:
    for letter_iterator in range (0,len(random_array)-1):
      if user_letter == random_array[letter_iterator]:
        underscores_array[letter_iterator] = user_letter
        print()  
  else:
    counter += 1
    print(HANGMANPICS[counter])      
    if counter == 7:
      print("You've lost!\nGame Over!")





