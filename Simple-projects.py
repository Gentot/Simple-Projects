#project hangman

import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
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
  |   |
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
      |
      |
      |
      |
=========''']
logo=''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       '''

lives=6
print(logo)
wordlists= [
    "apple",
    "banana",
    "cherry",
    "date",
    "elderberry",
    "fig",
    "grape",
    "honeydew",
    "kiwi",
    "lemon",
    "mango",
    "nectarine",
    "orange",
    "peach",
    "quince",
    "raspberry",
    "strawberry",
    "tangerine",
    "ugli",
    "watermelon",
    "apricot",
    "blueberry",
    "coconut",
    "dragonfruit",
    "guava",
    "jackfruit",
    "kumquat",
    "lychee",
    "melon",
    "papaya",
    "pineapple",
    "pomegranate",
    "rambutan",
    "soursop",
    "tamarind",
    "avocado",
    "blackberry",
    "cantaloupe",
    "durian",
    "gooseberry",
    "lime",
    "mandarin",
    "passionfruit",
    "persimmon",
    "plum",
    "starfruit",
    "yuzu",
    "acorn",
    "bamboo",
    "cedar",
    "daisy",
    "elm",
    "fern",
    "ginseng",
    "hickory",
    "iris",
    "juniper",
    "kelp",
    "lotus",
    "maple",
    "narcissus",
    "oak",
    "palm",
    "quinoa",
    "rose",
    "spruce",
    "tulip",
    "violet",
    "willow",
    "yew",
    "zinnia",
    "badger",
    "cheetah",
    "dolphin",
    "eagle",
    "flamingo",
    "gazelle",
    "hyena",
    "iguana",
    "jaguar",
    "koala",
    "lemur",
    "meerkat",
    "narwhal",
    "ostrich",
    "panda",
    "quail",
    "raccoon",
    "sloth",
    "tiger",
    "urchin",
    "vulture",
    "walrus",
    "xerus",
    "yak",
    "zebra",
    "amethyst",
    "bronze",
    "copper",
    "diamond",
    "emerald",
    "gold",
    "iron",
    "jade",
    "nickel",
    "onyx"
]
chosen=random.choice(wordlists)


placeholder=""
word_length=len(chosen)
for position in range(word_length):
    placeholder+="_"
print(f"Word to guess:{placeholder}")
#users input

gameover = False
correct_letters = []


while not gameover:
    guess=input("Guess a letter:").lower()
    display=""
    if guess in correct_letters:
        print(f"you've already guessed {guess}")

    for letter in chosen:
        if letter == guess:
            display += letter
            correct_letters.append(guess)    
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)
    

    if guess not in chosen:
        lives -= 1
        print(f"you have guessed {guess}, that is not in the word. you lose a life")
        if lives == 0:
            gameover =True
            print(f"You lose, the word is {chosen}" )
 #step 3
    if "_" not in display:
        gameover = True
        print("Congratulations!! You win\n")
        print("Thanks for playing!")
    print(stages[lives])
