import turtle
import Snake
import Food
import time
import Scoreboard

screen = turtle.Screen()
screen.setup(600,700)
screen.title("Snake")
screen.tracer(0)

snake = Snake.Snake()
food = Food.Food()
score_game = Scoreboard.Scoreboard()
bool_game = True

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")





def check_collision_with_food():
    if snake.body[0].distance(food)<15 :
        screen.update()
        snake.after_eat()
        score_game.increce_score()
        food.generate_loc()



def check_collision_with_body():
    global bool_game
    for part in snake.body[1:]:
        if snake.body[0].distance(part)<10:
            score_game.reset()
            snake.reset()
            food.generate_loc()




def check_collision_with_walls():
    global game_play
    global bool_game
    x=snake.body[0].xcor()
    y=snake.body[0].ycor()
    if x<-290 or x>290 or y<-340 or y >340:
         score_game.reset()
         snake.reset()
         food.generate_loc()





while(bool_game):
    screen.update()
    time.sleep(0.1)
    snake.move()
    check_collision_with_food()
    check_collision_with_walls()
    check_collision_with_body()





screen.exitonclick()





