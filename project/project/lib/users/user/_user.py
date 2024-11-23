###############################################################################
#
#       "U_S_E_R_S"             M O D U L E.
#
#         "U_S_E_R"             S U B - M O D U L E.
#
#
#             File:             "_user.py".
#
###############################################################################
from abc import ABC
from dataclasses import dataclass, field
from lib.utility import Cstring
import lib.utility as UTL
from lib.utility.constants import _M_SIZE_CONSTANTS



# 	CLASS:  "USER"
#
@dataclass(order=True, kw_only=True)
class User(ABC):
    '''Abstract Base Class (ABC) in an inheritance hierarchy that defines each type of user 
    within the Chocoholics Anonymous software package.'''
###############################################################################
###############################################################################

	################################################################
	################        Data Members for        ################
	################		    U S E R			    ################
	################################################################

    name                : str           = field(default="name",
                                                init=True,      compare=True,
                                                hash=True,      repr=True)

    id                  : str           = field(default="000000",
                                                init=True,      compare=True,
                                                hash=True,      repr=True)

    address             : str           = field(default="address",
                                                init=True,      compare=True,
                                                hash=True,      repr=True)

    city                : str           = field(default="city",
                                                init=True,      compare=True,
                                                hash=True,      repr=True)

    state               : str           = field(default="state",
                                                init=True,      compare=True,
                                                hash=True,      repr=True)

    zip                 : str           = field(default="zipcode",
                                                init=True,      compare=True,
                                                hash=True,      repr=True)


#   1.  Build-In Methods...
###############################################################################
    
    #   "__post_init__"
    #
    def __post_init__(self):
        return


#   2.  Properties...
###############################################################################

    #   "name"              | Getter.
    #@property
    #def name(self) -> str:
    #    return self.name

    #   "name"              | Setter.
    #@name.setter
    #def name(self, arg:str):
    #    self.name = arg[:_M_SIZE_CONSTANTS["name"]]
    #    return


#   3.  Member Functions...
###############################################################################
    




###############################################################################
###############################################################################
#   END "USER".






###############################################################################
###############################################################################
#   END "USERS" :: "_USER".
