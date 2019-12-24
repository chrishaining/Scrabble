from PyDictionary import PyDictionary
# from nltk import wordnet
import wordlist
import random
# from bs4 import BeautifulSoup

dictionary = PyDictionary()

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key, value in zip(letters, points)}
print(letter_to_points)

player_to_letters = []

def assign_tiles():
     while len(player_to_letters) < 7:
         random_tile = random.choice(letters)
         player_to_letters.append(random_tile)
     return player_to_letters

word = []
def get_word():
    print("Your letters are: {}.".format(player_to_letters))
    word.append(input("Tell me a word using those letters: "))
    return word

def check_word_uses_tiles():
    outcome = ""
    for item in word:
        for letter in item.upper():
            if letter not in player_to_letters:
                outcome += "$"
    if "$" in outcome:
        return False
    else:
        return True

def check_word_is_valid():
    word_string = word[0]
    if dictionary.meaning(word_string):
        return True
    else:
        return False

def score_word():
  point_total = 0
  for item in word:
      for letter in item.upper():
          points = letter_to_points.get(letter)
          point_total += points
  return point_total

#put it all together
def play_round():
    print("Welcome to Scrabble.")
    assign_tiles()
    get_word()
    if check_word_uses_tiles() == True:
        if check_word_is_valid() == True:
            return "Your word uses the tiles correctly and is in the dictionary. Your score is {}.".format(score_word())
        else:
            return "That word isn't in the dictionary."
    else:
        return "That word doesn't use the right tiles."

print(play_round())
