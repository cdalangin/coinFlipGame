# this is a coinflippin game
def coin_flip_game(guess):
    import random
    coin_flip = ["heads", "tails"]
    index = random.randint(0,1)
    if guess == "heads" or guess == "tails":
        if guess == coin_flip[index]:
        print("Your guess was " + guess)
        print("The coin flip was " + coin_flip[index])
            return "You guessed correctly! We stan!"
    elif guess != coin_flip[index]:
        print("Your guess was " + guess)
        print("The coin flip was " + coin_flip[index])
            return "You guessed wrong! Sorry!"

    else: 
        return "This ain't a guess chief"

#print(coin_flip_game("heads"))
#print(coin_flip_game("tails"))
#print(coin_flip_game("blarg"))