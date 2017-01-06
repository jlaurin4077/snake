#!/usr/bin/python2



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

# closes te window cleanly
def term(scr):   
    curses.nocbreak()
    scr.keypad(0)
    curses.echo()
    curses.endwin()

def snake(postions, eat,scr,snakelist):     
    #earse the old snake
    scr.erase()
    #draw the new snake
    for piece in snakelist:
        scr.addch(piece[0],piece[1], " ", curses.A_REVERSE)

    #scr.addstr(postions[0] ,postions[1], " " * eat , curses.A_REVERSE)
    # draws the mouse
    scr.addch(postions[2], postions[3]," ", curses.A_REVERSE)     
    scr.refresh 

def checkkey (key,postions,dire,counter):
    #press q to quit the game
    if key == 113:     
        postions[4] = 1
    elif key == 100: 
        dire = "right"
        if counter == -1 :
            counter += 1
    elif key == 119: 
        dire = "up"
        if counter == -1 :
            counter += 1
    elif key == 115: 
        dire = "down"
        if counter == -1 :
            counter += 1
    elif key == 97:  
        dire = "left"
        if counter == -1 :
            counter += 1
    return dire,counter 

def movement(dire):
    if dire == "right":
        mm = [0,1]
    if dire == "left":
        mm = [0,-1]
    if dire == "up":
        mm = [-1,0]
    if dire == "down":
        mm = [1,0]
    return mm    


scr = init() 

def main(scr):
    dim = scr.getmaxyx() 
    maxy = dim[0]
    maxx =  dim[1]
    counter = -1

    snakelist = [[dim[0]/2, dim[1]/2 +2, "right"],[dim[0]/2, (dim[1]/2)  +1, "right"], [dim[0]/2, dim[1]/2, "right"]]
    dire = "right"
    
    #[snake y, snake x, mouse y, mouse x] sets starting postions for snake and mouse
    postions = [dim[0]/2, dim[1]/2, random.randint(1,maxy), random.randint(1,maxx), 0]

    # start at size 1
    ea = 1

    # creates the starting snake
    snake(postions,ea,scr,snakelist)

    while 1:
        key = scr.getch()         
        time.sleep(0.1) 
        dire,counter = checkkey(key,scr,dire,counter)
        
        for piece in snakelist:
            mm = movement(piece[2])
            piece[0] += mm[0] 
            piece[1] += mm[1]
        if counter > -1 and counter < len(snakelist):
            snakelist[counter][2] = dire
            counter +=1
            scr.addstr(0,0,"heelo")
        else:
            counter = -1
                
        snake(postions,ea,scr,snakelist)

        # quit when q is hit
        if postions[4] == 1:
            break

        # adds one to the string in snake when you reach the random point
        if snakelist[0][0] == postions[2] and snakelist[0][1] == postions[3]:
            # checks direction of the last piece to add the extra piece 
            pieceshift = movement(snakelist[-1][2])
            #adds the extra piece to the snake
            snakelist.append([snakelist[-1][0] - pieceshift[0] , snakelist[-1][1] - pieceshift[1], snakelist[-1][2]]) 
            # resets the position of the mouse
            postions[2] = random.randint(1,maxy)
            postions[3] = random.randint(1,maxx)
        
        # ends game when you hit a border to avoid crashing 
        if postions[1]  == dim[1]-1 or postions[0] == dim[0]-1 or postions[1] == 1 or postions[0] == 1:
            break

    term(scr)

    
curses.wrapper(main(scr))

