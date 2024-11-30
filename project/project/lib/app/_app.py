###############################################################################
#
#       ************************************************************
#       ****            _ A P P . P Y  ____  F I L E.           ****
#       ************************************************************
#
#
###############################################################################
from dataclasses import dataclass, field
import numpy as np
from lib.utility import Cstring
from lib.utility import ANSI
import lib.utility as UTL
from lib.users import Member, Provider

import json, sys, time, traceback
from PIL import Image
import curses
import curses.textpad as tp






#   CONSTANTS / MISC.
###############################################################################
###############################################################################

_LW         = 87
_PROMPTS    = {
    #   Utility Texts...
    "tc"                : f"{ANSI.GREEN_BRIGHT}",   #   'tc'    = terminal color (color for output of program).
    "header"            : "WELCOME TO THE \"CHOCOHOLICS ANONYMOUS\" HEALTHCARE DATABASE MANAGMENT SYSTEM!",
    "line"              : f"{ANSI.WHITE_BB}" + _LW * '═' + f"{ANSI.RESET}",
    "o_cursor"          : f"█ ",
    "i_cursor"          : f"INPUT ",
    #
    #
    #   Prompts / Output...
    "provider_1"        : f"Please enter your 9-digit provider ID number: ",
    "t_cursor"          : f"",
    #
    #
    #   Exception Handling / Termination...
    "normal_exit"       : "Program terminating.  Have a great day!",
}


###############################################################################
#
#
#
#
#
#
#   UTILITY / PRIVATE FUNCTIONS FOR "APP" CLASS...
###############################################################################
###############################################################################



###############################################################################
#
#
#
#
#
#
#   MEMBER FUNCTION FOR "APP" CLASS (IMPORTED)...
###############################################################################
###############################################################################

#   "load_users"
#
def load_users(self, file_path:str) -> tuple:
    idx     = 0
    m_idx   = 0
    p_idx   = 0
    
    with open(file_path, 'r') as file:
        data = json.load(file)


    for item in data:
        #   CASE 1 :    Loaded a "Member" from the file.
        if (item["type"] == "Member"):
            #           1.1.    Load the main fields of the member.
            user = Member(
                name=item["name"],      id=item["id"],          address=item["address"],
                city=item["city"],      state=item["state"],    zip=item["zip"],
            )
            #           1.2.    Load the historical records of the member.
            for record in item.get("history", []):
                entry = (record["date"], record["provider_name"], record["service_name"])
                user.history.append( entry )
            
            self.members.append(user)
            idx     += 1
            m_idx   += 1
        #
        #   CASE 2 :    Loaded a "Provider" from the file.
        elif (item["type"] == "Member"):
            user = Member(
                name    =item["name"],
                id      =item["id"],
                address =item["address"],
                city    =item["city"],
                state   =item["state"],
                zip     =item["zip"],
            )
            self.providers.append(user)
            idx     += 1
            p_idx   += 1
        #
        #   CASE 3 :    Loaded a "Provider" from the file.
        else:
            UTL.log("Error while loading user-data from \"{file}\": data at entry \"{idx}\" has an unsupported type.", ANSI.WARN)
            idx += 1
            
    return (idx, m_idx, p_idx)
    
    
    
#   "__post_init__"
#
def __post_init__(self):
    file    = f'data/users.json'
    
    #   1.  TRY-BLOCK...
    try:
        #   1.1.    Assigning Positions.
        home            = ANSI.get_cursor_pos()
        self.pos        = {
            "home"  : home,
            "out1"  : (home[0]+3, 0),
            "out2"  : (home[0]+4, 0),
            "out3"  : (home[0]+5, 0),
            "line"  : (home[0]+6, 0),
            "in"    : (home[0]+7, 8),
            "last"  : (home[0]+8, 0),
            "end"   : (home[0]+9, 0),
        }
        self.prompts    = _PROMPTS
        load_info       = load_users(self, file)
        
        #   1.2.    Setting UI Dimensions.
        self.UI['in'] = { 'height' : 3, 'width' : 30 }
        
    #
    #
    #   2.  CATCH-BLOCK...
    except ValueError as e:             #   2.1.    Could not get position of the terminal cursor.
        UTL.log("CAUGHT A \"VALUE ERROR\" EXCEPTION.",type=ANSI.ERROR)
        UTL.log(f"{e}",color=False)
        raise(e)
    #
    except FileNotFoundError as e:      #   2.2.    Could not open the external data file.
        UTL.log("CAUGHT A \"FILE NOT FOUND\" EXCEPTION.",type=ANSI.ERROR)
        UTL.log(f"{e}",color=False)
        raise(e)
    #
    except ValueError as e:             #   2.3.    Unknown IOError occured.
        UTL.log("CAUGHT AN \"IOERROR\" EXCEPTION.",type=ANSI.ERROR)
        UTL.log(f"{e}",color=False)
        raise(e)
    #
    #
    #   3.  FINALLY-BLOCK...
    finally:
        UTL.log(f"Loaded {load_info[0]} total items from file \"{file}\": {load_info[1]} Members and {load_info[2]} Providers.")
        
    
    return
    
    
    
    
    
#   "setup_UI"
#
def setup_UI(self, stdscr):

    #   0.  INITIALIZE ELEMENTS OF UI...
    #
    #       0.1.    Colors.
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)      #   Header Text.
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)     #   Output Text.
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)       #   Input Text.
    #
    #       0.2.    Initial Commands.
    stdscr.clear()                                                  #   Clear the screen
    #
    #       0.3.    Initial Values.
    #curses.curs_set(0)                                             #   ANSI.HIDE
    curses.noecho()                                                 #   Disable real-time printing of input to screen.
    height, width           = stdscr.getmaxyx()                     #   Screen Dimensions.
    self.UI['global']       = { 'height':height, 'width':width }
    
    
    #   2.  CREATE WINDOW FOR EACH SECTION OF OUTPUT...
    #
    #       2.3.    User-Input Window.
    stdscr.addstr(0, 0, f"{self.prompts['i_cursor']}")
    input_win               = curses.newwin( self.UI['in']['height'], self.UI['in']['width']-2, 2, 1)  # 3 lines high, below output
    input_box               = tp.rectangle(stdscr, 1, 0, 1 + self.UI['in']['height'] + 1, 1 + self.UI['in']['width'] + 1)
    input_tbox              = tp.Textbox(input_win)
    stdscr.refresh()
    
    
    #   3.  ASSIGNING EACH WINDOW TO DICTIONARY...
    #
    self.UI['in']['win']    = input_win
    self.UI['in']['box']    = input_box
    self.UI['in']['tbox']   = input_tbox
    
    
    return
    
    


#   "main"
#
def main(self, stdscr):
    #UTL.log(f"Type of \"stdscr\" = {stdscr}.", ANSI.NOTE)
    setup_UI(self, stdscr)
    box = self.UI['in']['tbox']



    while (True):
        # Edit the box manually to capture each key press
        key = box.win.getch()

        #   CASE 1 :    "ENTER"
        if ( (key == curses.KEY_ENTER) or (key == 10) or (key == 13) ):
            break
        #
        #   CASE 2 :    "BACKSPACE"
        elif key in (curses.KEY_BACKSPACE, 127):
            y, x = box.win.getyx()
            if (x > 0):#                    2.1.    Delete in the middle of the line.
                box.win.delch(y, x - 1)
                
            elif (y > 0):#                    2.2.    Delete in the middle of the line.
                box.win.delch(y-1, x)
        #
        #   CASE 3 :    "NORMAL CHARACTER"
        else:
            box.win.addch(key)


    # Get resulting contents
    message = box.gather()

    # Display the message in the terminal (for testing)
    stdscr.addstr(8, 0, f"Message submitted: {message}")
    stdscr.refresh()

    # Wait for user to see the output before exiting
    stdscr.getch()
        
    return
    
    
    
#   "run"
#
def run(self) -> int:
    status = 0
    sys.stdout.write(f"{ANSI.ENABLE_WRAP}")
    
    #   1.  TRY-BLOCK...
    try:
        #stdscr = curses.initscr()
        curses.wrapper(self.main)
    #
    #   2.  EXCEPTION-CATCHING BLOCKS...
    except KeyboardInterrupt as e:
        UTL.log(f"Caught CTRL-C Keyboard Interuption.  Exiting...")
        UTL.log(f"{e}", color=False)
        
    except Exception as e:
        UTL.log("FALLBACK EXCEPTION CASE.  An specified exception has been thrown.",type=ANSI.ERROR)
        UTL.log(f"{e}", color=False)
        traceback.print_exc()
        status = 1
    #
    #   3.  FINALLY...
    finally:
        pass
    
    return status
    
    
    

###############################################################################
###############################################################################
#   END.
