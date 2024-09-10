import random
animals = ['zebra', 'cobra', 'stork', 'penguin', 'shark', 'elephant', 'buffalo', 'whale', 'wolf', 'seal', 'eagle', 'wren', 'horse', 'rattlesnake', 'ape', 'crow', 'tuna']
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
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









Selected_Word = random.choice(animals)
display1 = ""
for letters in Selected_Word:
    display1 += "_ "
print(f"This is Your Word, {display1}")
saved = []
lives = 7
game_over = False
while game_over != True:
    display2 = ""
    letter_guessed = input("Try to guess the letters!:\n")   

    for letters2 in Selected_Word:
        if letters2 == letter_guessed:
            display2 += letters2
            saved.append(letters2)
        elif letters2 in saved:
            display2 += letters2
        else:
            display2 += "_ "
            
    if letter_guessed not in Selected_Word:
        lives -= 1
        print(lives)
    if "_ " not in display2:
        game_over == True
    print(display2)





