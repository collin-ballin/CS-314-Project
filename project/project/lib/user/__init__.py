###############################################################################
#
#       ************************************************************
#       ****        ________  I N I T  ________  F I L E        ****
#       ****                                                    ****
#       ****        For  "_user.py"                             ****
#       ************************************************************
#
#
###############################################################################
from dataclasses import dataclass, field






# 	CLASS:  "USER"
#
@dataclass(order=True, kw_only=True)
class User:
	'''Class to define a user of the healthcare managment system.
It may be a good idea to use this as a base class of an inheritance hierarchy and 
then implement the following derived types:
    - "Member" : to define those who recieve healthcare from ChocAn.
    - "Provider" : to define a healthcare provider/organization within the ChocAn network.'''
###############################################################################

    #   Class Methods (Imported from "_name.py" files)...
	from ._user import __post_init__
 
 
	################################################################
	################        Data Members for        ################
	################		     A P P			    ################
	################################################################
	name: 			str			    = field(default=None,
                                            init=True,              compare=True,
                                            hash=True,              repr=True)
  

###############################################################################
#   END OF "APP".
#
#
#
#
#
###############################################################################
###############################################################################
#   END "__INIT__" FOR "USER".
