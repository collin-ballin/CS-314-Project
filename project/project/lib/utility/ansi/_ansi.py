###############################################################################
#
#   "C_O_N_S_T_A_N_T_S"          M O D U L E.
#
#             "A_N_S_I"          S U B - M O D U L E.
#
#
#                 File:         "_ansi.py".
#
###############################################################################
from enum import Enum, auto
import os, sys, termios, tty, select, signal, traceback
import time, re



#   1.  ANSI COLOR CODES.
###############################################################################
###############################################################################

#                   2.1.    Regular Typeface Colors (30-37).
RESET               = "\033[0m"
BLACK               = "\033[30m"
RED                 = "\033[31m"
BLUE                = "\033[32m"
GREEN               = "\033[34m"
YELLOW              = "\033[35m"
MAGENTA             = "\033[33m"
CYAN                = "\033[36m"
WHITE               = "\033[37m"


#                   2.2.    Bold Typeface Colors (1 + 30-37).
BLACK_BOLD          = "\033[1m\033[30m"
RED_BOLD            = "\033[1m\033[31m"
BLUE_BOLD           = "\033[1m\033[32m"
GREEN_BOLD          = "\033[1m\033[34m"
YELLOW_BOLD         = "\033[1m\033[35m"
MAGENTA_BOLD        = "\033[1m\033[33m"
CYAN_BOLD           = "\033[1m\033[36m"
WHITE_BOLD          = "\033[1m\033[37m"


#                   2.3.    Bright Typeface Colors (90-97).
BLACK_BRIGHT        = "\033[90m"
RED_BRIGHT          = "\033[91m"
GREEN_BRIGHT        = "\033[92m"
YELLOW_BRIGHT       = "\033[93m"
BLUE_BRIGHT         = "\033[94m"
MAGENTA_BRIGHT      = "\033[95m"
CYAN_BRIGHT         = "\033[96m"
WHITE_BRIGHT        = "\033[97m"


#                   2.4.    Bold Bright Colors (1 + 90-97).
BLACK_BB            = "\033[1m\033[90m"
RED_BB              = "\033[1m\033[91m"
GREEN_BB            = "\033[1m\033[92m"
YELLOW_BB           = "\033[1m\033[93m"
BLUE_BB             = "\033[1m\033[94m"
MAGENTA_BB          = "\033[1m\033[95m"
CYAN_BB             = "\033[1m\033[96m"
WHITE_BB            = "\033[1m\033[97m"


#                   2.5.    Typeface Styles and Misc Commands.
RESET               = "\033[0m"
RESET_ALL           = "\033[0m" + "\033[?25h"
BOLD                = "\033[1m"
DIM                 = "\033[2m"
ITALIC              = "\033[3m"
UNDERLINE           = "\033[4m"
BLINK               = "\033[5m"
INVERSE             = "\033[7m"
HIDDEN              = "\033[8m"
STRIKETHROUGH       = "\033[9m"
DISABLE_WRAP        = "\033[?7l"
ENABLE_WRAP         = "\033[?7h"


#                   2.6.    Cursor Movement Commands.
CLEAR               = "\033[2J"
CLEAR_ABOVE         = "\033[1J"
CLEAR_BELOW         = "\033[0J"

CLEAR_LINE          = "\033[2K"
CLEAR_RIGHT         = "\033[1K"
CLEAR_LEFT          = "\033[0K"

CRETURN             = "\r"
BELL                = "\a"
SAVE                = "\033[7"
RECALL              = "\033[8"
GET_POS             = "\033[6n"
HIDE                = "\033[?25l"
SHOW                = "\033[?25h"
    
def SET(r:int=1, c:int=1) -> str:
    return f"\033[{r};{c}H" + f"\033[{r};{c}f"

def UP(i:int=1) -> str:
    return f"\033[{i}A"
    
def DOWN(i:int=1) -> str:
    return f"\033[{i}B"
    
def RIGHT(i:int=1) -> str:
    return f"\033[{i}C"
    
def LEFT(i:int=1) -> str:
    return f"\033[{i}D"
    
def _BELL(f:int=1) -> str:
    return f"\033[10;{f}]"


def set(r:int=1, c:int=1):
    sys.stdout.write(f"\033[{r};{c}H" + f"\033[{r};{c}f")
    
def save():
    sys.stdout.write(SAVE)

def recall():
    sys.stdout.write(RECALL)
    
def up(i:int=1):
    sys.stdout.write(f"\033[{i}A")
    
def down(i:int=1):
    sys.stdout.write(f"\033[{i}B")
    
def right(i:int=1):
    sys.stdout.write(f"\033[{i}C")
    
def left(i:int=1):
    sys.stdout.write(f"\033[{i}D")

def set_terminal_title(title:str):
    sys.stdout.write(f"\033]0;{title}\007")

def hide():
    sys.stdout.write(f"\033[?25l")

def show():
    sys.stdout.write(f"\033[?25h")


#   "get_cursor_pos"
#
def get_cursor_pos() -> tuple:
    fd              = sys.stdin.fileno()
    init_setting    = termios.tcgetattr(fd)
    
    try:
        tty.setraw(fd)
        sys.stdout.write(GET_POS)
        sys.stdout.flush()
        
        response = ''
        while (True):
            # Read one character at a time
            char = sys.stdin.read(1)
            if (char == 'R'):
                response += char
                break
            response += char

        #   Response has format "ESC [ rows ; cols R".     EX: "\x1b[24;80R"
        match = re.match(r'\x1b\[(\d+);(\d+)R', response)
        
        if (match):
            row, col = match.groups()
            return (int(row), int(col))
        else:
            raise ValueError("Unexpected response: {}".format(response))
    finally:
        # Restore the original terminal settings
        termios.tcsetattr(fd, termios.TCSADRAIN, init_setting)
        
    return



#   "print_at"
#
def print_at(pos:tuple, msg:str):
    sys.stdout.write(f"{SET(pos[0],pos[1])}{msg}")
    return
    


###############################################################################
###############################################################################
#
#
#
#
#
#
#   2.  CLASSES AND TYPES TO DEFINE TAGS FOR LOGGING ...
###############################################################################
###############################################################################
#   Define an enum for EACH TYPE OF LOG.
class Log_Tag(Enum):
    LOG         = auto()
    WARN        = auto()
    EVENT       = auto()
    ERROR       = auto()
    NOTE        = auto()
    
    
#   2.1.    CONSTANT VALUES FOR LOG TAGS ...
###############################################################################
#   Log-Type Tags.
LOG                         = Log_Tag.LOG
WARN                        = Log_Tag.WARN
EVENT                       = Log_Tag.EVENT
ERROR                       = Log_Tag.ERROR
NOTE                        = Log_Tag.NOTE


#   2.2.    FORMAT STYLES FOR LOG TYPES ...
###############################################################################
LOG_LINEWIDTH               = 87

LOG_STYLES = {
    WARN: {
        "label"             : "WARN",
        "color_code"        : YELLOW_BOLD,
        "tag_color"         : YELLOW,
        "count"             : 0
    },
    ERROR: {
        "label"             : "ERROR",
        "color_code"        : UNDERLINE + RED_BB,
        "tag_color"         : RED,
        "count"             : 0
    },
    EVENT: {
        "label"             : "EVENT",
        "color_code"        : BLUE_BOLD,
        "tag_color"         : BLUE,
        "count"             : 0
    },
    NOTE: {
        "label"             : "NOTE",
        "color_code"        : UNDERLINE + CYAN_BB,
        "tag_color"         : CYAN_BRIGHT,
        "count"             : 0
    },
    LOG: {
        "label"             : "LOG",
        "color_code"        : GREEN_BOLD,
        "tag_color"         : GREEN,
        "count"             : 0
    }
}


#
#
#
###############################################################################




###############################################################################
###############################################################################
#   END "UTILITY" :: "_ANSI".
