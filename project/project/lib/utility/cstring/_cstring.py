###############################################################################
#
#           "U_T_I_L_I_T_Y"         M O D U L E.
#
#           "C_S_T_R_I_N_G"         S U B - M O D U L E.
#
#
#                 File:             "_cstring.py".
#
###############################################################################
#from enum import Enum, auto
import lib.utility.ansi as ANSI
import lib.utility as UTL



#   MEMBER FUNCTION FOR "CSTRING" CLASS (IMPORTED)...
###############################################################################
###############################################################################

#   "__post_init__"
#
def __post_init__(self):
    if ( len(self._data) > self._size ):#               Truncate...
        self._data = self._data[:self._size]
    elif ( len(self._data) < self._size ):#             Add Padding...
        self.data = self._data.ljust(self._size)
        
    return



#   "__str__"
#
def __str__(self):
    return self._data



#   "__repr__"
#
def __repr__(self):
    return f"cstring(data='{self._data}', size={self._size})"


###############################################################################
#
#
#
#   PROPERTIES FOR "APP" CLASS (IMPORTED)...
###############################################################################
###############################################################################

#   "setter" / "getter"     | FOR "data".
@property
def data(self) -> str:
    return self._data
            
            
@data.setter
def data(self, arg:str):
    UTL.log("Inside the \"data.setter\"...", ANSI.EVENT)
    UTL.log(f"Initial data: {self._data}.\tArgument: {arg}", ANSI.LOG)
    
    if ( self.size < len(arg) ):#               Truncate...
        self._value = arg[:self.size]
    else:#                                      Add Padding...
        self._value = arg#.ljust(self.size)
    
    
    UTL.log(f"Final data: {self._data}", ANSI.WARN)
    
    return
    
    

#   "setter" / "getter"     | FOR "size".
@property
def size(self) -> int:
    return self._size


###############################################################################
###############################################################################
#   END "UTILITY" :: "_CSTRING".
