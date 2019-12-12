from PyDictionary import PyDictionary
import random
from bs4 import BeautifulSoup

dictionary = PyDictionary()

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Blank"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]

letter_to_points = {key:value for key, value in zip(letters, points)}

print(letter_to_points)

def score_word(word):
  point_total = 0
  for letter in word.upper():
    points = letter_to_points.get(letter)
    point_total += points
  return point_total


player_to_words = {"Player1": [], "Player2": []}

player_to_points = {}

def update_points_total():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
      player_to_points[player] = player_points



def play_word(player, word):
  player_to_words[player].append(word)

play_word("Player1", "wow")
play_word("Player2", "chicken")

print(player_to_words)
update_points_total()
print(player_to_points)

# def check_word_meaning(word):
#     try:
#         return dictionary.meaning(word)
#     except Error:
#         return "Sorry, that word isn't in the dictionary."
#
# print(check_word_meaning("ZXX"))

def check_word_is_in_dictionary(word):
    # if word in dictionary:
    if dictionary.meaning(word):
        return dictionary.meaning(word)
    else:
        return "that's fine"
print(check_word_is_in_dictionary("zxx"))
#Next steps to make this interactive.
# player_to_words should start blank, or should start with blank value
# the user inputs their name (optional - it might be fine just to use player1)
# create a variable (dictionary?) that determines how many tiles of each letter there are - this is optional. it would be easier to have an unlimited number.
# randomly assign tiles to each player. so, this will need to add tiles to a list, which is linked to a player (in a dictionary?)
# the user makes a word. the program should check that the word is valid. valid in this context means it can be constructed from the user's tiles. there is no check to see if it's a real word. but if I can use PyDictionary, it would be so cool.
# the program creates a random word from the letters. I'm not sure if this is worthwhile, as the computer could generate nonsense words. Might be fun though! Alternative - look for a python dictionary package (in this instance I'm using dictionary is the non-python meaning - a book of words). try 'from PyDictionary import PyDictionary'

# examples of random
# random_list = [random.randint(1, 100) for i in range(101)]

#selects a random tile from the list of letters (or should I select from a dictionary, so I get value?)
# random_tile = random.choice(letters)

#adds random tile to a list/dictionary
