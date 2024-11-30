###############################################################################
#
#       ************************************************************
#       ****       _ S E R V I C E S . P Y  ____  F I L E.      ****
#       ************************************************************
#
#
###############################################################################
from dataclasses import dataclass, field
import math
from lib.utility import ANSI
import lib.utility as UTL
from lib.utility import Cstring
from lib.utility.constants import _S_SIZE_CONSTANTS



# 	CLASS:  "Service"
#
@dataclass(order=True, kw_only=True)
class Service:
    '''Class to define a \"Service\" that is offered by a provider of 
       the Chocoholics Anonymous healthcare network.'''
###############################################################################
###############################################################################

	################################################################
	################        Data Members for        ################
	################		 S E R V I C E		    ################
	################################################################

    name                : str           = field(default="NAME",
                                                init=True,      compare=True,
                                                hash=True,      repr=True)

    id                  : str           = field(default="ID NUMBER",
                                                init=True,      compare=True,
                                                hash=True,      repr=True)

    address             : str           = field(default="STREET ADDRESS",
                                                init=True,      compare=True,
                                                hash=True,      repr=True)

    city                : str           = field(default="CITY",
                                                init=True,      compare=True,
                                                hash=True,      repr=True)

    state               : str           = field(default="STATE",
                                                init=True,      compare=True,
                                                hash=True,      repr=True)

    zip                 : str           = field(default="ZIPCODE",
                                                init=True,      compare=True,
                                                hash=True,      repr=True)


#   1.  Build-In Methods...
###############################################################################
    
    #   "__post_init__"
    #
    def __post_init__(self):
        self._enforce_size()
        return
        
    
    #   "__str__"
    #
    def __str__(self) -> str:
        record_length   = len(self.history)
        string          = f"{self.name} (#{self.id}).  {self.address}, {self.city}, {self.state}.  "
        
        if ( not record_length ):
            string += f"No records of prior healthcare services."
        elif ( record_length == 1 ):
            string += f"{record_length} record of prior healthcare service."
        else:
            string += f"{record_length} records prior healthcare services."
        
        return string
    
    
    #   "__setattr__"
    #
    def __setattr__(self, attr, value):
        
        #   CASE 1 :    Attribute is inside base-class.
        if (attr in _S_SIZE_CONSTANTS):
            value_fmt = UTL.truncate(value, size=_S_SIZE_CONSTANTS[attr]).title()
            super().__setattr__(attr, value_fmt)
        #
        #
        #   CASE 2 :    Attempt to set/access an unrecognized attribute.
        else:
            UTL.log(f"Accessing unrecognized attribute, \"{attr}\", in class \"Service\".", ANSI.WARN)
            super().__setattr__(attr, value)
            
        
        return
            

#   3.  Member Functions...
###############################################################################
    
    #   "_enforce_size"
    #
    def _enforce_size(self):
        return
        
        
###############################################################################
###############################################################################
#   END "SERVICE".
    





###############################################################################
###############################################################################
#   END "SERVICES".
