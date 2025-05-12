#Wap to check if any 2 players of 2 teams A & B got the score more than 3 , then that team will win
#team A = player 1 , players 2
#team B = player 3 , player 4
#total score =5

player1=2
player2=0
player3=3
player4=2

if player1>=3 or player2>=3:
    print('Team A has won the match')
elif player3>=3 or player4>=3:
    print('Team B has won the match')
else: 
    print('Draw match')