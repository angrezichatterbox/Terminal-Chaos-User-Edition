import threading
import time
import curses
from curses.textpad import rectangle, Textbox

on=True
t=0
bhp=100
php=100

def holy_attack(stdscr, height, width):
    global on
    stdscr.refresh()
    win=curses.newwin(1, 20, height//2+height//4, width//2-10)
    box=Textbox(win)
    stdscr.refresh()
    stdscr.addstr(height//2-height//8, width//2-20,"Quick!! Khanrock is stunned, use the holy spell!!")
    text=box.edit()
    stdscr.erase()
    stdscr.refresh()
    if text=="niggers ":
        stdscr.addstr(height//2-height//8, width//2-20,f"{text}is the code! Great Enemy Felled!!")
        stdscr.refresh()
        time.sleep(1)
        on=False
    else:
        stdscr.addstr(height//2-height//8, width//2-20,f"{text}is not the code! Half ass")
        stdscr.refresh
        time.sleep(1)
        on=False
    stdscr.getch()

def boss_attack(stdscr):
    global t, bhp, php, on
    height, width= stdscr.getmaxyx()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_WHITE)
    while php!=2:
        # rectangle(stdscr, int(height*0.75)-3, 0, 7, 18)
        stdscr.addstr(int(height*0.75), 1, "Press p to parry")
        stdscr.addstr(int(height*0.75)+1, 1, "Press q to exit")

        if bhp==1:
            stdscr.addstr(0,0," "*(int(2*width/100)-2), curses.color_pair(1))
            stdscr.refresh()
            holy_attack(stdscr, height, width)
        else:
            stdscr.addstr(0,0," "*(int(bhp*width/100)-2), curses.color_pair(1))
        stdscr.addstr(1, width//2-1, f"{bhp}")
        stdscr.addstr(height-2,0," "*(int(php*width/100)-2), curses.color_pair(1))
        stdscr.addstr(height-3, width//2-1, f"{php-1}")
        # stdscr.hline(0, 0, curses.ACS_HLINE, int(bhp*width/100)-2)
        # stdscr.hline(4, 0, curses.ACS_HLINE, int(php*width/100)-2)        
        # rectangle(stdscr, 0,0,1,int(bhp*width/100)-2)
        # rectangle(stdscr, 10,0,1,int(php*width/100)-2)
        if bhp!=1:
            if t<3:
                stdscr.addstr(height//2-height//8, width//2-7, f"Boss Attack!({3-t})")
                stdscr.refresh()
                time.sleep(1)
                stdscr.addstr(1, 0, " " * 15)
                t+=1
                stdscr.refresh()
            else:
                stdscr.addstr(1,0,"you got attacked")
                t=0
                php-=49
                time.sleep(1)
                stdscr.erase()
                stdscr.addstr(1,0,str(php))
                time.sleep(1)
                stdscr.refresh()
    stdscr.erase()
    stdscr.addstr(height//2, width//2-4, "Game over")
    stdscr.refresh()
    time.sleep(2)
    on=False
    

def handle_input(stdscr):
    global t, bhp, on
    height, width= stdscr.getmaxyx()
    while php>0 and bhp!=1:
        key = stdscr.getch()
        if key == ord('p') and bhp>1:
            t=0
            bhp-=33
            stdscr.erase()
            # stdscr.addstr(0,0,' '*width)
            stdscr.addstr(1,0,' '*16)
            stdscr.addstr(2, 0, "You parried!")
            stdscr.refresh()
            time.sleep(1)
            stdscr.addstr(2, 0, " " * 15)
            stdscr.refresh()
        elif key == ord('q'):
            on=False
    

def main(stdscr):
    
    curses.curs_set(0) 
    stdscr.nodelay(1) 

    #window creartion
    # height, width=stdscr.getmaxyx()
    # x=35
    # win=curses.newwin(x, width, height//2-x//2, 0)
    # inpwin=curses.newwin(5,48,height//2+height//4+2,width//2-width//4+2)
    height, width=stdscr.getmaxyx()
    stdscr.addstr(height//2, width//2-15, "I'm Khanrock the Bloodforged!!")
    stdscr.refresh()
    time.sleep(3)
    stdscr.addstr(height//2, width//2-22, "And nobody shall pass as long as I'm alive!!")
    stdscr.refresh()
    time.sleep(3)
    stdscr.erase()

   
    boss_thread = threading.Thread(target=boss_attack, args=(stdscr,))
    boss_thread.daemon = True
    boss_thread.start()

   
    input_thread = threading.Thread(target=handle_input, args=(stdscr,))
    input_thread.daemon = True
    input_thread.start()

   
    while True:
        time.sleep(1)
        if on==False:
            break
    curses.endwin()

if __name__ == "__main__":
    curses.wrapper(main)
