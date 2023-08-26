from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.pencolor('white')
        self.goto(270,-350)
        self.write(f'Score: {self.score}', font=('Ariel',20,'normal'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', font=('Ariel',20,'normal'))

    def game_over(self):
        self.clear()
        self.goto(-100,0)
        self.pencolor('red')
        self.write(f'GAME OVER! \n Your score: {self.score}', font=('Ariel',25,'bold'))