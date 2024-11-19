###############################################################################
#
#   ********************************************************
#   ****    "U_T_I_L_I_T_Y"             M O D U L E ... ****
#   ****    "A_N_S_I" _______ S U B --- M O D U L E ... ****
#   ****                                                ****
#   ****                  File:         "__init__.py"   ****
#   ********************************************************
#
#	    This is one of the intermediate "__init__.py" files within the project.
#   This file handles the responsibilities of initializing the contents of the
#   CONSTANTS Module.
#
###############################################################################



#   LOG TAG-DISPATCH VALUES.
###############################################################################
#   Log Tags Types.
from ._ansi import Log_Tag

#   Log Type Tags.
from ._ansi import LOG,             WARN,           ERROR,          EVENT


#   ANSI COLOR CODES.
###############################################################################
#   Import 2.1.
from ._ansi import BLACK,           RED,            GREEN,          YELLOW,  \
                   BLUE,            MAGENTA,        CYAN,           WHITE

#   Import 2.2.
from ._ansi import BLACK_BOLD,      RED_BOLD,       GREEN_BOLD,     YELLOW_BOLD,  \
                   BLUE_BOLD,       MAGENTA_BOLD,   CYAN_BOLD,      WHITE_BOLD
                   
#   Import 2.3.
from ._ansi import BLACK_BRIGHT,    RED_BRIGHT,     GREEN_BRIGHT,   YELLOW_BRIGHT,  \
                   BLUE_BRIGHT,     MAGENTA_BRIGHT, CYAN_BRIGHT,    WHITE_BRIGHT

#   Import 2.4.
from ._ansi import BLACK_BB,        RED_BB,         GREEN_BB,       YELLOW_BB,       \
                   BLUE_BB,         MAGENTA_BB,     CYAN_BB,        WHITE_BB

#   Import 2.5.
from ._ansi import RESET,           BOLD,           DIM,            ITALIC,          \
                   UNDERLINE,       BLINK,          INVERSE,        HIDDEN,          \
                   STRIKETHROUGH
                   
                   
###############################################################################
###############################################################################
#   END "__INIT__" FOR "UTILITY" :: "ANSI".
