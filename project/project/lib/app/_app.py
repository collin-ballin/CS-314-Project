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
   
    
    member_1    = Member(name="Collin A. Bond and a lot of text",   id="1234123412341234",
                         address="308 Negra Arroyo Lane",           state="Oregon",
                         city="Portland")
                         
    member_2    = Member(name="Walter H. White",                    id="490662",
                         address="308 Negra Arroyo Lane",           city="Albuquerque",
                         state="NM",                                zip="87104")
    
   
    member_2.display()
    
    return





###############################################################################
###############################################################################
#   END.
