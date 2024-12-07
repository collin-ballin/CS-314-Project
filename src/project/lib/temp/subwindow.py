import curses
import curses.textpad as tp





def edit_window(box) -> str:
    xmax, ymax  = box.win.getmaxyx()
    x           = 0
    y           = 0
    capture     = True
    curses.curs_set(2)


    #   1.  ALLOW USER TO PROVIDE INPUT...
    while (capture):
        key     = box.win.getch()
        y, x    = box.win.getyx()

        #   CASE 1 :    "ENTER"
        if ( (key == curses.KEY_ENTER) or (key == 10) or (key == 13) ):
            capture = False
        #
        #   CASE 2 :    "BACKSPACE"
        elif key in (curses.KEY_BACKSPACE, 127):

            if ( (x==0) and (0 < y) ):#     2.1.    Delete at the beginning of a line (skip up to previous line).
                box.win.move(y-1, xmax)
                box.win.delch(y-1, xmax)
                
            elif (0 < x):#                  2.2.    Delete in the middle of the line.
                box.win.delch(y, x-1)
        #
        #   CASE 3 :    "NORMAL CHARACTER"
        else:
            if ( (not (y < ymax)) and (not (x < xmax)) ):#    3.2.    At the end of input text-box.
                pass
            else:#                                      3.1.    Adding character normally.
                box.win.addch(key)
                

    #   2.  FETCHING USER'S INPUT...
    response = box.gather()

    #   3.  RESET THE INPUT BOX...
    box.win.clear()
    box.win.refresh()

    return response.rstrip()


def draw_window(stdscr, dims:tuple, pos:tuple, text=None, title_offset:int=2, subwindow:bool=False):
    w, h    = dims
    x, y    = pos
    

    window  = stdscr.subwin(w, h,  x+1, y+1) if (subwindow) else curses.newwin(w, h,  x+1, y+1)
    box     = tp.rectangle(stdscr, x, y, 1+w+1+x, 1+h+1+y )
    
    
    if (text is not None):
        stdscr.addstr(x, y+title_offset, f"  {text}  ")
        
    return (window, box)




def main(stdscr):
    stdscr.clear()
    
    _H, _W      = stdscr.getmaxyx()
    h = _H-3
    w = _W-3
    
    #win, win_box    = draw_window(stdscr, (20, 30), (5, 20), text="WINDOW")
    win, win_box    = draw_window(stdscr, (h, w), (0, 0), text="WINDOW")
    win_tbox        = tp.Textbox(win)
    win.refresh()
    stdscr.refresh()
    
    
    stdscr.getch()
    
    
    
    edit_window(win_tbox)
    win.refresh()
    
    
    stdscr.getch()
    
    rows, cols  = win.getmaxyx()
    
    return (rows, cols)






if (__name__ == '__main__'):
    value = curses.wrapper(main)
    print(f"{value}")
