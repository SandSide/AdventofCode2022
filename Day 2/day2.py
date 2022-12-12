f = open('input.txt' ,'r')

oppPlays = ["A", "B", "C"]

playerPlays = ["X", "Y", "Z"]
playerRoundOutcome = ["loss", "draw", "win"]


########## REFRENCES ##########
# X for A (ROCK)
# Y for B (PAPER)
# Z for C(Scissors)

# Value for Each
# X 1 
# Y 2
# Z 3

# Lost 0
# Draw 3
# Won 6

def player_hand_value(hand):
    if hand == 'X':
        return 1
    elif hand == 'Y':
        return 2
    elif hand == 'Z':
        return 3


def compare_hands(opponent, player):

    print('{} vs {}'.format(opponent, player))

    score = player_hand_value(player)

    oppIndex = 0
    playerIndex = 0

    for index, value in enumerate(oppPlays):
        if opponent == value:
            oppIndex = index

    for index, value in enumerate(playerPlays):
        if player == value:
            playerIndex = index

    temp = (int(oppIndex) + 1) % 3

    # print("{} + 1 % 3 ===> {}".format(oppIndex, temp) )    

    if playerIndex == oppIndex:
        outcome = "draw"
        return score + 3
    elif playerIndex == temp:
        outcome = "win"
        return score + 6
    else:
        outcome = "loss"
        return score



def get_score(opp, player):
    
    print('{} vs {}'.format(opp, player))

    # Round outcome
    outcome = ""
    score = 0

    for index, value in enumerate(playerPlays):
        if player == value:
            outcome = playerRoundOutcome[index]

    print(player + ": " + outcome)

    oppIndex = 0
    for index, value in enumerate(oppPlays):
        if opp == value:
            oppIndex = index



    if outcome == "draw":
        print("draw index " + str(oppIndex))
        print("Need to Play: " + playerPlays[oppIndex])
        score = player_hand_value(playerPlays[oppIndex]) + 3

    elif outcome == "win":
        winIndex = (int(oppIndex) + 1) % 3
        print("win index " + str(winIndex))
        print("Need to Play: " + playerPlays[winIndex])
        score =  player_hand_value(playerPlays[winIndex]) + 6

    else:
        loseIndex = (int(oppIndex) - 1) % 3
        print("loss index " + str(loseIndex))
        print("Need to Play: " + playerPlays[loseIndex])
        score = player_hand_value(playerPlays[loseIndex])


    print(score)
    print("\n")
    return score

        
    


totalScore = 0

for line in f:
    values = line.strip().split(' ')
    # totalScore += compare_hands(values[0],values[1])
    totalScore += get_score(values[0],values[1]);

print(totalScore)