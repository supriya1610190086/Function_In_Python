def minion_game(string):
    player1 = 0
    player2 = 0
    strlength = len(string)
    for i in range(strlength):
        if GAME_NAME[i] in "AEIOU":
            player1 += (strlength)-i
        else :
            player2 += (strlength)-i
    if player1 > player2:
        print("Kevin", player1)
    elif player1 < player2:
        print("Stuart",player2)
    elif player1 == player2:
        print("Draw")
    else :
        print("Draw")


GAME_NAME = input("GAME_NAME")
minion_game(GAME_NAME)