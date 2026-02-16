from robot import *

while is_free_down() and is_free_right():
    paint()
    move_right()
    paint()
    move_down()