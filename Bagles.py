'''A deductive logic game where you must guess a number based on clues.'''
import random

NUM_DIGITS = 3
NUM_GUESSES = 10

def main():
  print(''' I am thinking of a {}-digit number with no repeated digits.
  Try to guess what it is. Here are some clues:
  When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.
  For example, if the secret number was 248 and your guess was 843, the
  clues would be Fermi Pico.'''.format(NUM_DIGITS))

  
  while True:
    '''Guess game starts'''
    secretNum = getSecretNum()
    print("Guess the secret number")
    print("You have {} guesses to get it right!".format(NUM_GUESSES))

    numGuesses = 1
    while numGuesses<=NUM_GUESSES:
      guess =  ""
      while(len(guess)!=NUM_DIGITS or not guess.isdecimal()):
        print("Guess:{}".format(numGuesses))
        guess=input('> ')
        clues = getClues(guess,secretNum)
        print(clues)
        numGuesses+=1

        if(guess==secretNum):
          break
        if(numGuesses>NUM_GUESSES):
          print("You ran out of guesses")
          print("The answer was {}".format(secretNum))

    print("Do you wanna play again?(yes or no)")
    wanna_play = input('> ')
    if wanna_play.lower()!='yes':
      break


  print("Thanks for playing!")
    




def getSecretNum():
  """Returns a string made up of NUM_DIGITS unique random digits."""
  listOfNums = [0,1,2,3,4,5,6,7,8,9]
  random.shuffle(listOfNums)
  secretNum = ""
  for i in range(NUM_DIGITS):
    secretNum+= str(listOfNums[i])
  return secretNum



def getClues(guess,secretNum):
  """Returns a string with the pico, fermi, bagels clues for a guess
  and secret number pair."""
  if guess== secretNum:
    return "You Got it bondhu!"
  
  clues = []
  for i in range(len(guess)):
    if(guess[i]==secretNum[i]):
      clues.append("Fermi")
    elif guess[i] in secretNum:
      clues.append("Pico")
  
  if(len(clues)==0):
    return 'Bagels'
  else:
    clues.sort()
    return ' '.join(clues)

if __name__ == '__main__':
  main()

  

