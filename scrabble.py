from PyDictionary import PyDictionary
# from nltk import wordnet
import wordlist
import random
from bs4 import BeautifulSoup

dictionary = PyDictionary()

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key, value in zip(letters, points)}

# print(letter_to_points)

def score_word(word):
  point_total = 0
  for letter in word.upper():
    points = letter_to_points.get(letter)
    point_total += points
  return point_total

player_to_letters = {"Player1": [], "Player2": []}

def assign_tiles(player):
     player_letters = player_to_letters[player]
     while len(player_letters) < 7:
         random_tile = random.choice(letters)
         player_letters.append(random_tile)
     return player_letters
# print(assign_tiles("Player1"))
# print(assign_tiles("Player1"))
assign_tiles("Player1")
assign_tiles("Player2")
print(player_to_letters)

#creating a word (start by doing this randomly for both players. Later, the parameter player will be unnecessary)
# This should be a random method. There are then various options on how we could do this:
# * the program creates a random word. The only check is that it uses letters from the player's assigned letters. So, it could result in nonsense words
# * the program could do this, along with checking that the word is in PyDictionary/other dictionary package before submitting the word. This would make it very hard to beat the computer. Alternatively, it could submit the word before checking PyDictionary. PyDictionary would then check the word (it would be much easier to beat the computer this way).
# * A problem using the above methods is that the computer will use all seven letters. In real-life Scrabble, it can be better to use only some of the letters (for example, you might find a six-letter word, but no seven-letter word). One way round this might be an if elif loop. If there is a seven-letter word in Pydictionary, use it; elif there is a six-letter word in Pydictionary, use it; etc. This still leaves the problem that a shorter word might generate more points than a longer one. A way round that - assign each possible word to a new list. At the end of the iteration, check which of the words in the list generates the highest score. Use it. We also have to factor in the possibility of unused tiles. The value of these should be subtracted from the score.

player_words = {"Player1": "", "Player2": ""}

def create_word(player):
    player_letters = player_to_letters[player]
    player_word = ""
    new_word = random.sample(player_letters, 7)
    for letter in new_word:
        player_word += letter
    # print(new_word)
    player_words[player] += player_word
    return player_word

print(create_word("Player1"))
print(create_word("Player2"))

print(player_words)

def check_word_is_valid(word):
    if dictionary.meaning(word):
        return "Nice one! {} is in the dictionary.".format(word)
    else:
        return "Awww! {} isn't in the dictionary.".format(word)

# alternative version of checking word is valid (useful if we want the program to only return valid words)
def check_validity(word):
    if dictionary.meaning(word):
        return True
    else:
        return False


#expect "That word isn't in the dictionary."
print(check_word_is_valid("xxxx"))

#Expect "That's a real word."
print(check_word_is_valid("soup"))

print(player_words["Player1"])

#Expect "That word isn't in the dictionary."
print(check_word_is_valid(player_words["Player1"]))

#now that we can create a word (but not necessarily a valid one) and we can check validity, we can combine our functions to create a valid random word. I am playing with a package called wordlist, which might help.
# generator = wordlist.Generator(player_words["Player1"])

def create_valid_random_word(player):
    generator = wordlist.Generator(player_words[player])
    list = []
    for each in generator.generate(1, 7):
        if not dictionary.meaning(each):
            continue
        list.append(each)
    return list
        # print("{each}: {meaning}".format(each=each, meaning=dictionary.meaning(each)))

#so, the next step is to add all the valid words to a list. then create a loop to identify the highest score.
    # while check_validity(word) == False:
        # create_word(player)

# print(create_valid_random_word("Player1"))

player_to_points = {}

def update_points_total():
  for player, words in player_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
      player_to_points[player] = player_points

def play_word(player, word):
  player_words[player].append(word)

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
