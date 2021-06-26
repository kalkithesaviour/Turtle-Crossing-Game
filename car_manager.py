import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []
        self.create_cars()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        for i in range(30):
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.penup()
            new_car.goto(random.randint(300, 1000), random.randint(-250, 250))
            self.car_list.append(new_car)

    def move(self):
        for car in self.car_list:
            if car.xcor() < -300:
                car.goto(random.randint(300, 600), random.randint(-250, 250))
            car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
