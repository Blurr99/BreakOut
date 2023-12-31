from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.fast = 5
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.06561

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def hit(self):
        self.y_move *= -1
        if self.move_speed > 0.04782969:
            self.move_speed *= 0.9