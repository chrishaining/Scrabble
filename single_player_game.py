from PyDictionary import PyDictionary
# from nltk import wordnet
import wordlist
import random
from bs4 import BeautifulSoup

dictionary = PyDictionary()

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key, value in zip(letters, points)}

def score_word(word):
  point_total = 0
  for letter in word.upper():
    points = letter_to_points.get(letter)
    point_total += points
  return point_total

player_to_letters = {"Player1": []}

def assign_tiles(player):
     player_letters = player_to_letters[player]
     while len(player_letters) < 7:
         random_tile = random.choice(letters)
         player_letters.append(random_tile)
     return player_letters
# print(assign_tiles("Player1"))
# print(assign_tiles("Player1"))
assign_tiles("Player1")
# print(player_to_letters)

player_words = {"Player1": ""}

# def create_word(player):
#     player_letters = player_to_letters[player]
#     player_word = ""
#     new_word = random.sample(player_letters, 7)
#     for letter in new_word:
#         player_word += letter
#     player_words[player] += player_word
#     return player_word

word = []
def get_word():
    print("Your letters are: {}.".format(player_to_letters))
    word.append(input("Tell me a word using those letters: "))
    return word

print(get_word())
# print(word[0])
# print(player_words)

def check_word_is_valid(word):
    word_string = word[0]
    if dictionary.meaning(word_string):
        return "Nice one! {} is in the dictionary.".format(word_string)
    else:
        return "Awww! {} isn't in the dictionary.".format(word_string)

print(check_word_is_valid(word))
# alternative version of checking word is valid (useful if we want the program to only return valid words)
# def check_validity(word):
#     if dictionary.meaning(word):
#         return True
#     else:
#         return False


#expect "That word isn't in the dictionary."
# print(check_word_is_valid("xxxx"))

#Expect "That's a real word."
# print(check_word_is_valid("soup"))

# print(player_words["Player1"])

#Expect "That word isn't in the dictionary."
# print(check_word_is_valid(player_words["Player1"]))


#so, the next step is to add all the valid words to a list. then create a loop to identify the highest score.
    # while check_validity(word) == False:
        # create_word(player)

# print(create_valid_random_word("Player1"))

# player_to_points = {}
#
# def update_points_total():
#   for player, words in player_words.items():
#     player_points = 0
#     for word in words:
#       player_points += score_word(word)
#       player_to_points[player] = player_points
#
# def play_word(player, word):
#   player_words[player].append(word)

# play_word("Player1", "wow")
# play_word("Player2", "chicken")

# print(player_to_words)
# update_points_total()
# print(player_to_points)

# def check_word_meaning(word):
#     try:
#         return dictionary.meaning(word)
#     except Error:
#         return "Sorry, that word isn't in the dictionary."
#
# print(check_word_meaning("ZXX"))

# def check_word_is_in_dictionary(word):
#     # if word in dictionary:
#     if dictionary.meaning(word):
#         return dictionary.meaning(word)
#     else:
#         return "that's fine"
# print(check_word_is_in_dictionary("zxx"))
#Next steps to make this interactive.
# player_to_words should start blank, or should start with blank value
# the user inputs their name (optional - it might be fine just to use player1)
# create a variable (dictionary?) that determines how many tiles of each letter there are - this is optional. it would be easier to have an unlimited number.
# randomly assign tiles to each player. so, this will need to add tiles to a list, which is linked to a player (in a dictionary?)
# the user makes a word. the program should check that the word is valid. valid in this context means it can be constructed from the user's tiles. there is no check to see if it's a real word. but if I can use PyDictionary, it would be so cool.
# the program creates a random word from the letters. I'm not sure if this is worthwhile, as the computer could generate nonsense words. Might be fun though! Alternative - look for a python dictionary package (in this instance I'm using dictionary is the non-python meaning - a book of words). try 'from PyDictionary import PyDictionary'
