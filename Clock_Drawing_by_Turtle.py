import turtle
from time import sleep
import math
from Linked_Lists_Time_Generator import create_CLL

# Setup turtle screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Turtle Clock Simulation")
screen.setup(width=600, height=600)

# Create a turtle object for drawing the clock face
face_turtle = turtle.Turtle()
face_turtle.hideturtle()
face_turtle.speed(0)  # Max drawing speed

# Create a turtle object for drawing clock hands
hand_turtle = turtle.Turtle()
hand_turtle.hideturtle()
hand_turtle.speed(0)  # Max drawing speed

# Draw the clock face only once
def draw_clock_face():
    # Draw the clock's circumference
    face_turtle.penup()
    face_turtle.goto(0, -250)
    face_turtle.pendown()
    face_turtle.pensize(3)  # Set pen size for circumference
    face_turtle.pencolor("black")  # Set color for circumference
    face_turtle.circle(250)

    # Marking 12, 3, 6, 9 on clock
    positions = [(0, 210), (210, 0), (0, -220), (-220, 0)]
    labels = ['12', '3', '6', '9']

    for i in range(4):
        face_turtle.penup()
        face_turtle.goto(positions[i])
        face_turtle.write(labels[i], align="center", font=("Arial", 24, "normal"))

# Function to draw the clock hands
def draw_hands(hh, mm, ss):
    hand_turtle.penup()
    hand_turtle.goto(0, 0)  # Move to center to draw hands

    # Calculate angles for hands in radians
    sec_angle = math.radians(90 - (6 * ss))  # 360° / 60 seconds
    min_angle = math.radians(90 - (6 * mm))  # 360° / 60 minutes
    hr_angle = math.radians(90 - (30 * (hh % 12) + mm / 2))  # 360° / 12 hours

    # Draw second hand
    hand_turtle.pensize(1)
    hand_turtle.pencolor("red")
    hand_turtle.goto(100 * math.cos(sec_angle), 100 * math.sin(sec_angle))
    hand_turtle.pendown()
    hand_turtle.goto(0, 0)  # Return to center
    hand_turtle.penup()

    # Draw minute hand
    hand_turtle.pensize(4)
    hand_turtle.pencolor("blue")
    hand_turtle.goto(150 * math.cos(min_angle), 150 * math.sin(min_angle))
    hand_turtle.pendown()
    hand_turtle.goto(0, 0)  # Return to center
    hand_turtle.penup()

    # Draw hour hand
    hand_turtle.pensize(6)
    hand_turtle.pencolor("black")
    hand_turtle.goto(80 * math.cos(hr_angle), 80 * math.sin(hr_angle))
    hand_turtle.pendown()
    hand_turtle.goto(0, 0)  # Return to center
    hand_turtle.penup()

# Initial draw of the clock face

def runMain():
    Time_Obj1=create_CLL()

    draw_clock_face()
    try:
        while True:
            hand_turtle.clear()  # This only clears the hands without affecting the clock face
            draw_hands(*Time_Obj1())
            print(Time_Obj1)
            Time_Obj1.tick()
            sleep(0.5)  # Shorter delay for faster updates
    except:# turtle.Terminator:
        print("Turtle graphics window closed.")

    # Keep the window open
    screen.mainloop()
