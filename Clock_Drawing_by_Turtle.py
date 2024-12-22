import turtle
from turtle import tracer
import math

def draw_hand(length, angle, color, width):
    turtle.penup()
    turtle.home()
    turtle.pendown()
    turtle.color(color)
    turtle.width(width)
    turtle.setheading(angle)
    turtle.forward(length)
    turtle.penup()
    turtle.home()

def draw_circle(radius):
    turtle.penup()
    turtle.goto(0, -radius)
    turtle.pendown()
    turtle.color("darkblue")
    turtle.width(5)
    turtle.circle(radius)

def setup_clock():
    turtle.reset()
    turtle.speed(0)
    turtle.bgcolor("lightyellow")

    # Draw clock face
    draw_circle(200)
    for i in range(12):
        angle = i * 30
        x = 180 * math.sin(math.radians(angle))
        y = 180 * math.cos(math.radians(angle))
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.dot(15, "darkgreen")
        turtle.penup()
        
        writeup_corrector = 12
        
        turtle.goto(1.2 * x, 1.2 * y - writeup_corrector)
        turtle.write(str(i if i > 0 else 12), align="center", font=("Arial", 16, "bold"))

def validate_time(hour, minute, second):
    if not (1 <= hour <= 12):
        raise ValueError(f"Hour must be between 1 and 12. Provided: {hour}")
    if not (0 <= minute <= 59):
        raise ValueError(f"Minute must be between 0 and 59. Provided: {minute}")
    if not (0 <= second <= 59):
        raise ValueError(f"Second must be between 0 and 59. Provided: {second}")

def show_clock(hour, minute, second): # Analog Clock rendering. This method will be used by Main.py file
    validate_time(hour, minute, second)
    turtle.clear()
    setup_clock()

    correction_factor = 270
    inp_shift = 0

    total_shift = correction_factor + inp_shift
    

    hour_angle = (360 / 12) * (hour % 12) + (minute / 60) * 30 + total_shift
    minute_angle = (360 / 60) * minute + (second / 60) * 6 + total_shift
    second_angle = (360 / 60) * second + total_shift

    draw_hand(100, -hour_angle, "black", 6)
    draw_hand(150, -minute_angle, "blue", 4)
    draw_hand(180, -second_angle, "red", 2)
    turtle.update()


#turtle.done()
