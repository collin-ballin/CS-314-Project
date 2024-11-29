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

import json, sys, time, curses
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
    "o1_cursor"         : f"{ANSI.GREEN_BB}{ANSI.INVERSE}1{ANSI.RESET} ",
    "o2_cursor"         : f"{ANSI.GREEN_BB}{ANSI.INVERSE}2{ANSI.RESET} ",
    "o3_cursor"         : f"{ANSI.GREEN_BB}{ANSI.INVERSE}3{ANSI.RESET} ",
    "i_cursor"          : f"{ANSI.RED_BB}{ANSI.INVERSE}INPUT{ANSI.RESET}{ANSI.RED_BB}{ANSI.BLINK} █ {ANSI.RESET}",
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
    
#   draw_UI
#
def draw_UI(self):
    #   1.  PRINTING THE FORMATTING OF THE COMMAND-LINE APPLICATION...
    sys.stdout.write(f"\f")
    ANSI.print_at( self.pos['home'],
                   UTL.make_dboxed(self.prompts['header'], textcolor=ANSI.CYAN_BB, boxcolor=ANSI.WHITE_BB, lw=self.lw) )
    ANSI.print_at( self.pos['line'],  self.prompts['line'] )
    ANSI.print_at( self.pos['last'],  self.prompts['line'] )
    ANSI.print_at( self.pos['end'],   '\n' )
    
    sys.stdout.write(f"\f")
    
    return



#   "display_prompt"
#
def display_prompt(self, text1:str, text2:str='', text3:str=''):
    ANSI.print_at(self.pos['out1'], f"{ANSI.CRETURN}{ANSI.CLEAR_LINE}{self.prompts['o1_cursor']} {self.prompts['tc']}{text1}{ANSI.RESET}")
    ANSI.print_at(self.pos['out2'], f"{ANSI.CRETURN}{ANSI.CLEAR_LINE}{self.prompts['o2_cursor']} {self.prompts['tc']}{text2}{ANSI.RESET}")
    ANSI.print_at(self.pos['out3'], f"{ANSI.CRETURN}{ANSI.CLEAR_LINE}{self.prompts['o3_cursor']} {self.prompts['tc']}{text3}{ANSI.RESET}")
    ANSI.print_at(self.pos['in'], f"{ANSI.CRETURN}{ANSI.CLEAR_LINE}{self.prompts['i_cursor']} ")
    
    return



#   "display_input_prompt"
#
def display_input_prompt(self, text1:str, text2:str='', text3:str=''):
    display_prompt(self, text1, text2, text3)
    return input("")


        
#   "main"
#
def main(self):
    #   1.  Print the "UI" for the command-line application...
    sys.stdout.write(f"{ANSI.DISABLE_WRAP}")
    #sys.stdout.write(f"\033[=1h")
    draw_UI(self)
    
    
    #   2.  PRINTING THE FORMATTING OF THE COMMAND-LINE APPLICATION...
    ANSI.print_at( self.pos['line'], self.prompts['line'] )
    ANSI.print_at( self.pos['last'],  self.prompts['line'] )
        
        
    #   3.  MAIN PROGRAM LOOP...
    response = display_input_prompt(self, self.prompts['provider_1'])
    
    while (True):
        response = display_input_prompt(self, f"recieved: \"{response}\"")
    
    return
    
 
 
#   "main_old"
#
def main_old(self):
    UTL.log("Inside the \"App\" class...", ANSI.NOTE)
   
    
    member_1    = Member(name="Collin A. Bond and a lot of text",   id="1234123412341234",
                         address="308 Negra Arroyo Lane",           state="Oregon",
                         city="Portland")
                         
    member_2    = Member(name="Walter H. White",                    id="490662",
                         address="308 Negra Arroyo Lane",           city="Albuquerque",
                         state="NM",                                zip="87104")
    
   
    member_2.display()
    
    return

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
    
    

#   "run"
#
def run(self) -> int:
    status = 0
    
    #   1.  TRY-BLOCK...
    try:
        sys.stdout.write(f"{ANSI.HIDE}")
        main(self)
    #
    #   2.  EXCEPTION-CATCHING BLOCKS...
    except KeyboardInterrupt as e:
        UTL.log(f"Caught CTRL-C Keyboard Interuption.  Exiting...")
        #UTL.log(f"{e}",color=False)
        
    except Exception as e:
        UTL.log("FALLBACK EXCEPTION CASE.  An specified exception has been thrown.",type=ANSI.ERROR)
        UTL.log(f"{e}",color=False)
        traceback.print_exc()
        status = 1
    #
    #   3.  FINALLY...
    finally:
        sys.stdout.write(f"{ANSI.SET(self.pos['end'])}{ANSI.SHOW}")
        display_prompt(self, self.prompts['normal_exit'])
    
    return status



###############################################################################
###############################################################################
#   END.
