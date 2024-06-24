import random


def getword():
    #choose a random word from file 
    with open('words.txt', 'r') as file:
        wordchecker=[word.strip() for word in file.readlines()]
        currword=list(random.choice(wordchecker)) #random word is chosen
        return currword, wordchecker
        
        
#wordle logic
def check(currword, wordchecker):
    guess_common=[]
    
    #check if word is valid or not
    while True:
        guess1=(input("Enter your guess (5 lettered word) or type 'no' to exit: ").lower())
        guess=list(guess1)
        if guess1=='no':
            exit()
        
        elif(len(guess1) != 5):
            print("ay man don't make ur life hard, just enter a 5 lettered word\n")
        
        elif(guess1 not in wordchecker):
            print("what is this man, don't make up your own words. \n")
        
        else:
            break
    
   
    #Checks common letters
    matched=set()
    for i in range(len(currword)):
        if currword[i]==guess[i]:
            guess_common.append(currword[i])
            matched.add(i)
        
        elif currword[i] in guess and guess.count(currword[i]) > guess_common.count(currword[i]):
            guess_common.append('1')
        
        else: guess_common.append('_')
    
    print(guess)
    print(guess_common)
    return guess_common


#main
def main():
    i=0
    print("---------\n5 lettered word\n_ means not a correct letter\n1 means letter is correct but not at the right position\n'letter' means correct position\nYou get 6 chances to guess the correct word\n")
    currword, wordchecker = getword()
    guess_common=[]
    attempts = 6
    
    print(currword)

    for i in range(attempts):
        guess_common = check(currword, wordchecker)
        if guess_common == currword:
            print("Yay, you won! Congratulations!!")
            break
        print(f"Guesses left: {attempts - i - 1}\n")
    
    else:
        print(f"Sorry, you've run out of guesses. The word was: {''.join(currword)}")
    
    
    if input("Play again? yes: ").lower() == 'yes':
        main()
    
    else:
        exit()

   
main()
