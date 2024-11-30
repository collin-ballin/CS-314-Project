from dataclasses import dataclass, field
import math




def truncate(text, size:int) -> str:
    return text if len(text) <= size else text[:size - 3] + "..."
    
    
    

#   1.  Names...
_S_NAME_SIZE                = 25                        #   Name of service.
_S_PROVIDER_NAME_SIZE       = 25                        #   Name of Provider
_S_PATIENT_NAME_SIZE        = 25                        #   Name of Patient (Member)

#   2.  ID Numbers...
_S_ID_SIZE                  = 6                         #   ID of service.
_S_PROVIDER_ID_SIZE         = 9                         #   ID of Provider
_S_PATIENT_ID_SIZE          = 9                         #   ID of Patient (Member)


#   3.  Misc. Members...
_S_FEE_SIZE                 = '3.2'                     #   $999.99.    SERVICE FEE.
_S_COMMENTS_SIZE            = 100                       #   Comments / Notes...
_S_DOS_FMT                  = 'MM-DD-YYYY'              #   DOS = DATE-OF-SERVICE.
_S_DOR_FMT                  = 'MM-DD-YYYY HH:MM:SS'     #   DOR = DATE-OF-RECORD.



_S_SIZE_CONSTANTS           = {
    #   Names.
    "name"                  : _S_NAME_SIZE,
    "provider_name"         : _S_PROVIDER_NAME_SIZE,
    "patient_name"          : _S_PATIENT_NAME_SIZE,
    #
    #   ID numbers.
    "ID"                    : _S_ID_SIZE,
    "provider_ID"           : _S_PROVIDER_ID_SIZE,
    "patient_ID"            : _S_PATIENT_ID_SIZE,
    #
    #   Misc. Fields.
    "fee"                   : _S_FEE_SIZE,
    "comments"              : _S_COMMENTS_SIZE,
    "dos"                   : _S_DOS_FMT,
    "dor"                   : _S_DOR_FMT,
}



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

    fee                 : float         = field(default=None,
                                                init=True,      compare=True,
                                                hash=True,      repr=True)

    comments            : str           = field(default=None,
                                                init=True,      compare=True,
                                                hash=True,      repr=True)

    provider_name       : str           = field(default=None,
                                                init=True,      compare=True,
                                                hash=True,      repr=True)

    provider_id         : str           = field(default=None,
                                                init=True,      compare=True,
                                                hash=True,      repr=True)

    patient_name        : str           = field(default=None,
                                                init=True,      compare=True,
                                                hash=True,      repr=True)

    patient_id          : str           = field(default=None,
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
        
        string  = f"Service: \"{self.name}\" ({self.id})\n"
        string += f""
        
        #text if len(text) <= size else text[:size - 3] + "..."
        
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
                pass
            #
            #   CASE 1.2. :     Dealing with the "FEE" Attribute...
            elif ( (attr == 'fee') ):
                pass
            #
            #   CASE 1.3. :     Truncate each other field...
            else:
                value_fmt = truncate(value, size=_S_SIZE_CONSTANTS[attr]).title()
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














def main():
    s1          = Service(name="X-Ray", id="123456", comments="some notes and comments", fee=999.99,
                          provider_name="Providence",    provider_id="000000001",
                          patient_name="Collin Bond",    patient_id="000000007")
                          
    s2          = Service(id="123456", comments="some notes and comments", fee=999.99,
                          provider_name="Providence",    provider_id="000000001",
                          patient_name="Collin Bond",    patient_id="000000007")
                          
                         
    print(f"\n\nPrinting the FIRST service...\n{s1}")
    
    
    print(f"\n\nPrinting another service...\n{s2}")
    
    
    
    print(f"\n\n")
    
    return










if (__name__ == '__main__'):
    main()
