import random

word_list = ["aardvark", "baboon", "camel"]

random_word = random.choice(word_list)
print(random_word)
word = []
for _ in random_word:
    word.append("-") 

print(f"It's a {len(random_word)} letter word can you guess what is it?")
score = 6
game_not_over = True
while game_not_over:
    if "-" in word:
        user_guess = input("Guess a letter\n")
        if user_guess in word:
            print("You have already guessed this letter.Try another letter")
        else:
            for i in range(len(random_word)):
                if random_word[i] == user_guess:
                    word[i] = user_guess
        print(" ".join(word))
        if user_guess not in random_word:        
            score -=1
            print("You guessed a wrong letter")        
            if score == 0:
                print('You have no more lives.\nYou lose')
                game_not_over = False
    else:
        print('You won')
        game_not_over = False
