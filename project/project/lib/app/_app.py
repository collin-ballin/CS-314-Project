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
from lib.services import Service

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
    #   Instructions / Info...
    "display_mode_ON"   : "DISPLAY MODE:  Use arrow-keys to cycle forward/backward through entries.  Press \"q\" to exit.",
    "display_mode_OFF"  : "Exiting Display Mode...",
    #
    #
    #   Exception Handling / Termination...
    "normal_exit"       : "Program terminating.  Have a great day!",
}


###############################################################################
###############################################################################


    
    
    
    
    





#   1.  "APPLICATION" CLASS FUNCTIONS...
###############################################################################
###############################################################################
#
#
#
#
#
#
#       1.1  INITIALIZATION / BUILT-IN METHODS...
###############################################################################
###############################################################################

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
        width               = 80
        self.UI['head']     = {
            'height'    : 1,            'width'         : width,
            'pos'       : (0,0),        'title'         : 'WELCOME TO COCOA! (The ChocAn Organization and Clinical Operations Application)' }
                                
        self.UI['out']      = { 'height'    : 15,           'width'         : width,
                                'pos'       : (5,0),        'title'         : 'OUTPUT' }
                                
        self.UI['in']       = { 'height'    : 1,            'width'         : width,
                                'pos'       : (25,0),       'title'         : 'INPUT' }
        
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
                user.history.append( Service(name=record["name"],           id=record["id"],
                                     provider_name=record["provider_name"], provider_id=record["provider_id"],
                                     patient_name=record["patient_name"],   patient_id=record["patient_id"],
                                     dos=record["dos"],                     dor=record["dor"],
                                     comments=record["comments"],           fee=record["fee"]) )
                
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
    
    
    
#   "setup_UI"
#
def setup_UI(self):
    stdscr = self.stdscr
    
    #   0.  INITIALIZE ELEMENTS OF UI...
    #       0.1.    Colors.
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)         #   Header Text.
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)         #   Output Text.
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)           #   Input Text.
    #
    #       0.2.    Initial Commands.
    stdscr.clear()                                                      #   Clear the screen
    #
    #       0.3.    Initial Values.
    #curses.curs_set(0)                                                 #   ANSI.HIDE
    curses.noecho()                                                     #   Disable real-time printing of input to screen.
    height, width               = stdscr.getmaxyx()                     #   Screen Dimensions.
    self.UI['global']           = { 'height':height, 'width':width }
    self.UI['in']['width']      = width-3
    self.UI['out']['width']     = width-3
    
    
    #   2.  CREATE WINDOW FOR EACH SECTION OF PROGRAM...
    #
    #       2.1.    Header Window.
    pos                     = (self.UI['head']['pos'][0], self.UI['in']['pos'][1])
    dims                    = (self.UI['head']['height'], self.UI['in']['width'])
    title                   = self.UI['head']['title']
    head_win                = curses.newwin(       dims[0],   dims[1]-2,  2+pos[0],            1+pos[1] )  # 3 lines high, below output
    head_box                = tp.rectangle(stdscr, 1+pos[0],  pos[1],     1+dims[0]+pos[0]+1,  1+dims[1]+pos[1]+1 )
    head_tbox               = tp.Textbox(head_win)
    head_win.addstr(pos[0], pos[1], title, curses.color_pair(1)|curses.A_BOLD)
    stdscr.refresh()
    #
    #
    #       2.2.    Program-Output Window.
    pos                     = (self.UI['out']['pos'][0], self.UI['in']['pos'][1])
    dims                    = (self.UI['out']['height'], self.UI['in']['width'])
    title                   = self.UI['out']['title']
    stdscr.addstr(pos[0], pos[1], title, curses.color_pair(2)|curses.A_BOLD)
    output_win              = curses.newwin(       dims[0],   dims[1]-2,  2+pos[0],            1+pos[1] )  # 3 lines high, below output
    output_box              = tp.rectangle(stdscr, 1+pos[0],  pos[1],     1+dims[0]+pos[0]+1,  1+dims[1]+pos[1]+1 )
    output_tbox             = tp.Textbox(output_win)
    stdscr.refresh()
    #
    #
    #       2.3.    User-Input Window.
    pos                     = (self.UI['in']['pos'][0], self.UI['in']['pos'][1])
    dims                    = (self.UI['in']['height'], self.UI['in']['width'])
    title                   = self.UI['in']['title']
    stdscr.addstr(pos[0], pos[1], title, curses.color_pair(3)|curses.A_BOLD)
    input_win               = curses.newwin(       dims[0],   dims[1]-2,  2+pos[0],            1+pos[1] )  # 3 lines high, below output
    input_box               = tp.rectangle(stdscr, 1+pos[0],  pos[1],     1+dims[0]+pos[0]+1,  1+dims[1]+pos[1]+1 )
    input_tbox              = tp.Textbox(input_win)
    stdscr.refresh()
    
    
    #   3.  ASSIGNING EACH WINDOW TO DICTIONARY...
    #
    self.UI['head']['win']      = head_win
    self.UI['head']['box']      = head_box
    self.UI['head']['tbox']     = head_tbox
    
    self.UI['in']['win']        = input_win
    self.UI['in']['box']        = input_box
    self.UI['in']['tbox']       = input_tbox
    
    self.UI['out']['win']       = output_win
    self.UI['out']['box']       = output_box
    self.UI['out']['tbox']      = output_tbox
    
    
    curses.curs_set(0)
    self.UI['head']['win'].refresh()
    self.UI['out']['win'].refresh()
    self.UI['in']['win'].refresh()
    
    return
    
    
###############################################################################
###############################################################################
#
#
#
#
#
#
#       1.2.  MAIN FUNCTIONS...
###############################################################################
###############################################################################

#   "run"
#
def run(self) -> int:
    status = 0
    
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
    
    
    
#   "main"
#
def main(self, stdscr):
    run = True
    self.stdscr = stdscr
    
    
    setup_UI(self)
    
    
    #   MAIN PROGRAM LOOP...
    while(run):
        #   1.1.    FETCH INPUT FROM USER...
        response = get_input(self, stdscr)
        set_output(self, response)
        
        if (response == 'a'):
            set_output(self, response)
        
    
    
    
    
    
    #   2.  RESET THE INPUT BOX AND DISPLAY ON OUTPUT CONSOLE...
    self.UI['out']['win'].clear()
    self.UI['in']['win'].clear()
    self.UI['out']['win'].addstr(0, 0, response, curses.color_pair(2))
    
    
    #   3.  REFRESH THE SCREEN...
    self.UI['out']['win'].refresh()
    self.UI['in']['win'].refresh()
    self.stdscr.refresh()
        
        
    #   4.  PARSING CERTAIN RESPONSES...
    #if (response == "display"):
    display_members(self, stdscr)
        


    #   5.  WAIT FOR ENTER-KEY BEFORE CLOSING...
    self.stdscr.getch()
        
    return
    

###############################################################################
###############################################################################
#
#
#
#
#
#
#       1.3.  UTILITY / HELPER FUNCTIONS...
###############################################################################
###############################################################################

#   "display_members"
#
def display_members(self, stdscr):
    N1          = len(self.members)
    N2          = 0
    x           = 0
    y           = 0
    capturing   = True
    curses.curs_set(0)

    #   "get_entry"
    def get_entry(x:int, y:int) -> tuple:
        N       = len( self.members[x].history )
        head_1  = f"PATIENT #{x+1}"
        body_1  = f"{self.members[x]}"
        head_2  = f"RECORD #{y+1}" if (N > 0) else f"NO RECORD OF PRIOR HEALTHCARE SERVICE"
        body_2  = f"{self.members[x].history[y]}" if (N > 0) else ''
        
        return ( (head_1, body_1), (head_2, body_2) )
    
    #   "display_entry"
    def display_entry(x:int, y:int) -> None:
        entry = get_entry(x, y)
        self.UI['out']['win'].clear()
        
        self.UI['out']['win'].addstr(0, 0, entry[0][0], curses.color_pair(2)|curses.A_STANDOUT)
        self.UI['out']['win'].addstr(1, 0, entry[0][1], curses.color_pair(2))
        self.UI['out']['win'].addstr(3, 0, entry[1][0], curses.color_pair(2)|curses.A_STANDOUT)
        self.UI['out']['win'].addstr(4, 0, entry[1][1], curses.color_pair(2))
        
        self.UI['out']['win'].refresh()
        return
    
    
    #   0.  CONFIGURE TERMINAL FOR REAL-TIME INPUT...
    curses.cbreak()  # Alternatively: curses.raw()
    curses.noecho()
    stdscr.keypad(True)  # Enable special key handling like arrows
    
    #   CASE 1 :    NO DATA TO DISPLAY...
    if (N1 == 0):
        raise ValueError("No data on record to display.")

    #   1.  CLEAR INPUT/OUTPUT SCREENS, FETCH INITIAL ENTRY, AND DISPLAY INSTRUCTIONS...
    self.UI['in']['win'].clear()
    self.UI['in']['win'].addstr(0, 0, self.prompts['display_mode_ON'], curses.color_pair(3)|curses.A_STANDOUT)
    self.UI['in']['win'].refresh()
    display_entry(x, y)

    #   2.  MAIN, REAL-TIME INPUT LOOP...
    while (capturing):
        key = stdscr.getch()
    
        #   2.1.    GET THE USER'S KEY-INPUT.
        if (key == ord('q')):
            capturing = False
        #
        elif (key == curses.KEY_LEFT):
            x   = (x-1)%N1
            y   = 0
            N2  = len(self.members[x].history)
        #
        elif (key == curses.KEY_RIGHT):
            x   = (x+1)%N1
            y   = 0
            N2  = len(self.members[x].history)
        #
        elif (key == curses.KEY_UP):
            y = (y+1)%N2 if (N2 > 0) else 0
        #
        elif (key == curses.KEY_DOWN):
            y = (y-1)%N2 if (N2 > 0) else 0


        #   2.2.    Fetch and Display the selected entry.
        display_entry(x, y)
        
        
    #   3.  CLEANING THE SCREEN.  DISPLAYING EXIT MESSAGE...
    self.UI['in']['win'].clear()
    self.UI['out']['win'].clear()
    self.UI['in']['win'].addstr(0, 0, self.prompts['display_mode_OFF'], curses.color_pair(3)|curses.A_STANDOUT)
    self.UI['out']['win'].refresh()
    self.UI['in']['win'].refresh()
    
    return
    
    

#   "get_input"
#
def get_input(self, stdscr) -> str:
    box         = self.UI['in']['tbox']
    xmax        = self.UI['in']['width']-3
    ymax        = self.UI['in']['height']
    capture     = True
    curses.curs_set(2)


    #   1.  ALLOW USER TO PROVIDE INPUT...
    while (capture):
        key     = box.win.getch()
        y, x    = box.win.getyx()

        #   CASE 1 :    "ENTER"
        if ( (key == curses.KEY_ENTER) or (key == 10) or (key == 13) ):
            box.win.move(0, 0)
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
    self.UI['in']['win'].clear()
    self.UI['in']['win'].refresh()
    stdscr.refresh()

    return response
    
 
 
#   "set_output"
#
def set_output(self, text:str, pos:tuple=(0,0), clear:bool=False, attribute=None) -> None:

    if (
    if (clear):
        self.UI['out']['win'].clear()
    
    if (attribute is None):
        self.UI['out']['win'].addstr(pos[0], pos[1], text, curses.color_pair(2))
    else:
        self.UI['out']['win'].addstr(pos[0], pos[1], text, curses.color_pair(2)|attribute)
        
    self.UI['out']['win'].refresh()
    self.stdscr.refresh()
    return
    
    
###############################################################################
###############################################################################
#
#
#
###############################################################################
###############################################################################
#   END OF "APPLICATION" CLASS...
    





###############################################################################
###############################################################################
#   END.
