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
import copy
import lib.utility.ansi as ANSI
import lib.utility as UTL









# CLASS: "CSTRING"
#
class Cstring:
    '''Class to implements a string of constant length.  
    The purpose is to mimic the functionality of a compile-time array in a manin C/C++ style function of a compile-time array.'''
###############################################################################
###############################################################################
#
#
#
#   1.  BUILT-IN METHODS...
###############################################################################

    #   "__init__"
    def __init__(self, *, size, data=''):
        if ( not isinstance(size, int) or (size <= 0) ):
            raise ValueError("Size must be a positive, non-zero integer.")
            
        self._size = size
        self._data = self._enforce_size(data)
        return


    #   "__str__"
    #
    def __str__(self):
        return self._data


    #   "__repr__"
    #
    def __repr__(self):
        return f"Cstring(size={self._size}, data='{self._data}')"


    #   "__eq__"
    #
    def __eq__(self, other):
        if isinstance(other, Cstring):
            return self._data == other._data and self._size == other._size
        return False


    #   "__setattr__"
    #
    def __setattr__(self, name, value):
        if hasattr(self, '_size') and name == 'size':
            raise AttributeError("Size attribute is read-only.")
            
        super().__setattr__(name, value)
        return


###############################################################################
#
#
#
#   2.  PROPERTIES...
###############################################################################

    #   "size"              | Getter.
    #
    @property
    def size(self):
        return self._size

    #   "size"              | Setter.
    @size.setter
    def size(self, arg:str):
        raise AttributeError("Size of \"Cstring\" cannot be modified after instantiation.")
        return



    #   "data"              | Getter.
    #
    @property
    def data(self) -> str:
        return copy.deepcopy(self._data)
        
    #   "data"              | Setter.
    @size.setter
    def size(self, arg:str):
        raise AttributeError("Size of \"Cstring\" cannot be modified after instantiation.")
        return


###############################################################################
#
#
#
#   3.  MEMBER FUNCTIONS...
###############################################################################

    #   "_enforce_size"
    #
    def _enforce_size(self, data:str) -> str:
        if (len(data) > self._size):
            return data[:self._size]
            
        return data.ljust(self._size)
        


###############################################################################
###############################################################################









































#   OLD STUFF BELOW HERE ...
###############################################################################
###############################################################################








#   MEMBER FUNCTION FOR "CSTRING" CLASS (IMPORTED)...
###############################################################################
###############################################################################

#   "_enforce_size"
#
def _enforce_size(self, src:str):
    if (self.size < len(src)):#             Truncate...
        self._data  = src[:self.size]
    else:#                                  Add Padding...
        self._data  = src.ljust(self.size)
        
    return
    

###############################################################################
#
#
#
#   BUILT-IN CLASS METHODS...
###############################################################################
###############################################################################

#   "__post_init__"
#
def __post_init__(self):
    if (len(self._data) > self._size):
        self._data = self._data[:self._size]
    elif (len(self._value) < self._size):
        self._data = self._data.ljust(self._size)
        
    return



#   "__str__"
#
def __str__(self):
    return self._data



#   "__repr__"
#
def __repr__(self):
    return f"Cstring(data='{self._data}', size={self._size})"


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
