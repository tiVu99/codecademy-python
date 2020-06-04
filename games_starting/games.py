import random

money = 100


# Write your game of chance functions here
def coin_flipping(guess, bet):
    if bet <= 0:
        print("Your bet should be above 0")
        return 0

    print("------------------")
    print("Let's flip a coin! You guessed " + guess)
    num = random.randint(1, 2)
    print("------------------")

    if (guess == "Heads" and num == 1) or (guess == "Tails" and num == 2):
        print("Congrats! You won " + str(bet) + " dollars!")
        print("------------------")
        return bet
    else:
        print("Too bad! You lost " + str(bet) + " dollars!")
        print("------------------")
        return -bet


def cho_han(guess, bet):
    if bet <= 0:
        print("Your bet should be above 0")
        return 0

    print('\n')
    print("------------------")
    print("Let's roll the first dice!")
    dice1 = random.randint(1, 6)
    print("The result is " + str(dice1))

    print("------------------")
    print("Let's roll the second dice!")
    dice2 = random.randint(1, 6)
    print("The result is " + str(dice2))

    sum_dice = dice1 + dice2

    print("------------------")
    print("You guessed " + guess + " !")
    print("------------------")

    if (guess == "Even" and sum_dice % 2 == 0) or (guess == "Odd" and sum_dice % 2 != 0):
        print("Congrats! You won " + str(bet) + " dollars!")
        print("------------------")
        return bet
    else:
        print("Too bad! You lost " + str(bet) + " dollars!")
        print("------------------")
        return -bet


def card(bet):
    if bet <= 0:
        print("Your bet should be above 0")
        return 0

    print('\n')
    print("------------------")
    print("Player 1: Let's pick a card!")
    card1 = random.randint(1, 13)
    print("Your card is " + str(card1))

    print("------------------")
    print("Player 2: Let's pick a card!")
    card2 = random.randint(1, 13)
    print("Your card is " + str(card2))

    if card1 > card2:
        print("------------------")
        print("Congrats Player 1! You won " + str(bet) + " dollars!")
        print("------------------")
        return bet
    elif card1 < card2:
        print("------------------")
        print("Congrats Player 2! You won " + str(bet) + " dollars!")
        print("------------------")
        return -bet
    else:
        print("------------------")
        print("It was a tie")
        print("------------------")
        return 0


def roulette(guess, bet):
    if bet <= 0:
        print("Your bet should be above 0")
        return 0

    print('\n')
    print("------------------")
    print("Let's play roulette!")
    print("------------------")
    result = random.randint(0, 37)
    print("The result is " + str(result))

    print("------------------")
    print("You guessed " + guess + " !")

    if guess == "Even" and result % 2 == 0 and result != 0:
        print("------------------")
        print("Congrats! You won " + str(bet) + " dollars!")
        print("------------------")
        return bet
    elif guess == "Odd" and result % 2 != 0 and result != 37:
        print("------------------")
        print("Congrats! You won " + str(bet) + " dollars!")
        print("------------------")
        return bet
    elif result == 37 or 0:
        print("------------------")
        print("Too bad! You lost " + str(bet) + " dollars!")
        print("------------------")
        return -bet
    else:
        print("------------------")
        print("Too bad! You lost " + str(bet) + " dollars!")
        print("------------------")
        return -bet


# Call your game of chance functions here
coin_flipping("Heads", 25)
money += coin_flipping("Heads", 25)
cho_han("Even", 50)
money += cho_han("Even", 50)
card(75)
money += card(75)
roulette("Odd", 100)
money += roulette("Odd", 100)

print('\n')
print("Your money: " + str(money))

