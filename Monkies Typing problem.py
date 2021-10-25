import threading 
import time
import random
from progress.bar import Bar


The_String = 'Luke'

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz,!.? "

def idkwhatimdong(Monknum, type_speed):
    monkey_string = ""
    for item in The_String:
        char = chars[random.randint(0,56)]
        #print(char)
        if item == char:
            monkey_string += char
            #print("in here")
        elif item != char:
            break
     
    #print(monkey_string)
    #print(The_String)
    if monkey_string == The_String:
        print(Monknum)
        

def main():
    c=0
    size = 100000000
    #with Bar(c) as bar:
    for x in range(0,size):
        idkwhatimdong(c,0)
        c+=1
            #bar.next()

main()



#thread.start_new_thread( print_time, ("Thread-1", 2, ) )
#thread.start_new_thread( print_time, ("Thread-2", 4, ) )

