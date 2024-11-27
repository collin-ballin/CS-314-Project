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
from lib.users import Member

import sys, time
from PIL import Image






#   CONSTANTS / MISC.
###############################################################################
###############################################################################

_LW         = 87
_PROMPTS    = {
    #   Utility Texts...
    "tc"                : f"{ANSI.GREEN_BRIGHT}",   #   'tc'    = terminal color (color for output of program).
    "header"            : "WELCOME TO THE \"CHOCOHOLICS ANONYMOUS\" HEALTHCARE DATABASE MANAGMENT SYSTEM!",
    "line"              : f"\n{ANSI.CYAN}" + _LW * '═' + f"{ANSI.RESET}",
    "o_cursor"          : f"{ANSI.GREEN_BB}█{ANSI.RESET} ",
    "i_cursor"          : f"{ANSI.RED_BOLD}{ANSI.BLINK}█{ANSI.RESET} ",
    #
    #
    #   Prompts / Output...
    "provider_1"        : f"Please enter your 9-digit provider ID number: ",
    "t_cursor"          : f"",
}


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

#   "__post_init__"
#
def __post_init__(self):
    #
    try:
        home    = ANSI.get_cursor_pos()
    
        self.pos        = {
            "home"  : ANSI.get_cursor_pos()
        }
    
        self.prompts    = _PROMPTS
    #
    #
    except:
        pass
        
    return
    


    
#   "main"
#
def main(self):

    def print_at(pos:tuple, text:str):
        sys.stdout.write(f"{ANSI.SET(pos[0], pos[1])}{text}")
        return



    #UTL.log("Inside the \"App\" class...", ANSI.NOTE)


    print( UTL.make_dboxed(_PROMPTS['header'], textcolor=ANSI.CYAN_BB, boxcolor=ANSI.CYAN, lw=_LW),)
    print( _PROMPTS['o_cursor'] + "\n" + _PROMPTS['line'] + "\n" + _PROMPTS['line'])
    #ANSI.up(4)
    
    
    
    def display_input_prompt(text:str, params:dict=_PROMPTS):
        print(f"{ANSI.UP(4)}{ANSI.CRETURN}{ANSI.CLEAR_LINE}{_PROMPTS['o_cursor']} ", end='')
        print(f"{params['tc']}{text}{ANSI.RESET}", end='')
        return input(f"{ANSI.DOWN(3)}{ANSI.CRETURN}{ANSI.CLEAR_LINE}{_PROMPTS['i_cursor']} ")
        
        
    ANSI.up(1)
    response = display_input_prompt(self.prompts['provider_1'])
    
    
    response = display_input_prompt(f"You entered \"{response}\"")
    
    
    response = display_input_prompt(f"And now, you have entered \"{response}\"")
    
    
    
    #print_at( (99,0), "text")
    #display_input_prompt(_PROMPTS['provider_1'])
    
    sys.stdout.write(f"The current position is: {ANSI.get_cursor_pos()}")
    
    input(f"")
    
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



###############################################################################
###############################################################################
#   END.
