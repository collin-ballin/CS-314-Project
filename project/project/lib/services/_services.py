###############################################################################
#
#       ************************************************************
#       ****       _ S E R V I C E S . P Y  ____  F I L E.      ****
#       ************************************************************
#
#
###############################################################################
from dataclasses import dataclass, field
import math, textwrap
import datetime as dt

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

    name                : str           = field(default=None,
                                                init=True,      compare=True,
                                                hash=True,      repr=True)

    id                  : str           = field(default=None,
                                                init=True,      compare=True,
                                                hash=True,      repr=True)

    patient_name        : str           = field(default=None,
                                                init=True,      compare=True,
                                                hash=True,      repr=True)

    patient_id          : str           = field(default=None,
                                                init=True,      compare=True,
                                                hash=True,      repr=True)

    provider_name       : str           = field(default=None,
                                                init=True,      compare=True,
                                                hash=True,      repr=True)

    provider_id         : str           = field(default=None,
                                                init=True,      compare=True,
                                                hash=True,      repr=True)

    dos                 : dt.date       = field(default=None,
                                                init=True,      compare=True,
                                                hash=True,      repr=True)

    dor                 : dt.datetime   = field(default=None,
                                                init=True,      compare=True,
                                                hash=True,      repr=True)

    comments            : str           = field(default=None,
                                                init=True,      compare=True,
                                                hash=True,      repr=True)

    fee                 : float         = field(default=None,
                                                init=True,      compare=True,
                                                hash=True,      repr=True)


#   1.  Build-In Methods...
###############################################################################
    
    #   "__post_init__"
    #
    def __post_init__(self):
        #self._enforce_size()
        return
        
    
    #   "__str__"
    #
    def __str__(self) -> str:
        w1      = 22
        w2      = 45
        s       = 7
        sep     = s * '.'
        pre     = w1 + s + 2
        wrapper = textwrap.TextWrapper(
            width=pre + w2,
            initial_indent=f"\n{'Provider Comments':>{w1}} {sep} ",
            subsequent_indent=' ' * (pre)
        )
    
    
        string  = ""#"Service:\t\"{self.name}\" (#{self.id})"
        
        #   1.  Service.
        string += f"{'Service':>{w1}} {sep} {self.name}" if (self.name is not None) else ''
        string += f" (#{self.id})" if ( (self.name is not None) and (self.id is not None) ) else ''
        
        #   2.  Patient.
        string += f"\n{'Patient':>{w1}} {sep} {self.patient_name}" if (self.patient_name is not None) else ''
        string += f" (#{self.patient_id})" if ( (self.patient_name is not None) and (self.patient_id is not None) ) else ''
        
        #   3.  Provider.
        string += f"\n{'Provider':>{w1}} {sep} {self.provider_name}" if (self.provider_name is not None) else ''
        string += f" (#{self.provider_id})" if ( (self.provider_name is not None) and (self.provider_id is not None) ) else ''
        
        #   4.  DOS.
        string += f"\n{'Date-of-Service':>{w1}} {sep} {self.dos.strftime( _S_SIZE_CONSTANTS['dos'] )}" if (self.dos is not None) else ''
        
        #   5.  DOR.
        string += f"\n{'Date-of-Record':>{w1}} {sep} {self.dor.strftime( _S_SIZE_CONSTANTS['dor'] )}" if (self.dor is not None) else ''
        
        #   6.  Comments.
        string += wrapper.fill(self.comments) if (self.comments is not None) else ''
        
        #   7.  Fee.
        string += f"\n{'Amount Due':>{w1}} {sep} ${self.fee:06.2f}" if (self.fee is not None) else ''
    
        return string
    
    
    
    #   "__setattr__"
    #
    def __setattr__(self, attr, value):
        value_fmt = value
        
        #   CASE 1 :    Attribute is defined in the dictionary of size-constrained values...
        if (attr in _S_SIZE_CONSTANTS):
            #
            #   CASE 1.1. :     Default value is None...
            if ( value is None ):
                super().__setattr__(attr, value)
            #
            #   CASE 1.2. :     Dealing with the "FEE" Attribute...
            elif (attr == 'fee'):
                if ( (value < _S_SIZE_CONSTANTS['min_fee']) or (_S_SIZE_CONSTANTS['max_fee'] < value) ):
                    raise ValueError(f"Service fee must be a positive value that cannot exceed ${_S_SIZE_CONSTANTS['min_fee']:06.2f}.")
                    
                super().__setattr__(attr, value)
            #
            #
            #
            #   CASE 1.3. :     Dealing with the "DOS" or "DOR" Attributes...
            elif ( attr == 'dos' ):
                #print(f"{GREEN_BB}Attempting to set \"dos\"...\n\tattr={attr}, value={value}, const[\"{attr}\"]={_S_SIZE_CONSTANTS[attr]}{RESET}")
                super().__setattr__(attr, dt.datetime.strptime(value, _S_SIZE_CONSTANTS[attr]).date())
            #
            #
            elif (attr == 'dor'):
                #print(f"{GREEN_BB}Attempting to set \"dor\"...\n\tattr={attr}, value={value}, const[\"{attr}\"]={_S_SIZE_CONSTANTS[attr]}{RESET}")
                super().__setattr__(attr, dt.datetime.strptime(value, _S_SIZE_CONSTANTS[attr]))
            #
            #
            #
            #   CASE 1.5. :     Truncate each other field...
            else:
                value_fmt = UTL.truncate(value, size=_S_SIZE_CONSTANTS[attr]).title()
                super().__setattr__(attr, value_fmt)
        #
        #
        #   CASE 2 :    Unrecognized attribute...
        else:
            super().__setattr__(attr, value_fmt)
            
            
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
