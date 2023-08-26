from turtle import Turtle

colors = ['red','red','orange','orange','green','green','yellow','yellow']
y_cors = [450,434,418,402]

class Bricks(Turtle):
    def __init__(self):
        super().__init__()
        self.bricks = []
        for row in range(8):
            for column in range(8):
                brick = Turtle()
                brick.speed(0)
                brick.shape("square")
                brick.color(colors[row])
                brick.shapesize(stretch_wid=1, stretch_len=4)
                brick.penup()
                x = -350 + column * 100
                y = 430 - row * 40
                brick.goto(x, y)
                self.bricks.append(brick)




