import curses
import random

def init():
    scr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    scr.keypad(1)
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

def checkkey (key,postions):
    if key == 113:                                                  # q to exit
        postions[4] = 1

    elif key == 100:                                                  # moves right
        postions[1] +=1
        snake(postions,ea,scr)
        
    elif key == 119:                                                   # moves up
        postions[0] -= 1
        snake(postions,ea,scr)

    elif key == 115:                                                  # moves down
        postions[0] += 1
        snake(postions,ea,scr)

    elif key == 97:                                                   # moves left
        postions[1] -=1
        snake(postions,ea,scr)

    return postions 
    
scr = init() 

dim = scr.getmaxyx() 
maxy = dim[0]
maxx =  dim[1]

#[snake y, snake x, mouse y, mouse x]
postions = [dim[0]/2, dim[1]/2, random.randint(1,maxy), random.randint(1,maxx), 0]

#screen values for mouse postions.

ea = 1                                                           # start at size 1

snake(postions,ea,scr)                                         # creates the starting snake


while 1:
    key = scr.getch()         

    postions = checkkey(key,postions)

    if postions[4] == 1:
        break
    
    if postions[1] == postions[3] and postions[0] == postions[2]:                                    # adds one to the string in snake when you reach the random point
        ea +=1
        postions[2] = random.randint(1,maxy)
        postions[3] = random.randint(1,maxx)
 
    if postions[1]  == dim[1]-1 or postions[0] == dim[0]-1 or postions[1] == 1 or postions[0] == 1:             # ends game when you hit a border to avoid crashing 
        break

term(scr)

