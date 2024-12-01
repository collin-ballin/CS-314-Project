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
                service = Service(name=record["name"],                      id=record["id"],
                                  provider_name=record["provider_name"],    provider_id=record["provider_id"],
                                  patient_name="Collin Bond",               patient_id="000000007",
                                  dos=record["dos"],                        dor=record["dor"],
                                  comments=record["comments"],              fee=record["fee"])
                
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
        width               = 20
        self.UI['head']     = { 'height'    : 1,            'width'         : width,
                                'pos'       : (0,0),        'title'         : 'title' }
                                
        self.UI['out']      = { 'height'    : 5,            'width'         : width,
                                'pos'       : (5,0),        'title'         : 'OUTPUT' }
                                
        self.UI['in']       = { 'height'    : 2,            'width'         : width,
                                'pos'       : (15,0),       'title'         : 'INPUT' }
        
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
    #       2.2.    Program-Output Window.
    pos                     = (self.UI['out']['pos'][0], self.UI['in']['pos'][1])
    dims                    = (self.UI['out']['height'], self.UI['in']['width'])
    title                   = self.UI['out']['title']
    stdscr.addstr(pos[0], pos[1], f"{title}")
    output_win              = curses.newwin(       dims[0],   dims[1]-2,  2+pos[0],            1+pos[1] )  # 3 lines high, below output
    output_box              = tp.rectangle(stdscr, 1+pos[0],  pos[1],     1+dims[0]+pos[0]+1,  1+dims[1]+pos[1]+1 )
    output_tbox             = tp.Textbox(output_win)
    stdscr.refresh()
    #
    #
    #
    #       2.3.    User-Input Window.
    pos                     = (self.UI['in']['pos'][0], self.UI['in']['pos'][1])
    dims                    = (self.UI['in']['height'], self.UI['in']['width'])
    title                   = self.UI['in']['title']
    stdscr.addstr(pos[0], pos[1], f"{title}")
    input_win               = curses.newwin(       dims[0],   dims[1]-2,  2+pos[0],            1+pos[1] )  # 3 lines high, below output
    input_box               = tp.rectangle(stdscr, 1+pos[0],  pos[1],     1+dims[0]+pos[0]+1,  1+dims[1]+pos[1]+1 )
    input_tbox              = tp.Textbox(input_win)
    stdscr.refresh()
    
    
    
    
    #   3.  ASSIGNING EACH WINDOW TO DICTIONARY...
    #
    self.UI['in']['win']    = input_win
    self.UI['in']['box']    = input_box
    self.UI['in']['tbox']   = input_tbox
    
    self.UI['out']['win']   = output_win
    self.UI['out']['box']   = output_box
    self.UI['out']['tbox']  = output_tbox
    
    return
    
    


#   "main"
#
def main(self, stdscr):
    setup_UI(self, stdscr)
    
    
    #   1.  FETCH INPUT FROM USER...
    response = get_input(self, stdscr)


    #   2.  RESET THE INPUT BOX AND DISPLAY ON OUTPUT CONSOLE...
    self.UI['out']['win'].clear()
    self.UI['in']['win'].clear()
    self.UI['out']['win'].addstr(0, 0, response, curses.color_pair(2))
    
    
    #   3.  REFRESH THE SCREEN...
    self.UI['out']['win'].refresh()
    self.UI['in']['win'].refresh()
    stdscr.refresh()


    #   4.  WAIT FOR ENTER-KEY BEFORE CLOSING...
    stdscr.getch()
        
    return
    


#   "get_input"
#
def get_input(self, stdscr) -> str:
    box         = self.UI['in']['tbox']
    xmax        = self.UI['in']['width']-3
    ymax        = self.UI['in']['height']
    capture     = True



    #   1.  ALLOW USER TO PROVIDE INPUT...
    while (capture):
        key     = box.win.getch()
        y, x    = box.win.getyx()

        #   CASE 1 :    "ENTER"
        if ( (key == curses.KEY_ENTER) or (key == 10) or (key == 13) ):
            capture = False
            #break
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
    self.UI['out']['win'].clear()
    self.UI['in']['win'].clear()
    self.UI['out']['win'].refresh()
    stdscr.refresh()

    return response
    
    
    
#   "run"
#
def run(self) -> int:
    status = 0
    #sys.stdout.write(f"{ANSI.ENABLE_WRAP}")
    
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
