import random
import time
import os

tries = 0
correct = []
incorrect = []
correct_postion = []
game = True
word_list = open("word_list.txt").read().split()
word = random.choice(word_list)

def introduction():
  print("Wordle")
  print("----------------------------------------------------")
  print("In order to play this game, you'll be given a five letter word. You have 6 tries to guess the word.")
  print("If you guess a letter correctly, it will be highlighted green")
  print("If you guess a letter in the wrong place, it will be highlighted yellow")
  print("If you guess a letter incorrectly, the letter will gray")
  print("Good luck!")         


def generate_word():
  wordList = open("word_list.txt").read().split()
  word = random.choice(wordList)
  print(f'Word = ' + '[_]' * len(word))
  return word


def check_word(correct, incorrect, correct_postion, word, tries):
  guess = input('Guess a word: ')
  if len(guess) != 5:
    print('Please enter a 5 letter word')
    return tries, correct, incorrect, correct_postion, False
  else:
    for i in range(len(guess)):
      if guess[i] == word[i]:
        print(f'Nice! {guess[i]} is in the correct position')
        if guess[i] not in correct:
          correct.append(guess[i])
        if i not in correct_postion:
          correct_postion.append(i)
      elif guess[i] in word:
        print(f'{guess[i]} is in the word but in the wrong position')
        if guess[i] not in correct:
          correct.append(guess[i])
      else:
        print(f'{guess[i]} is not in the word')
        if guess[i] not in incorrect:
          incorrect.append(guess[i])
  return tries, correct, incorrect, correct_postion, True


def print_word(word, correct, correct_postion):
  progress = ''
  for i, character in enumerate(word):
    if character in correct and i in correct_postion:
      progress = progress + '\033[92m'+ character + '\033[0m'
    elif character in correct:
      progress = progress + '\033[93m' + character + '\033[0m'
    else:
      progress = progress + '[_]'
  return progress


introduction()

while game:
  correct_postion = []
  correct = []
  incorrect = []
  tries = 0
  word = generate_word()

  while tries < 6:
    tries, correct, incorrect, correct_postion, valid = check_word(correct, incorrect, correct_postion, word, tries)
    time.sleep(1)
    os.system('clear')
    progress = print_word(word, correct, correct_postion)
    print(f'Word = {progress}')
    print(f'Incorrect Guesses = {incorrect}')
    if len(set(correct_postion)) == len(word):
      print('You win! The word was ' + word)
      break
    if valid:
      tries += 1
    if tries >= 6:
      print('You ran out of tries! The word was ' + word)
      break
    print('You have ' + str(6 - tries) + ' tries left')

  start_over = input('Would you like to play again? press y: ')
  if start_over == 'y':
    game = True
    os.system('clear')
  else:
    game = False
