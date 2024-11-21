###############################################################################
#
#   ****************************************************************
#   ****    "U_T_I_L_I_T_Y"                    M O D U L E ...  ****
#   ****    "C_S_T_R_I_N_G" ________ S U B --- M O D U L E ...  ****
#   ****                                                        ****
#   ****                            File:        "__init__.py"  ****
#   ****************************************************************
#
#	    This is one of the intermediate "__init__.py" files within the project.
#   This file handles the responsibilities of initializing the contents of the
#   CONSTANTS Module.
#
###############################################################################
from dataclasses import dataclass, field
import re


# 	CLASS:  "CSTRING"
#
@dataclass
class Cstring:
	'''Class to implement a fixed-size string following the C-style function of a compile-time array.'''
###############################################################################

    #   Imported Class Methods (Imported from "_name.py" files)...
	from ._cstring import __post_init__
	from ._cstring import __str__
	from ._cstring import __repr__
    
    #   Imported Properties...
	from ._cstring import data
	from ._cstring import size
 
    #   Class Data Members...
	_data:          str             = field(init=True, repr=True)
	_size:          int             = field(init=True, repr=True)
 
 
 
###############################################################################
#   END OF "CSTRING".
#
#
#
#
#
###############################################################################
###############################################################################
#   END "__INIT__" FOR "UTILITY" :: "CONSTANTS".


    #size:           int     = field(init=True,  repr=True)
#_value:str=field(init=True, repr=True)
