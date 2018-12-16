GAME_SIZE = 4
#SCORE_TO_WIN = 2048

from game2048.game import Game
from game2048.agents import ExpectiMaxAgent

# save the dataset

for i in range(7):
    print("i = ", i)
    f1 = open("0_512.txt", "a")
    f2 = open("512_1024.txt", "a")
    f3 = open("1024_2048.txt", "a")
    for j in range(8):
        print("j = ",j)
        game = Game(score_to_win=2048)
        agent = ExpectiMaxAgent(game=game)
        while True:
            direction = agent.step()
            scr=game.board.max()
            if(scr <= 256):f=f1
            elif(scr == 512):f=f2
            elif(scr == 1024):f=f3  
            if (game.end == 2):
                break
            #print (game.board)
            #print ("direction: ", direction)
            for k in range(4):
                for p in range(4):
                    print(game.board[k, p], file = f)
            print(direction, file = f)    
            game.move(direction)
    f1.close()
    f2.close()
    f3.close()