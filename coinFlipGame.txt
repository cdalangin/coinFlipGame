# this is a coinflippin game
def coin_flip_game(guess):
    coin_flip = [heads, tails]
    index = random.randint(1,2)
    if guess != heads or guess != tails:
        return "This ain't a guess chief"
    elif guess == coin_flip[index]:
        print("Your guess was " + guess)
        print("The coin flip was " + coin_flip[index])
        print("You guessed correctly! We stan!")
    elif guess != coin_flip[index]:
        print("Your guess was " + guess)
        print("The coin flip was " + coin_flip[index])
        print("You guessed wrong! Sorry!")

print(coin_flip_game(heads))