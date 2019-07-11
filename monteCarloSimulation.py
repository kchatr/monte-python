#A Monte Carlo Simulation: A model used to understand and assess the risk and uncertainity in a myriad of fields (i.e.finance, project management, and other forecasting models)
#Player gets to spin an imaginary spinner in a casino. If it is between 52-100, the player wins; if it is between 1-51, the house wins
#The house edge in this game is 2%. For comparison, the lowest house edge in European Roulette is 2.7%.

#Let's see how this plays out.

#import required libraries
import random #random module which allows the generation of random numbers
import matplotlib.pyplot as mplt #matplotlib graphs data and produces a plot

#function in which player spins an imaginary spinner
def spinSpinner():
    spinner = random.randint(1,100) #spinner has values from 1 to 100. A random value is selected from a uniform probability distribution.
    
    if spinner <= 51: #if value is from 1-51 (inclusive), the house wins
        return False
    elif spinner > 51 & spinner <= 100: #if the value is from 52-100 (inclusive), the player wins
        return True
    
#function which simulates each play and outputs the player's net funds    
def play(total_funds, bet_amount, total_plays):
    play_num = [] #the play number (i.e. the x-axis in the plot)
    funds = [] #the player's funds (i.e. the y-axis in the plot)
    final_funds = [] #the amount of money the player ends with
    play = 0
    
    while play <= total_plays:
        if spinSpinner(): #if player wins
            total_funds += bet_amount #add money to player's funds
            play_num.append(play) #add play number to list play_num
            funds.append(total_funds) #add funds to list funds
        else: #if house wins
            total_funds -= bet_amount #subtract money from player's funds
            play_num.append(play) #add play number to list play_num
            funds.append(total_funds) #add total funds to list funds
        play += 1
        
    mplt.plot(play_num,funds) #plot the play_num and the funds to the graph
    final_funds.append(funds[-1]) #append the final element of funds to list final_funds
    return(final_funds) #return the final funds of the player

scenario = 1 #initalize scenario to 1.
#Each scenario is one 'full round' i.e. 1 round = total_plays. By having multiple scenarios, we see the variance in data and how random variables influence the end result, even though the control variables are never altered.
#The more scenarios used, the better.

total_funds_userInput = int(input("How much money do you start with? " + "Please enter a positive integer. ")) #user input for the total funds of the player
total_bet_userInput = int(input("How much money do you bet each turn? " + "Please enter a positive integer. ")) #user input for the amount of money wagered
total_plays_userInput = int(input("How many times would you like to play? " + "Please enter a positive integer. ")) #user input for the number of plays
total_scenarios = int(input("How many scenarios would you like to simulate? " + "Please enter a postitive integer. ")) #user input for amount of scenarios being run
print("The more scenarios you use, the more accurate the model will be, but it will also take longer for the graph to load.")

while scenario <= total_scenarios: #the number indicates the amount of lines that will be drawn in the graph. Each line is one 'full round'
    ending_fund = play(total_funds_userInput, total_bet_userInput, total_plays_userInput)
    scenario += 1

mplt.xlabel('Number of bets') #sets x-axis label
mplt.ylabel('Player\'s money in $') #sets y-axis label
mplt.show() #displays the graph

print("You started the game with $10,000 and ends with $" + str(sum(ending_fund)/len(ending_fund)))

#On average, the amount lost in every scenario is aproximately 2% of the amount the player bets (bet_amount) - the same as the house edge
#Jack has a better chance of minimizing his losses and turning a profit by placing fewer bets (reducing total_plays)

#The house always wins.
