import threading 
import time
import random
from alive_progress import alive_bar



The_String = 'Hello, Luke made me think of this'

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz,!.? "

def idkwhatimdong(Monknum, type_speed):
    monkey_string = ""
    for item in The_String:
        char = chars[random.randint(0,56)]
        if item == char:
            monkey_string += char
        elif item != char:
            break

    if monkey_string == The_String:
        print(Monknum)
        

def main():
    c=0
    size = 1000000000
    with alive_bar(size) as bar:
        for x in range(0,size):
            idkwhatimdong(c,0)
            c+=0
            bar()


main()




"""
for x in range(0,15):
    t = threading.Thread(target=main)
    t.start()
    time.sleep(0.1)
"""


