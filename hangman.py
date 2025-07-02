import random
import os

# Function to clear the console screen for a cleaner look
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ASCII art for the hangman stages
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']

# List of words for the game
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def get_random_word(word_list):
    """Returns a random string from the passed list of strings."""
    word_index = random.randint(0, len(word_list) - 1)
    return word_list[word_index]

def display_board(missed_letters, correct_letters, secret_word):
    """Displays the current state of the game board."""
    print(HANGMAN_PICS[len(missed_letters)])
    print()

    print('Missed letters:', ' '.join(missed_letters))
    
    blanks = '_' * len(secret_word)

    # Replace blanks with correctly guessed letters
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

    # Show the secret word with spaces in between letters
    print('Current word: ', ' '.join(blanks))
    print("-" * 20)


def get_guess(already_guessed):
    """Ensures the player enters a single letter they haven't guessed before."""
    while True:
        guess = input('Guess a letter: ').lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in already_guessed:
            print('You have already guessed that letter. Choose again.')
        elif not 'a' <= guess <= 'z':
            print('Please enter a LETTER.')
        else:
            return guess

def play_again():
    """Asks the player if they want to play again."""
    return input('Do you want to play again? (yes or no) ').lower().startswith('y')


def main():
    """Main function to run the Hangman game."""
    clear_screen()
    print('H A N G M A N')
    missed_letters = []
    correct_letters = []
    secret_word = get_random_word(words)
    game_is_done = False

    while True:
        display_board(missed_letters, correct_letters, secret_word)

        # Let the player enter a letter.
        guess = get_guess(missed_letters + correct_letters)

        if guess in secret_word:
            correct_letters.append(guess)

            # Check if the player has won.
            found_all_letters = True
            for i in range(len(secret_word)):
                if secret_word[i] not in correct_letters:
                    found_all_letters = False
                    break
            if found_all_letters:
                clear_screen()
                print(f'Yes! The secret word is "{secret_word}"! You have won!')
                game_is_done = True
        else:
            missed_letters.append(guess)

            # Check if player has guessed too many times and lost.
            if len(missed_letters) == len(HANGMAN_PICS) - 1:
                clear_screen()
                display_board(missed_letters, correct_letters, secret_word)
                print('You have run out of guesses!\nAfter ' +
                      str(len(missed_letters)) + ' missed guesses and ' +
                      str(len(correct_letters)) + ' correct guesses, the word was "' + secret_word + '"')
                game_is_done = True

        # Ask the player to play again if the game is done.
        if game_is_done:
            if play_again():
                # Reset the game
                missed_letters = []
                correct_letters = []
                game_is_done = False
                secret_word = get_random_word(words)
                clear_screen()
            else:
                break

if __name__ == '__main__':
    main()
