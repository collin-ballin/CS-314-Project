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
    "line"              : f"{ANSI.WHITE_BB}" + _LW * '═' + f"{ANSI.RESET}",
    "o1_cursor"         : f"{ANSI.GREEN_BB}{ANSI.INVERSE}1{ANSI.RESET} ",
    "o2_cursor"         : f"{ANSI.GREEN_BB}{ANSI.INVERSE}2{ANSI.RESET} ",
    "o3_cursor"         : f"{ANSI.GREEN_BB}{ANSI.INVERSE}3{ANSI.RESET} ",
    "i_cursor"          : f"{ANSI.RED_BOLD}{ANSI.BLINK}█{ANSI.RESET} ",
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


def load_users_from_file(file_path):
    with open(file_path, 'r') as file:
        users_data = json.load(file)

    users = []
    for user_data in users_data:
        if user_data["type"] == "Member":
            user = Member(
                user_data["name"],
                user_data["street_address"],
                user_data["city"],
                user_data["state"],
                user_data["zip"],
                user_data["membership_number"]
            )
        elif user_data["type"] == "Provider":
            user = Provider(
                user_data["name"],
                user_data["street_address"],
                user_data["city"],
                user_data["state"],
                user_data["zip"],
                user_data["provider_id"]
            )
        users.append(user)
    return users
    
    
    
#   draw_UI
#
def draw_UI(self):
    #   1.  PRINTING THE FORMATTING OF THE COMMAND-LINE APPLICATION...
    ANSI.print_at( self.pos['home'],
                   UTL.make_dboxed(self.prompts['header'], textcolor=ANSI.CYAN_BB, boxcolor=ANSI.WHITE_BB, lw=self.lw) )
    ANSI.print_at( self.pos['line'], self.prompts['line'] )
    ANSI.print_at( self.pos['last'],  self.prompts['line'] )
    
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
    #UTL.log("Inside the \"App\" class...", ANSI.NOTE)
        
    #   1.  Print the "UI" for the command-line application...
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

#   "__post_init__"
#
def __post_init__(self):
    #
    try:
        home            = ANSI.get_cursor_pos()
        self.pos        = {
            "home"  : home,
            "out1"  : (home[0]+3, 0),
            "out2"  : (home[0]+4, 0),
            "out3"  : (home[0]+5, 0),
            "line"  : (home[0]+6, 0),
            "in"    : (home[0]+7, 0),
            "last"  : (home[0]+8, 0),
            "end"   : (home[0]+9, 0),
        }
        self.prompts    = _PROMPTS
    #
    #
    except ValueError as e:
        raise(e)
        
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
