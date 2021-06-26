from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for car in car_manager.car_list:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 280:
        player.goto(0, -280)
        car_manager.increase_speed()
        scoreboard.increase_level()

    car_manager.move()

screen.exitonclick()
