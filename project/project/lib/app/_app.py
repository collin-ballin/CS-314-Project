###############################################################################
#
#       ************************************************************
#       ****            _ A P P . P Y  ____  F I L E.           ****
#       ************************************************************
#
#
###############################################################################
from dataclasses import dataclass, field
from lib.utility import Cstring
from lib.utility import ANSI
import lib.utility as UTL
from lib.users import Member


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
    S1      = Cstring(size=s1, data=t1)
    #S2      = Cstring(t2, s2)
    
    
    #UTL.log(f"Constructing a Cstring[{s1}] with the text:\"{t1}\"[{len(t1)}]...",)
    #UTL.log(f"Displaying the Cstring:\t\t\t\t\t\t\t\"{S1}\"", ANSI.WARN)
    
    
    #member_1    = Member(name="Collin A. Bond")
    member_2    = Member(name="Walter H. White", id="490662", address="308 Negra Arroyo Lane", state="NM", city="ABQ")
    
    #UTL.log(f"Printing a Member:\n{member_1}",)
    UTL.log(f"Printing another Member:\n{member_2}")
    
    
    UTL.log("Second Stage...", ANSI.NOTE)
    
    
    member_2.name = "Jesse Pinkman"
    UTL.log(f"Changing the member's name...\n{member_2}", ANSI.WARN)
    
    
    test = member_2.name
    test = "Walter H. White"
    UTL.log(f"Trying to change it back...\n{member_2}", ANSI.ERROR)
    
    
    return





###############################################################################
###############################################################################
#   END.
