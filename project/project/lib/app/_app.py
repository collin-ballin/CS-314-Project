###############################################################################
#
#       ************************************************************
#       ****            _ A P P . P Y  ____  F I L E.           ****
#       ************************************************************
#
#
###############################################################################
from dataclasses import dataclass, field
from lib.user import User
from lib.utility.cstring import Cstring
import lib.utility.ansi as ANSI
import lib.utility as UTL



#   MEMBER FUNCTION FOR "APP" CLASS (IMPORTED)...
###############################################################################
###############################################################################

#   "__post_init__"
#
def __post_init__(self):
    
    return
    
    
#   "main"
#
def main(self):
    UTL.log("Inside the \"App\" class...", ANSI.NOTE)
   
   
    t1      = "Here is a name"
    t1      = "Here is a name"
    t2      = "Here is a whole lot of text and even some more text, lots of text"
    s1      = 15
    s2      = 15
    S1      = Cstring(t1, s1)
    S2      = Cstring(t2, s2)
    
    
    UTL.log(f"Constructing a Cstring[{s1}] with the text:\"{t1}\"[{len(t1)}]...",)
    UTL.log(f"Displaying the Cstring:\t\t\t\t\t\t\t\"{S1}\"", ANSI.WARN)
    
    UTL.log(f"Constructing a Cstring[{s2}] with the text:\"{t2}\"[{len(t2)}]...",)
    UTL.log(f"Displaying the Cstring:\t\t\t\t\t\t\t\"{S2}\"", ANSI.WARN)
    
    
    data = S2.data
    UTL.log(f"Using \"getter\" to get the data...data=\"{data}\"",)
    
    size = S2.size
    UTL.log(f"Using \"getter\" to get the size...size=\"{size}\"",)
    
    
    UTL.log(f"Attempting to change the data...", ANSI.WARN)
    data = "changed"
    
    UTL.log(f"Displaying the data...data=\"{S2.data}\"", ANSI.WARN)
    
    
    
    S2.data = "Test"
    UTL.log(f"Modifying the data...S2=\"{S2}\"", ANSI.EVENT)
    
    my_user = User(name="Name")
    
    return





###############################################################################
###############################################################################
#   END.
