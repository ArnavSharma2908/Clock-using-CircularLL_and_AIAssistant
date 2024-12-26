from os import _exit
from tkinter import _tkinter
from turtle import Terminator
from time import sleep,localtime

try:

    from Linked_Lists_Time_Generator import create_CLL
    from Clock_Drawing_by_Turtle import tracer,setup_clock,show_clock
    from Digital_Representer import display_message
    from Clock_DevBuddy import Chat_with_Dev
    from threading import Thread

    time1 = create_CLL(localtime().tm_hour % 12 or 12, localtime().tm_min, localtime().tm_sec, not(localtime().tm_hour < 12))

    t1 = Thread(target = Chat_with_Dev)
    t1.start()
    delay_correction = 0.0063
    
    display_message("START OF PROGRAM")
    sleep(3)
    tracer(0)
    setup_clock()
    while True:
        show_clock(*time1())
        display_message(time1.__str__())
        sleep(1-delay_correction)
        time1.tick()

except KeyboardInterrupt:
    print('KeyboardInterrupt: Killing Threads')
    _exit(0)

except ModuleNotFoundError as e:
    print(e)
    print('''Required Module is not present
Install the requirements using pip or install the dependencies from available source/repository''')

except _tkinter.TclError:
    print("Exited")
    _exit(0)

except Terminator:
    print("Exited")
    _exit(0)