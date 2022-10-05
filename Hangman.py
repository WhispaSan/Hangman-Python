import random
from words import word_list #other file containing word list

# asks for custom word if no picks random using random from the word list
YN = input("""Would you like to use a custom word? (Y/N) """).lower()
if YN == "y":
    def get_word():
        word = input("Please input custom word: ")
        return word.upper()

else:
    def get_word():
        word = random.choice(word_list)
        return word.upper()
    

#this is the main brick of code making the game word as well as having some of the visual promps inculded
def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("please guess letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("you have already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job, ", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You have already guessed the word", guessed_words)
            elif guess != word:
                print(guess, "is not the word")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = word_completion = word
        else:
            ("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You Win!")
    else:
        print("Sorry, you ran out of tries. The word was ", word ,"maybe next time")

# pyrely visuals, these change every wrong answer
def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

#allows the game to loop
if YN == "y":
    word = input
    def main():
        word = get_word()
        play(word)
        while input("""Play Again? (Y/N) """).upper() == "Y":
            word = get_word()
            play(word)

else:
    def main():
        word = get_word()
        play(word)
        while input("""Play Again? (Y/N) """).upper() == "Y":
            word = get_word()
            play(word)

if __name__ == "__main__":
    main()

