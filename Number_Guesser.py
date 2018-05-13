"""
AJH
Python based number game
"""
import random
import sys

class GuessTheNumber(object):
    #Prints user introduction
    def gameIntro(self):
        intro = print("Welcome to the game!\nYour goal is to guess the randomly generated number\n"+
                                  "You will be given hints to triangulate your guesses\nGOOD LUCK!")
        return intro

    #Returns the user's desired ID
    def getUserID(self):
        name = input("What is your name? This will be your user ID")
        return name

    #Generates a dict to be populated by UserID, Guesses, Wins during the gameplay experience
    def generateProfile(self, username):
        profile = {"Name":username, "Guesses":0, "Wins":0}
        return profile

    #Returns the user's desired range of values
    def getRange(self):
        print("You will select the upper range of values you wish to be generated")
        upperLimit = input("Enter your choice. Ex: Enter 100 for a range of 1-100")
        print("Thank you, you have selected "+ str(upperLimit))
        return upperLimit

    #Accepts the user's defined range, generates a random number, returns this number to be used as the "winning" number
    def getNumber(self, numberRange):
        number = random.randrange(1, int(numberRange), 1)
        return number

    #Gameplay logic
    def startGame(self, user, secretNumber, numberRange):
        print("Hello, " + user["Name"] + ", let's begin")
        print("The winning number exists somewhere from 1 to " + str(numberRange))
        playGame = True
        while playGame == True:
            currentGuess = int(input("Please enter a guess"))
            if currentGuess < secretNumber:
                print("Too low!")
                user["Guesses"]+=1
            if currentGuess > secretNumber:
                print("Too high!")
                user["Guesses"]+=1
            if currentGuess == secretNumber:
                print("Winner winner chicken dinner!")
                user["Guesses"]+=1
                user["Wins"]+=1
                print("--Your totals so far are--")
                for x,y in user.items():
                    print(str(x)+":"+str(y))
                playGame = False
                Ratio = user["Guesses"]/user["Wins"]
                print("Average number of guesses per win = " + str(format(Ratio, '.2f')))
                print("This is equal to " + str(format(user["Wins"]/user["Guesses"]*100, '.2f')) + "% accuracy")
                playAgain = input("Play again? Enter Yes to continue, or No to end the program")
                if playAgain == 'Yes' or playAgain == 'yes':
                    numberRange = self.getRange()
                    winningNumber = self.getNumber(numberRange)
                    self.startGame(userProfile, winningNumber, numberRange)
                if playAgain == "No" or playAgain == "no":
                    print("Thank you for playing, it's been a pleasure.")
                    sys.exit(0)

#Main
if __name__ == '__main__':
    start = GuessTheNumber()
    start.gameIntro()
    userName = start.getUserID()
    userProfile = start.generateProfile(userName)
    numberRange = start.getRange()
    winningNumber = start.getNumber(numberRange)
    start.startGame(userProfile, winningNumber, numberRange)
