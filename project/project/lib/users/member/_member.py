###############################################################################
#
#           "U_S_E_R_S"         M O D U L E.
#
#         "M_E_M_B_E_R"         S U B - M O D U L E.
#
#
#             File:             "_member.py".
#
###############################################################################
from dataclasses import dataclass, field
import lib.utility as UTL
from lib.users.user import User
from lib.utility import Cstring
from lib.utility.constants import _M_SIZE_CONSTANTS



# 	CLASS:  "Member"
#
@dataclass(order=True, kw_only=True)
class Member(User):
    '''Class to define a \"Member\" (a patient) of the Chocoholics Anonymous program.'''
###############################################################################
###############################################################################

	################################################################
	################        Data Members for        ################
	################		  M E M B E R		    ################
	################################################################

    history             : list          = field(default_factory=list,
                                                metadata={"description": "list of services"},
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
        return f'''{self.name} ({self.id}).  {self.address}, {self.city}'''
    
    
    #   "__setattr__"
    #
    def __setattr__(self, attr, value):
        #   CASE 1 :    Attribute is inside base-class.
        if (attr in _M_SIZE_CONSTANTS):
            crop = value[ :_M_SIZE_CONSTANTS[attr] ]
            UTL.log(f"Setting \"{attr}\" with \"{value}\".\nCropped = {crop}")
            super().__setattr__(attr, value)
        #
        #   CASE 2 :
        else:
            super().__setattr__(attr, value)
            
        return
            

#   3.  Member Functions...
###############################################################################
    
    #   "_enforce_size"
    #
    def _enforce_size(self):
        #self.name       = self.name[:_M_SIZE_CONSTANTS["name"]]
        #self.id         = self.id[:_M_SIZE_CONSTANTS["id"]]
        #self.address    = self.address[:_M_SIZE_CONSTANTS["address"]]
        #self.city       = self.city[:_M_SIZE_CONSTANTS["city"]].upper()
        #self.state      = self.state[:_M_SIZE_CONSTANTS["state"]].upper()
        #self.zip        = self.zip[:_M_SIZE_CONSTANTS["zip"]]
    
        return
        
        
###############################################################################
###############################################################################
#   END "MEMBER".




###############################################################################
###############################################################################
#   END "USERS" :: "_MEMBER".
