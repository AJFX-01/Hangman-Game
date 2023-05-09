from wordx import wordx 
import random
import string

def main():
    #word = random.choice(wordx)
    get_letter(wordx)
    #get_user_letter()
    print(setts())



def get_letter(wordx):
    word = random.choice(wordx)
    while "-" in word or " " in word:
        word = (random.choice(wordx))
    return word

def get_user_letter():
    while True:
        try:
            user_letter = input(str("Guess Letter:")).lower()
            if len(user_letter) == 1 and user_letter.isalpha():
                break
        except:
            pass
    return user_letter
 

def setts():
    alphabet = set(string.ascii_lowercase)
    alphabet2 = (string.ascii_lowercase)
    guessed_letter = set()
    word = get_letter(wordx)
    word_letters = set(word)
    chances = 10
    score = 0

    while len(word_letters) > 0 and chances > 0:

        # already guessed letter 
       
        print(" ")
        print("YOU HAVE" , chances ,"chances left")
        print("")
        print("YOU Scored", score)
        print("")
        print("You Have Use these letter: ", " ".join(guessed_letter))
        print("")
        
        if score > 2 and len(word) > 5:
            sugget = random.choice(word)
            sugget2 = random.choice(alphabet2)
            print(" ")
            print("suggestions:", sugget, sugget2)
            print("")
        user_letter = get_user_letter()
        # list out the words guessed correctly and dash to represent the rest
        word_list = [letter if letter in guessed_letter else '*' for letter in word]
        print(" ")
        print("Current Word: ", " ".join(word_list))
        print("")


        if user_letter in alphabet - guessed_letter:
            guessed_letter.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                score += 1
                chances += 2

            else:
                chances -= 1
                print("Letter not in the word")
    

        elif user_letter in guessed_letter:
            print("You've Used the letter already, Guess Another one")
        else:
            print("Invalid Character")

    if chances == 0:
        print("you lose the word was", word)
    else:
         print("You've guessed correctly", word, "!!")
    return level(score , chances)
 
def level(score, chances):
    if 5 >= score >= 1 and 10 >= chances >= 5:
        return "Meduim"
    elif score > 5 and chances > 10:
        return "High"
    elif score == 0 and chances == 0:
        return "Low"





if __name__ == "__main__":
    main()
