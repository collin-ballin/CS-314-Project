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
BOLD                = "\033[1m"
DIM                 = "\033[2m"
ITALIC              = "\033[3m"
UNDERLINE           = "\033[4m"
BLINK               = "\033[5m"
INVERSE             = "\033[7m"
HIDDEN              = "\033[8m"
STRIKETHROUGH       = "\033[9m"


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
LOG_LINEWIDTH               = 70

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
