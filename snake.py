import curses
import random
import time


def init():
    scr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    scr.keypad(1)
    scr.nodelay(1)
    curses.curs_set(0)
    return scr

def term(scr):                                      # closes cleaning when you press q or when you touch 1 away form the edge
    curses.nocbreak()
    scr.keypad(0)
    curses.echo()
    curses.endwin()

def snake(postions, eat,scr):                   # it makes the snake 
    scr.erase()
    scr.addstr(postions[0] ,postions[1], " " * eat , curses.A_REVERSE)          #the eat term is so when we hit the "mouse" the line grows in size
    scr.addch(postions[2], postions[3]," ", curses.A_REVERSE)        # spot to be eaten
    scr.refresh 

def checkkey (key,postions,ea,scr,dire):
    if key == 113:                                                  # q to exit
        postions[4] = 1
    elif key == 100:                                                  # moves right
        dire = "right"
    elif key == 119:                                                   # moves up
        dire = "up"
    elif key == 115:                                                  # moves down
        dire = "down"
    elif key == 97:                                                   # moves left
        dire = "left"
    return dire 
    
def movement(dire):
    if dire == "right":
        mm = [1,0]
    if dire == "left":
        mm = [-1,0]
    if dire == "up":
        mm = [0,-1]
    if dire == "down":
        mm = [0,1]
    return mm    


scr = init() 

def main(scr):
    dim = scr.getmaxyx() 
    maxy = dim[0]
    maxx =  dim[1]

    dire = "right"
    
    #[snake y, snake x, mouse y, mouse x] sets starting postions for snake and mouse
    postions = [dim[0]/2, dim[1]/2, random.randint(1,maxy), random.randint(1,maxx), 0]

    # start at size 1
    ea = 1

    # creates the starting snake
    snake(postions,ea,scr)

    while 1:
        key = scr.getch()         
        time.sleep(0.3) 
        dire = checkkey(key,postions,ea,scr,dire)
        mm = movement(dire)
        
        postions[1] = mm[0] + postions[1]
        postions[0] = mm[1] + postions[0]
        snake(postions,ea,scr)

        # quit when q is hit
        if postions[4] == 1:
            break

        # adds one to the string in snake when you reach the random point
        if postions[1] == postions[3] and postions[0] == postions[2]:
            ea +=1
            postions[2] = random.randint(1,maxy)
            postions[3] = random.randint(1,maxx)
        
        # ends game when you hit a border to avoid crashing 
        if postions[1]  == dim[1]-1 or postions[0] == dim[0]-1 or postions[1] == 1 or postions[0] == 1:
            break

    term(scr)

main(scr)
