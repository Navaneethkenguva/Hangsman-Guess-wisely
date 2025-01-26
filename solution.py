import random

word_list = [
    # Animals
    "dolphin", "elephant", "leopard", "penguin", "buffalo",
    "cheetah", "kangaroo", "flamingo", "octopus", "platypus",

    # Fruits & Vegetables
    "apricot", "spinach", "zucchini", "asparagus", "blueberry",
    "eggplant", "avocado", "pineapple", "broccoli", "cucumber",

    # Countries
    "finland", "germany", "portugal", "morocco", "zimbabwe",
    "malaysia", "slovakia", "hungary", "thailand", "indonesia",

    # Professions
    "architect", "engineer", "pharmacist", "mechanic", "detective",
    "plumber", "designer", "electrician", "scientist", "biologist",

    # Nature
    "volcano", "rainbow", "glacier", "tundra", "canyon",
    "hurricane", "mountain", "tsunami", "sandstorm", "ecosystem",

    # Miscellaneous
    "lantern", "compass", "alphabet", "bicycle", "balloon",
    "stadium", "festival", "anchor", "treasure", "galaxy"
]


lives = 6

game_logo = r"""
 _                                              
| |                                             
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
"""
print("welcome to")
print(game_logo)

chosen_word = random.choice(word_list)


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"lives left are {lives}")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"{guess} is already guessed")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)



    if guess not in chosen_word:
        print(f"The letter {guess} is not in the word")
        lives -= 1

        if lives == 0:
            game_over = True
            print(f"YOU LOSE and the correct word is:{chosen_word}")

    if "_" not in display:
        game_over = True
        print("YOU WIN")

    stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
    print(stages[lives])
