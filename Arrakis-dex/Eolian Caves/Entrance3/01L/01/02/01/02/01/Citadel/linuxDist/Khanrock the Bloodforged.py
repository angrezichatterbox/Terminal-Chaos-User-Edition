import threading
import time
import curses
from curses.textpad import rectangle, Textbox
import os

on=True
t=0
bhp=100
php=100
iter=0

def dropsAndFileGen(stdscr, height, width):
    global on
    stdscr.erase()
    stdscr.refresh()
    # stdscr.addstr(height//2-1, width//2-30," __  __  __   ___   __     __          __ __       __ __  ")
    # stdscr.addstr(height//2+0, width//2-30,"/ _ |__)|_  /\ |   |_ |\ ||_ |\/|\_/  |_ |_ |  |  |_ |  \ ")
    # stdscr.addstr(height//2+1, width//2-30,"\__)| \ |__/--\|   |__| \||__|  | |   |  |__|__|__|__|__/ ")  
                                                                                                                                        
    stdscr.addstr(height//2-10, width//2-33,"@@@@@@@   @@@@@@@@  @@@@@@@@@@   @@@   @@@@@@@@   @@@@@@   @@@@@@@ ")
    stdscr.addstr(height//2-9, width//2-33,"@@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@  @@@@@@@@@  @@@@@@@@  @@@@@@@@")
    stdscr.addstr(height//2-8, width//2-33,"@@!  @@@  @@!       @@! @@! @@!  @@!  !@@        @@!  @@@  @@!  @@@")
    stdscr.addstr(height//2-7, width//2-33,"!@!  @!@  !@!       !@! !@! !@!  !@!  !@!        !@!  @!@  !@!  @!@")
    stdscr.addstr(height//2-6, width//2-33,"@!@  !@!  @!!!:!    @!! !!@ @!@  !!@  !@! @!@!@  @!@  !@!  @!@  !@!")
    stdscr.addstr(height//2-5, width//2-33,"!@!  !!!  !!!!!:    !@!   ! !@!  !!!  !!! !!@!!  !@!  !!!  !@!  !!!")
    stdscr.addstr(height//2-4, width//2-33,"!!:  !!!  !!:       !!:     !!:  !!:  :!!   !!:  !!:  !!!  !!:  !!!")
    stdscr.addstr(height//2-3, width//2-33,":!:  !:!  :!:       :!:     :!:  :!:  :!:   !::  :!:  !:!  :!:  !:!")
    stdscr.addstr(height//2-2, width//2-33," :::: ::   :: ::::  :::     ::    ::   ::: ::::  ::::: ::   :::: ::")
    stdscr.addstr(height//2-1, width//2-33,":: :  :   : :: ::    :      :    :     :: :: :    : :  :   :: :  : ")
    stdscr.addstr(height//2, width//2,"                                                                   ")                                                               
    stdscr.addstr(height//2+1, width//2-29,"@@@@@@@@  @@@@@@@@  @@@       @@@       @@@@@@@@  @@@@@@@ ") 
    stdscr.addstr(height//2+2, width//2-29,"@@@@@@@@  @@@@@@@@  @@@       @@@       @@@@@@@@  @@@@@@@@") 
    stdscr.addstr(height//2+3, width//2-29,"@@!       @@!       @@!       @@!       @@!       @@!  @@@") 
    stdscr.addstr(height//2+4, width//2-29,"!@!       !@!       !@!       !@!       !@!       !@!  @!@") 
    stdscr.addstr(height//2+5, width//2-29,"@!!!:!    @!!!:!    @!!       @!!       @!!!:!    @!@  !@!") 
    stdscr.addstr(height//2+6, width//2-29,"!!!!!:    !!!!!:    !!!       !!!       !!!!!:    !@!  !!!") 
    stdscr.addstr(height//2+7, width//2-29,"!!:       !!:       !!:       !!:       !!:       !!:  !!!") 
    stdscr.addstr(height//2+8, width//2-29,":!:       :!:        :!:       :!:      :!:       :!:  !:!") 
    stdscr.addstr(height//2+9, width//2-29," ::        :: ::::   :: ::::   :: ::::   :: ::::   :::: ::") 
    stdscr.addstr(height//2+10, width//2-29," :        : :: ::   : :: : :  : :: : :  : :: ::   :: :  : ") 
                                                                                                                                                                                                                                                                                       
    stdscr.refresh()
    time.sleep(4)
    stdscr.erase()
    stdscr.refresh()
    stdscr.addstr(height//2, width//2-12,"Celestial Amulet Dropped")
    stdscr.refresh()
    time.sleep(1.5)
    stdscr.erase()
    stdscr.addstr(height//2, width//2-9,"Light Book Unlocked")
    stdscr.refresh()
    time.sleep(2.5)
    with open("LightBook.txt","w") as file:
        file.write("Behold the Light Book!\nA beacon of wisdom that illuminates the path of creation, peace, and enlightment. The legends whisper of a hidden counterpart in the Dark Realm.\ncode:2F 61 6E 67 72 65 7A 69 63 68 61 74 74")
    with open("Celestial Veil Amulet.txt","w") as file:
        file.write("Forged in the celestial forges of Sigmaron, the Celestial Veil Amulet is a relic born of divine intervention to combat the malevolent forces that threaten the balance of existence. When worn, the Celestial Veil Amulet emanates a radiant glow, warding off malevolent influences and shielding the bearer from the corrupting touch of the Chaos.\ncode:CSigVmaroAn\n")
    on=False


def holy_attack(stdscr, height, width):
    global on
    stdscr.refresh()
    win=curses.newwin(1, 20, height//2+height//4, width//2-10)
    box=Textbox(win)
    stdscr.refresh()
    stdscr.addstr(height//2-height//8, width//2-27,"Quick!! Khanrock is stunned, use the holy spell!!")
    text=box.edit()
    stdscr.erase()
    stdscr.refresh()
    if text=="LhrudhkCqaLnnmanknl ":
        stdscr.addstr(height//2-height//8, width//2-20,f"{text}is the code! Using holy magic....")
        stdscr.refresh()
        time.sleep(1)
        stdscr.erase()
        stdscr.refresh()
        stdscr.addstr(height//2-10,width//2-17,"             /       \            ",)
        stdscr.addstr(height//2-9,width//2-17,"         \ |/         \| /        ",)
        stdscr.addstr(height//2-8,width//2-17,"          |/           \|         ",)
        stdscr.addstr(height//2-7,width//2-17,"           \           /          ",)
        stdscr.addstr(height//2-6,width//2-17,"            \-       -/           ",)
        stdscr.addstr(height//2-5,width//2-17,"              \.-*-./             ",)
        stdscr.addstr(height//2-4,width//2-17,"               |x x|              ",)
        stdscr.addstr(height//2-3,width//2-17,"                \|/               ",)
        stdscr.addstr(height//2-2,width//2-17,"                 *                ",)
        stdscr.addstr(height//2-1,width//2-17,"               /---\              ",)
        stdscr.addstr(height//2,width//2-17,"             /-    -\             ",)
        stdscr.addstr(height//2+1,width//2-17,"            /.       \            ",)
        stdscr.addstr(height//2+2,width//2-17,"           |  -_____- |           ",)
        stdscr.addstr(height//2+3,width//2-17,"          *│      |    *          ",)
        stdscr.addstr(height//2+4,width//2-17,"          /│  /   |    |          ",)
        stdscr.addstr(height//2+5,width//2-17,"         -|_ /    |   ||.         ",)
        stdscr.addstr(height//2+6,width//2-17,"          |__     |   ;           ",)
        stdscr.addstr(height//2+7,width//2-17,"           | /--._;__.*           ",)
        stdscr.addstr(height//2+8,width//2-17,"            |        \|           ",)
        stdscr.addstr(height//2+9,width//2-17,"          |/          \           ",)
        stdscr.refresh()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        for j in range(height//4):
            stdscr.addstr(j, width//2-17,"                                   ", curses.color_pair(1))
        stdscr.refresh()
        time.sleep(0.3)
        stdscr.addstr(height//2-10,width//2-17,"             /       \            ", curses.color_pair(1))
        stdscr.addstr(height//2-9,width//2-17,"         \ |/         \| /        ", curses.color_pair(1))
        stdscr.addstr(height//2-8,width//2-17,"          |/           \|         ", curses.color_pair(1))
        stdscr.addstr(height//2-7,width//2-17,"           \           /          ", curses.color_pair(1))
        stdscr.addstr(height//2-6,width//2-17,"            \-       -/           ", curses.color_pair(1))
        stdscr.addstr(height//2-5,width//2-17,"              \.-*-./             ", curses.color_pair(1))
        stdscr.addstr(height//2-4,width//2-17,"               |x x|              ", curses.color_pair(1))
        stdscr.addstr(height//2-3,width//2-17,"                \|/               ", curses.color_pair(1))
        stdscr.addstr(height//2-2,width//2-17,"                 *                ", curses.color_pair(1))
        stdscr.addstr(height//2-1,width//2-17,"               /---\              ", curses.color_pair(1))
        stdscr.addstr(height//2,width//2-17,"             /-    -\             ",)
        stdscr.addstr(height//2+1,width//2-17,"            /.       \            ",)
        stdscr.addstr(height//2+2,width//2-17,"           |  -_____- |           ",)
        stdscr.addstr(height//2+3,width//2-17,"          *│      |    *          ",)
        stdscr.addstr(height//2+4,width//2-17,"          /│  /   |    |          ",)
        stdscr.addstr(height//2+5,width//2-17,"         -|_ /    |   ||.         ",)
        stdscr.addstr(height//2+6,width//2-17,"          |__     |   ;           ",)
        stdscr.addstr(height//2+7,width//2-17,"           | /--._;__.*           ",)
        stdscr.addstr(height//2+8,width//2-17,"            |        \|           ",)
        stdscr.addstr(height//2+9,width//2-17,"          |/          \           ",)
        stdscr.refresh()
        time.sleep(0.3)
        stdscr.erase()
        for i in range(3):
            stdscr.erase()
            stdscr.addstr(height//2-10,width//2-17,"             /       \            ", curses.color_pair(1))
            stdscr.addstr(height//2-9,width//2-17,"         \ |/         \| /        ", curses.color_pair(1))
            stdscr.addstr(height//2-8,width//2-17,"          |/           \|         ", curses.color_pair(1))
            stdscr.addstr(height//2-7,width//2-17,"           \           /          ", curses.color_pair(1))
            stdscr.addstr(height//2-6,width//2-17,"            \-       -/           ", curses.color_pair(1))
            stdscr.addstr(height//2-5,width//2-17,"              \.-*-./             ", curses.color_pair(1))
            stdscr.addstr(height//2-4,width//2-17,"               |x x|              ", curses.color_pair(1))
            stdscr.addstr(height//2-3,width//2-17,"                \|/               ", curses.color_pair(1))
            stdscr.addstr(height//2-2,width//2-17,"                 *                ", curses.color_pair(1))
            stdscr.addstr(height//2-1,width//2-17,"               /---\              ", curses.color_pair(1))
            stdscr.addstr(height//2,width//2-17,"             /-    -\             ", curses.color_pair(1))
            stdscr.addstr(height//2+1,width//2-17,"            /.       \            ", curses.color_pair(1))
            stdscr.addstr(height//2+2,width//2-17,"           |  -_____- |           ", curses.color_pair(1))
            stdscr.addstr(height//2+3,width//2-17,"          *│      |    *          ", curses.color_pair(1))
            stdscr.addstr(height//2+4,width//2-17,"          /│  /   |    |          ", curses.color_pair(1))
            stdscr.addstr(height//2+5,width//2-17,"         -|_ /    |   ||.         ", curses.color_pair(1))
            stdscr.addstr(height//2+6,width//2-17,"          |__     |   ;           ", curses.color_pair(1))
            stdscr.addstr(height//2+7,width//2-17,"           | /--._;__.*           ", curses.color_pair(1))
            stdscr.addstr(height//2+8,width//2-17,"            |        \|           ", curses.color_pair(1))
            stdscr.addstr(height//2+9,width//2-17,"          |/          \           ", curses.color_pair(1))
            stdscr.refresh()
            time.sleep(0.3)
            stdscr.erase()
            stdscr.addstr(height//2-10,width//2-2-17,"               /       \              ", curses.color_pair(1))
            stdscr.addstr(height//2-9,width//2-2-17,"           \ |/         \| /          ", curses.color_pair(1))
            stdscr.addstr(height//2-8,width//2-2-17,"            |/           \|           ", curses.color_pair(1))
            stdscr.addstr(height//2-7,width//2-2-17,"             \           /            ", curses.color_pair(1))
            stdscr.addstr(height//2-6,width//2-2-17,"              \-       -/             ", curses.color_pair(1))
            stdscr.addstr(height//2-5,width//2-2-17,"                \.-*-./               ", curses.color_pair(1))
            stdscr.addstr(height//2-4,width//2-2-17,"                 |x x|                ", curses.color_pair(1))
            stdscr.addstr(height//2-3,width//2-2-17,"                  \|/                 ", curses.color_pair(1))
            stdscr.addstr(height//2-2,width//2-2-17,"                   *                  ", curses.color_pair(1))
            stdscr.addstr(height//2-1,width//2-2-17,"                 /---\                ", curses.color_pair(1))
            stdscr.addstr(height//2,width//2-2-17,"               /-    -\               ", curses.color_pair(1))
            stdscr.addstr(height//2+1,width//2-2-17,"              /.       \              ", curses.color_pair(1))
            stdscr.addstr(height//2+2,width//2-2-17,"             |  -_____- |             ", curses.color_pair(1))
            stdscr.addstr(height//2+3,width//2-2-17,"            *│      |    *            ", curses.color_pair(1))
            stdscr.addstr(height//2+4,width//2-2-17,"            /│  /   |    |            ", curses.color_pair(1))
            stdscr.addstr(height//2+5,width//2-2-17,"           -|_ /    |   ||.           ", curses.color_pair(1))
            stdscr.addstr(height//2+6,width//2-2-17,"            |__     |   ;             ", curses.color_pair(1))
            stdscr.addstr(height//2+7,width//2-2-17,"             | /--._;__.*             ", curses.color_pair(1))
            stdscr.addstr(height//2+8,width//2-2-17,"              |        \|             ", curses.color_pair(1))
            stdscr.addstr(height//2+9,width//2-2-17,"            |/          \             ", curses.color_pair(1))
            stdscr.refresh()
            time.sleep(0.3)
        stdscr.erase()
        stdscr.refresh()
        stdscr.addstr(height//2-5,width//2+7-17,"     /       \      ")
        stdscr.addstr(height//2-4, width//2+7-17," \ |          \| /  ")
        stdscr.addstr(height//2-3, width//2+7-17,"  |            \    ")
        stdscr.addstr(height//2-2, width//2+7-17,"   \                ")
        stdscr.addstr(height//2-1, width//2+7-17,"     -       -/     ")
        stdscr.addstr(height//2, width//2+7-17,"      \.-*-.        ")
        stdscr.addstr(height//2+1, width//2+7-17,"       |  *|        ")
        stdscr.addstr(height//2+2, width//2+7-17,"  |  -__\|          ")
        stdscr.addstr(height//2+3, width//2+7-17," *  ,.   *    *     ")
        stdscr.addstr(height//2+4, width//2+7-17," /,. / \   -- |     ")
        stdscr.addstr(height//2+5, width//2+7-17," |_ /  '   - _ .    ")
        stdscr.addstr(height//2+6, width//2+7-17,".,,_   / |   ;  , .,")
        stdscr.addstr(height//2+7, width//2+7-17," ,|  --._; _.* ,,   ")
        stdscr.addstr(height//2+8, width//2+7-17,"   |         |  \   ")
        stdscr.addstr(height//2+9, width//2+7-17," |/          \      ")
        stdscr.refresh()
        time.sleep(0.5)
        stdscr.erase()
        stdscr.refresh()
        stdscr.addstr(height//2+4, width//2+8-17,"   \  /          ")
        stdscr.addstr(height//2+5, width//2+8-17,"    |/           ")
        stdscr.addstr(height//2+6, width//2+8-17,"     \  *x     /_")
        stdscr.addstr(height//2+7, width//2+8-17,"     xx-xxxxx./  ")
        stdscr.addstr(height//2+8, width//2+8-17,"  xxxxx**xx8xxx  ")
        stdscr.addstr(height//2+9, width//2+8-17,"xx**x8*#cxxx*xxx ")
        stdscr.refresh()
        time.sleep(2)
        dropsAndFileGen(stdscr, height, width)
    else:
        stdscr.addstr(height//2-height//8, width//2-20,f"{text}is not the code! Half ass")
        stdscr.refresh()
        time.sleep(2)
        stdscr.erase()
        stdscr.addstr(height//2, width//2-40,"Game Over-You run away for now. But Khanriok might be ready for the next round.")
        stdscr.refresh()
        time.sleep(3)
        curses.endwin()
    stdscr.getch()

def boss_attack(stdscr):
    global t, bhp, php, on, iter
    height, width= stdscr.getmaxyx()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_WHITE)
    while php!=2:
        stdscr.erase()
        # rectangle(stdscr, int(height*0.75)-3, 1, 7, 18)
        stdscr.addstr(int(height*0.75), 3, "Press p to parry")
        stdscr.addstr(int(height*0.75)+1, 3, "Press q to exit and escape")

        if bhp==1:
            stdscr.addstr(0,2," "*(int(2*width/100)-4), curses.color_pair(1))
            stdscr.refresh()
            holy_attack(stdscr, height, width)
        else:
            # health bar and number
            stdscr.addstr(0,2," "*(int(bhp*width/100)-4), curses.color_pair(1))
            stdscr.addstr(1, width//2-1, f"{bhp}")
            stdscr.addstr(height-2,2," "*(int(php*width/100)-4), curses.color_pair(1))
            stdscr.addstr(height-3, width//2-1, f"{php-php%50}")#health bar number
            
            stdscr.noutrefresh()
            curses.doupdate()
        
            if t<3:
                if t==0 or t==-1:
                    stdscr.noutrefresh()
                    curses.doupdate()
                    stdscr.addstr(height//2-10, width//2-17,"             /       \            ")
                    stdscr.addstr(height//2-9, width//2-17,"         \ |/         \| /        ")
                    stdscr.addstr(height//2-8, width//2-17,"          |/           \|         ")
                    stdscr.addstr(height//2-7, width//2-17,"           \           /          ")
                    stdscr.addstr(height//2-6, width//2-17,"            \-       -/           ")
                    stdscr.addstr(height//2-5, width//2-17,"              \.-*-./             ")
                    stdscr.addstr(height//2-4, width//2-17,"               |* *|              ")
                    stdscr.addstr(height//2-3, width//2-17,"                \|/               ")
                    stdscr.addstr(height//2-2, width//2-17,"                 *                ")
                    stdscr.addstr(height//2-1, width//2-17,"               /---\              ")
                    stdscr.addstr(height//2+0, width//2-17,"             /-    -\             ")
                    stdscr.addstr(height//2+1, width//2-17,"            /.       \            ")
                    stdscr.addstr(height//2+2, width//2-17,"           |  -_____- |           ")
                    stdscr.addstr(height//2+3, width//2-17,"====      *│      |    *   .__    ")
                    stdscr.addstr(height//2+4, width//2-17,"    ====__/│  /   |    |   '  *-_ ")
                    stdscr.addstr(height//2+5, width//2-17,"         -|_ /    |   ||.   \    *")
                    stdscr.addstr(height//2+6, width//2-17,"          |__     |   ; ==__;   / ")
                    stdscr.addstr(height//2+7, width//2-17,"           | /--._;__.*   -/   |  ")
                    stdscr.addstr(height//2+8, width//2-17,"            |        \|   /    \  ")
                    stdscr.addstr(height//2+9, width//2-17,"          |/          \  -------* ")
                    stdscr.noutrefresh()
                    curses.doupdate()
                elif t==1:
                    stdscr.noutrefresh()
                    curses.doupdate()
                    stdscr.addstr(height//2-8, width//2-17,"                 /       \    ") 
                    stdscr.addstr(height//2-7, width//2-17,"   _ ---_    \ |/         \| / ")
                    stdscr.addstr(height//2-6, width//2-17,"    -    /    |/           \|  ")
                    stdscr.addstr(height//2-5, width//2-17,"   /   /       \           /   ")
                    stdscr.addstr(height//2-4, width//2-17,"_-*   -==       \-       -/    ")
                    stdscr.addstr(height//2-3, width//2-17,"-     \  ====     \.-*-./      ")
                    stdscr.addstr(height//2-2, width//2-17," -   _-     ====   |* *|       ")
                    stdscr.addstr(height//2-1, width//2-17,"  ***          ===/ \|/        ")
                    stdscr.addstr(height//2, width//2-17,"                /-_  *|        ")
                    stdscr.addstr(height//2+1, width//2-17,"              /    *** '==     ")
                    stdscr.addstr(height//2+2, width//2-17,"             /        /| ====  ")
                    stdscr.addstr(height//2+3, width//2-17,"            -        / |    ===")
                    stdscr.addstr(height//2+4, width//2-17,"           |           |       ")
                    stdscr.addstr(height//2+5, width//2-17,"            \          ;       ")
                    stdscr.addstr(height//2+6, width//2-17,"           / - _     _*        ")
                    stdscr.addstr(height//2+7, width//2-17,"          |/*   *---*          ")
                    stdscr.addstr(height//2+8, width//2-17,"         /        `|           ")
                    stdscr.noutrefresh()
                    curses.doupdate()
                elif t==2:
                    stdscr.noutrefresh()
                    curses.doupdate()
                    stdscr.addstr(height//2-8, width//2-17,"            /       \               ")
                    stdscr.addstr(height//2-7, width//2-17,"        \ |/         \| /           ")
                    stdscr.addstr(height//2-6, width//2-17,"         |/           \|            ")
                    stdscr.addstr(height//2-5, width//2-17,"          \           /             ")
                    stdscr.addstr(height//2-4, width//2-17,"           \-       -/              ")
                    stdscr.addstr(height//2-3, width//2-17,"             \.-*-./                ")
                    stdscr.addstr(height//2-2, width//2-17,"              |* *|                 ")
                    stdscr.addstr(height//2-1, width//2-17,"             / \|/                  ")
                    stdscr.addstr(height//2, width//2-17,"           /\ __*|                  ")
                    stdscr.addstr(height//2+1, width//2-17,"======   /,  / /  '                 ")
                    stdscr.addstr(height//2+2, width//2-17,"     ===/===/ /./ |                 ")
                    stdscr.addstr(height//2+3, width//2-17,"       -  ===/*== |      ._--**---_ ")
                    stdscr.addstr(height//2+4, width//2-17,"      |   /     ==|====   \      _-*")
                    stdscr.addstr(height//2+5, width//2-17,"       \ /        ;  ===== |   -*   ")
                    stdscr.addstr(height//2+6, width//2-17,"      / **--|--/-*    __-**    *-.  ")
                    stdscr.addstr(height//2+7, width//2-17,"     ;.*    | /      *-__    __-*   ")
                    stdscr.addstr(height//2+8, width//2-17,"            .'           **-*       ")
                    stdscr.noutrefresh()
                    curses.doupdate()
                stdscr.addstr(8, 0, f"Boss Attack!({3-t})")
                stdscr.noutrefresh()
                curses.doupdate()
                time.sleep(1)
                t+=1
                stdscr.noutrefresh()
                curses.doupdate()
            else:
                stdscr.erase()
                stdscr.addstr(height//2,width//2-8,"you got attacked")
                stdscr.refresh()
                time.sleep(1)
                t=-1
                php-=49
                stdscr.erase()
                stdscr.refresh()

    stdscr.erase()
    stdscr.addstr(height//2-5, width//2-25,"@@@@@@@   @@@@@@@@   @@@@@@   @@@@@@@  @@@  @@@")
    stdscr.addstr(height//2-4, width//2-25,"@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@  @@@  @@@")
    stdscr.addstr(height//2-3, width//2-25,"@@!  @@@  @@!       @@!  @@@    @@!    @@!  @@@")
    stdscr.addstr(height//2-2, width//2-25,"!@!  @!@  !@!       !@!  @!@    !@!    !@!  @!@")
    stdscr.addstr(height//2-1, width//2-25,"@!@  !@!  @!!!:!    @!@!@!@!    @!!    @!@!@!@!")
    stdscr.addstr(height//2, width//2-25,"!@!  !!!  !!!!!:    !!!@!!!!    !!!    !!!@!!!!")
    stdscr.addstr(height//2+1, width//2-25,"!!:  !!!  !!:       !!:  !!!    !!:    !!:  !!!")
    stdscr.addstr(height//2+2, width//2-25,":!:  !:!  :!:       :!:  !:!    :!:    :!:  !:!")
    stdscr.addstr(height//2+3, width//2-25," :::: ::   :: ::::  ::   :::     ::    ::   :::")
    stdscr.addstr(height//2+4, width//2-25,":: :  :   : :: ::    :   : :     :      :   : :")
                                                 
    stdscr.refresh()
    time.sleep(2)
    on=False
    

def handle_input(stdscr):
    global t, bhp, on, iter
    height, width= stdscr.getmaxyx()
    while php>0 and bhp!=1:
        key = stdscr.getch()
        if key == ord('p') and ( bhp>1 and (3-t)==1):
            t=-1
            bhp-=33
            stdscr.erase()
            stdscr.addstr(1,0,' '*16)
            stdscr.addstr(height//2, width//2-6, "You parried!")
            stdscr.refresh()
            time.sleep(1)
            stdscr.addstr(2, 0, " " * 15) 
            stdscr.refresh()
        elif key == ord('q'):
            on=False
    

def main(stdscr):

    curses.curs_set(0) # Hide cursor
    
    height, width=stdscr.getmaxyx()
    stdscr.addstr(height//2, width//2-15, "I'm Khanrock the Bloodforged!!")
    stdscr.refresh()
    time.sleep(2)
    stdscr.addstr(height//2, width//2-22, "And nobody shall pass as long as I'm alive!!")
    stdscr.refresh()
    time.sleep(2)
    stdscr.erase()

    # boss attack thread
    boss_thread = threading.Thread(target=boss_attack, args=(stdscr,))
    boss_thread.daemon = True
    boss_thread.start()

    # input handling thread
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
