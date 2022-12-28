import random
from hangman_words import words
from hangman_art import logo
from hangman_art import stages
print(logo)
chosen_word= random.choice(words)
display=[]
underscore="_"
lives=6
for letter in chosen_word:
    underscore="_"
    display.append(underscore)
end_of_game= False
while end_of_game==False:
    guess= input("Guess a letter: ")
    if guess in display:
        print(f"You have already guessed {guess}.")
    for position in range(0,len(chosen_word)):
        letter= chosen_word[position]
        if letter==guess:
            display[position]=letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives-=1
        if lives==0:
            end_of_game= True
            print("You lose")
    print(stages[lives])
    print(f"{' '.join(display)}")
    if underscore not in display:
        end_of_game= True
        print("You win!")




