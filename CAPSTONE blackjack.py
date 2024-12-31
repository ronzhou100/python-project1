import random

logo = r"""
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/     
"""

#create a function that returns a random card from the cards list.
def deal_card():
    """returns a random card from the cards list"""
    #11 is ace
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    random_card = random.choice(cards)
    return random_card

#create a function called calculate_score() that takes a list of cards as input and returns the sum of all the cards in the list as the score.
def calculate_score(list):
    """returns the sum of the inputted list"""
    #inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10 and return 0 instead of the actual score. 0 will represent blackjack in our game.)
    if sum(list) == 21 and len(list) == 2:
        return 0
    #inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
    elif sum(list) > 21 and 11 in list:
        list.remove(11)
        list.append(1)
    return sum(list)

#create a function called compare() and pass in the user_score and computer_score.
def compare(user_score, computer_score):
    #if the computer and user both have the same score, then it's a draw.
    if user_score == computer_score:
        return "It's a Draw!"
    #if the computer has blackjack(0), then the user loses.
    elif computer_score == 0:
        return "Lose, opponent has a blackjack!"
    #if user has a blackjack(0), then the user wins.
    elif user_score == 0:
        return "You win with a blackjack!"
    #if user goes over 21, use loses.
    elif user_score > 21:
        return "Lose, you went over 21."
    #if computer goes over 21, computer loses.
    elif computer_score > 21:
        return "You win, opponent went over 21." 
    #if none of the above, user with the highest score wins.
    elif user_score > computer_score:
        return "You win"
    else:
        return "Lose"

#this function plays the game of blackjack
def play_game():
    #print logo
    print(logo)
    #deal the computer and user 2 cards each using deal_card() and append.
    user_cards = []
    computer_cards = []
    is_game_over = False

    #append 2 random cards to user and computer's hand. **INITIAL SETUP**
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    #the score will need to be rechecked with every new card drawn and the checks need to be repeated until the game ends.
    while not is_game_over:

        #call the function calculate_score(). If the computer or the user has a blackjack(0) or if the user's score is over 21, then the game ends.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, Current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        #if the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards list.
        #if no, the game has ended.
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    #once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    #reveal final hands.
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    #call the compare function, this should play out the entire game.
    print(compare(user_score, computer_score))

#ask the user if they want to play another game. If they do, clear the console and start a new game.
#do not put input inside a variable or it will never update.
while input("Do you want to play a round of Blackjack? Type 'y' or 'n'. ").lower() == 'y':
    print("\n" * 100)
    play_game()

print("Goodbye!")
