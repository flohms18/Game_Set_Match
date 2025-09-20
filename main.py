import random

def Referee():
    Score = ["0","15","30","40","A"]

    ScoreP1 = 0;
    ScoreP2 = 0
    GameP1 = 0
    GameP2 = 0

    Point = random.randint(0,1)
    print(Point)

    while ScoreP1 != 4 or ScoreP2 != 4:
        if Point == 0:
            ScoreP1 += 1
            print(f"Score : {Score[ScoreP1]} -- {Score[ScoreP2]}")
        else :
            ScoreP2 += 1
        
            print(f"Score : {Score[ScoreP1]} -- {Score[ScoreP2]}")
    
    if Point == 4 or Point > 4:
        print("Game")
        
Referee()
