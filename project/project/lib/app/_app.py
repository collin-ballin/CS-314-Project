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

import json, sys, time, traceback, curses
from PIL import Image






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
            user = Member(
                name    =item["name"],
                id      =item["id"],
                address =item["address"],
                city    =item["city"],
                state   =item["state"],
                zip     =item["zip"],
            )
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
    height, width = stdscr.getmaxyx()                               #   Screen Dimensions.
    
    
    #   2.  CREATE WINDOW FOR EACH SECTION OF OUTPUT...
    #
    #       2.1.    Header Window.
    header_win              = curses.newwin(3, width - 2, 0, 1)  # 3 lines high, full width
    header_win.box()
    header_win.addstr(1, 2, self.prompts['header'], curses.color_pair(1)|curses.A_BOLD)
    header_win.refresh()
    #
    #       2.2.    Program-Output Window.
    output_win              = curses.newwin(6, width - 2, 4, 1)  # 6 lines high, below header
    output_win.box()
    output_win.refresh()
    #
    #       2.3.    User-Input Window.
    input_win               = curses.newwin(3, width - 2, 11, 1)  # 3 lines high, below output
    rectangle(stdscr, 1, 0, 1 + 5 + 1, 1 + 30 + 1)  # Draw a rectangle around the edit window
    stdscr.refresh()

    # Create the Textbox object
    box = Textbox(editwin)
    
    
    input_win               = curses.newwin(3, width - 2, 11, 1)  # 3 lines high, below output
    input_win.box()
    input_win.addstr(1, 2, "INPUT", curses.color_pair(3))  # Red input label
    input_win.refresh()
    
    
    #   3.  ASSIGN EACH WINDOW TO THE CLASS UI...
    self.UI['header']       = header_win
    self.UI['out']          = output_win
    self.UI['in']           = input_win
    
    return
    
    
    
#   "main"
#
def main(self, stdscr):
    #UTL.log(f"Type of \"stdscr\" = {stdscr}.", ANSI.NOTE)
    setup_UI(self, stdscr)
    
    
    self.UI['out'].clear()
    self.UI['out'].box()
    self.UI['out'].addstr(1, 2, self.prompts['provider_1'], curses.color_pair(2)|curses.A_BOLD)
    self.UI['out'].refresh()

    

    # Main interaction loop
    while (True):
        # Example prompt and user input handling
        #self.UI['out'].clear()
        #self.UI['out'].box()
        #self.UI['out'].addstr(1, 2, "Please enter your 9-digit provider ID number:", curses.color_pair(2))
        #self.UI['out'].refresh()

        # Get user input
        self.UI['in'].clear()
        self.UI['in'].box()
        self.UI['in'].addstr(1, 2, self.prompts['i_cursor'], curses.color_pair(3))
        self.UI['in'].refresh()

        curses.echo()
        input_value = self.UI['in'].getstr(1, 8).decode('utf-8')  # Capture user input
        
        # Display the user's input back in the output area
        self.UI['out'].clear()
        self.UI['out'].box()
        self.UI['out'].addstr(1, 2, f"Received: \"{input_value}\"", curses.color_pair(2))
        self.UI['out'].refresh()
        
    return
    
    
    
def holder(self, stdscr):
    # Main interaction loop
    while (True):
        # Example prompt and user input handling
        self.UI['out'].clear()
        self.UI['out'].box()
        self.UI['out'].addstr(1, 2, "1 Please enter your 9-digit provider ID number:", curses.color_pair(2))
        #self.UI['out'].refresh()

        # Get user input
        self.UI['in'].clear()
        self.UI['in'].box()
        self.UI['in'].addstr(1, 2, "INPUT", curses.color_pair(3))
        #self.UI['in'].refresh()

        curses.echo()
        input_value = self.UI['in'].getstr(1, 8).decode('utf-8')  # Capture user input
        
        # Display the user's input back in the output area
        self.UI['out'].clear()
        self.UI['out'].box()
        self.UI['out'].addstr(1, 2, f"1 Received: \"{input_value}\"", curses.color_pair(2))
        #self.UI['out'].refresh()

        # Note: Loop will continue and input will be asked again, just like your screenshots showed
        
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
