###############################################################################
#
#           "U_S_E_R_S"         M O D U L E.
#
#     "P_R_O_V_I_D_E_R"         S U B - M O D U L E.
#
#
#             File:             "_provider.py".
#
###############################################################################
from dataclasses import dataclass, field
import math
from lib.utility import ANSI
import lib.utility as UTL
from lib.users.user import User
from lib.utility import Cstring
from lib.utility.constants import _M_SIZE_CONSTANTS



# 	CLASS:  "Provider"
#
@dataclass(order=True, kw_only=True)
class Provider(User):
    '''Class to define a \"Member\" (a patient) of the Chocoholics Anonymous program.'''
###############################################################################
###############################################################################

	################################################################
	################        Data Members for        ################
	################		P R O V I D E R		    ################
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
        if (attr in _M_SIZE_CONSTANTS):
            #value_fmt = value[ :_M_SIZE_CONSTANTS[attr] ].title()
            value_fmt = UTL.truncate(value, size=_M_SIZE_CONSTANTS[attr]).title()
            
            #     CASE 1.1 :    Capitalize arguments for "city".
            if (attr == "state"):
                value_fmt = UTL.truncate(value, size=_M_SIZE_CONSTANTS["state"]).title()
                value_fmt = value_fmt.upper()
            
            super().__setattr__(attr, value_fmt)
        #
        #
        #   CASE 2 :    Attempt to set/access an unrecognized attribute.
        else:
            UTL.log(f"Accessing unrecognized attribute, \"{attr}\", in class \"Member\".", ANSI.WARN)
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
        
        record_length   = len(self.history)
        
        string          = f'''PROVIDER:   {self.name} 
            ID-NUMBER           : (#{self.id}).  
            STREET ADDRESS      : {self.address}, 
            CITY                : {self.city}, 
            STATE               : {self.state},  
            {record_length} Service Records.'''
    
        return
        
    #   "display"
    #
    def display(self, output:bool=True) -> str:
        string          = ""
        record          = ""
        record_length   = len(self.history)
        length          = 15
        
        #   "left"  = True              ===> LEFTHAND-ALIGNMENT.
        #   "fc" = "fill character".    "ic" = "indent character".
        def fmt(label:str, value:str, indent:bool=True, m_indent:bool=False, left:bool=False, fc='.', ic=' ', w:int=length) -> str:
            space = (w - len(label))
            if (indent):
                fill        = 4
                label_fmt   = "{:{char}<{w}}".format(label, char=fc, w=int(1.2*w))  if (left) else "{:{char}>{w}} ".format(label, char=ic, w=int(1.2*w))
                indent      = f"{w*ic}\t"
                more_indent = math.floor(fill/2) if (m_indent) else 0
                data        = f"{label_fmt}{ math.ceil(fill/2) * fc }\t{value}\n" if (m_indent) else f"{label_fmt}{fill * fc}\t{value}\n"
                return indent + more_indent*ic + data
                
            return f"{label}{space * ic}\t{value}\n"


        
        for i in range(0, record_length):
            record += fmt(f'ENTRY [{1+i:02}] ', f"{self.history[i]}", m_indent=True, left=True)
            
        string  = ANSI.WHITE_BB + ANSI.UNDERLINE                                            \
                  + fmt('PROVIDER ', self.name, ic='.', indent=False)                       \
                  + ANSI.RESET                                                              \
                  + fmt('ID NUMBER ', self.id, left=True)                                   \
                  + fmt('STREET ADDRESS', self.address)         + fmt('CITY', self.city)    \
                  + fmt('STATE', self.state)                    + fmt('ZIPCODE', self.zip)
        string += "\n" + fmt('HISTORY ', f"{record_length} RECORDS OF SERVICE", left=True)
        string += record


        #   CASE 1 :    Function is instructed to output text to standard output.
        if (output):     print(string)
        #UTL.log(f"Printing the __str__:\n{self}",)
        
        return string
        
        
###############################################################################
###############################################################################
#   END "PROVIDER".




###############################################################################
###############################################################################
#   END "USERS" :: "_PROVIDER".
