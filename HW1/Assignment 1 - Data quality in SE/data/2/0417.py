def playerChoises(playerA, playerB, playerOptions) :
    while True :
        playerAHand = input(
            playerA + " what is your option? \ntype pp for paper, st for stone or sc for scissors\n")
        if playerAHand == playerOptions['paper'] or playerAHand == playerOptions['stone'] or playerAHand == \
                playerOptions['scissors'] :
            break
        else :
            print("Not right, try again!!\n")
    while True :
        playerBHand = input(
            "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n" + playerB + " what is your option? \ntype pp for paper, st for stone or sc for scissors\n")
        if playerAHand == playerOptions['paper'] or playerAHand == playerOptions['stone'] or playerAHand == \
                playerOptions['scissors'] :
            break
        else :
            print("Not right, try again!!\n")
    return (playerAHand, playerBHand)


def playGame(playerAHand, playerBHand, playerOptions) :
    if playerAHand == playerOptions['paper'] and playerBHand == playerOptions['scissors'] :
        return 2
    elif playerBHand == playerOptions['paper'] and playerAHand == playerOptions['scissors'] :
        return 1
    elif playerAHand == playerOptions['scissors'] and playerBHand == playerOptions['stone'] :
        return 2
    elif playerBHand == playerOptions['scissors'] and playerAHand == playerOptions['stone'] :
        return 1
    elif playerAHand == playerOptions['stone'] and playerBHand == playerOptions['paper'] :
        return 2
    elif playerBHand == playerOptions['stone'] and playerAHand == playerOptions['paper'] :
        return 1
    else :
        return 0


def playAgain() :
    _answer = input("Do you want to play again?\n Answer y for YES or n for NO.\n")
    return _answer


def main() :
    playerAHand = None
    playerBHand = None

    playerA = ''
    playerB = ''

    playerOptions = {'paper' : 'pp', 'stone' : 'st', 'scissors' : 'sc'}
    gameOptions = {'yes' : 'y', 'no' : 'n'}

    playerA = input("Hello player one,\nwhats your name?\n")
    playerB = input("Hello player two,\nwhats your name?\n")

    answer = gameOptions['yes']
    result = 0

    print("Let's play!!!")

    while answer == (gameOptions['yes']) :
        (playerAHand, playerBHand) = playerChoises(playerA,playerB,playerOptions)
        result = playGame(playerAHand, playerBHand, playerOptions)
        if result == 1 :
            print("CONGRATULATIONS " + playerA + " \n You're the winner!!!!!!!!!!\n\n")
        elif result == 2 :
            print("CONGRATULATIONS " + playerB + " \n You're the winner!!!!!!!!!!\n\n")
        else :
            print("Even, try again")
        answer = playAgain()


if __name__ == "__main__" :
    main()
