from random import randint

if __name__ == '__main__':
    print("""This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!\n""")
    target = randint(0, 100)
    tries = 0
    while(tries < 7):
        guess = input("What's your guess between 1 and 99 ?\n")
        if guess == 'exit':
            exit('Aurevoir.')
        if not guess.isdigit():
            print("That's not a number.")
            tries += 1
            continue
        if target == int(guess):
            if target == 42:
                print("The answer to the ultimate question of life, the universe and everything is 42.")
            if tries == 0:
                print("Congratulations! You got it on your first try!")
            else:
                print("Congratulations, you've got it!\nYou won in 5 attempts!")
            tries = 0 if tries < 5 else tries - 5
            target = randint(0, 100)
        else:
            print("Too high!" if int(guess) > target else "Too low!")
            tries += 1
    print(":::::::::::::::::::::::::", ":::.GAME OVER.::( -_-')::", ":::::::::::::::::::::::::", sep='\n')