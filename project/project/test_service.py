from dataclasses import dataclass, field
import math, textwrap
import datetime as dt


def truncate(text, size:int) -> str:
    return text if len(text) <= size else text[:size - 3] + "..."
    



RESET               = "\033[0m"
BLACK_BRIGHT        = "\033[90m"
RED_BRIGHT          = "\033[91m"
GREEN_BRIGHT        = "\033[92m"
YELLOW_BRIGHT       = "\033[93m"
BLUE_BRIGHT         = "\033[94m"
MAGENTA_BRIGHT      = "\033[95m"
CYAN_BRIGHT         = "\033[96m"
WHITE_BRIGHT        = "\033[97m"
BLACK_BB            = "\033[1m\033[90m"
RED_BB              = "\033[1m\033[91m"
GREEN_BB            = "\033[1m\033[92m"
YELLOW_BB           = "\033[1m\033[93m"
BLUE_BB             = "\033[1m\033[94m"
MAGENTA_BB          = "\033[1m\033[95m"
CYAN_BB             = "\033[1m\033[96m"
WHITE_BB            = "\033[1m\033[97m"



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
    "min_fee"               : 000.00,
    "max_fee"               : 999.99,
    "comments"              : _S_COMMENTS_SIZE,
    "dos"                   : "%d-%m-%Y",
    "dor"                   : "%d-%m-%Y %H:%M:%S",
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
        w2      = 35
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
        
        
        
        
        #sys.stdout.write(textwrap.dedent(f"""{ANSI.DIM}
        #{'OS NAME':>{w1}} {sep} {os.name:<{w2}}
        #{'SYSTEM PLATFORM':>{w1}} {sep} {sys.platform:<{w2}}
    
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
                value_fmt = truncate(value, size=_S_SIZE_CONSTANTS[attr]).title()
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














def main():
    s1          = Service(name="X-Ray", id="123456",
                          provider_name="Providence",    provider_id="000000001",
                          patient_name="Collin Bond",    patient_id="000000007",
                          dos="28-11-2024", dor="28-11-2024 11:37:15",
                          comments="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut",
                          fee=999.99)
                          
    s2          = Service(name="Service Name", id="123456",
                          patient_name="Collin Bond",    patient_id="000000007",
                          provider_name="Providence",    provider_id="000000001",
                          comments="some notes and comments", fee=999.99)
                          
                          
                         
    print(f"\n\nPrinting the FIRST service...\n{s1}")
    
    
    print(f"\n\nPrinting another service...\n{s2}")
    
    
    
    print(f"\n\n")
    
    return





def test_datetime():
    print("\n\n")
    
    
    #   TEST 1.
    #   1.1.    Create a date (DOS).
    print(f"{CYAN_BB}TEST #1:\n{CYAN_BRIGHT}Store a date as \"MM-DD-YYYY\"...{RESET} ")
    test_1      = dt.date(2024, 11, 28)
    date_fmt_1  = test_1.strftime( _S_SIZE_CONSTANTS['dos'] )
    print(f"\tdatetime.date(2024, 11, 28)\t\t\t=\t{date_fmt_1}")
    #
    #   1.2.    GETTING THE TYPE.
    type1   = type(test_1)
    type2   = type(date_fmt_1)
    print(f"\ttype( date(y, d, m) )\t\t\t\t=\t{RED_BB}{type1}{RESET}", end="\n")
    print(f"\ttype( date(y, d, m).strftime( ...format... ) )\t=\t{RED_BB}{type2}{RESET}", end="\n\n")


    #   TEST 2.
    #   2.1.    Create a date with a time (DOR).
    print(f"{CYAN_BB}TEST #2:\n{CYAN_BRIGHT}Store a date and time as \"MM-DD-YYYY HH-MM-SS\"...{RESET} ")
    test_2      = dt.datetime(2024, 11, 28, 14, 30, 45)
    date_fmt_2  = test_2.strftime( _S_SIZE_CONSTANTS['dor'] )
    print(f"\tdatetime.datetime(2024, 11, 28, 14, 30, 45)\t=\t{date_fmt_2}")
    #
    #   2.2.    GETTING THE TYPE.
    type1       = type(test_2)
    type2       = type(date_fmt_2)
    print(f"\ttype( datetime(y, d, m, ... ) )\t\t\t=\t{RED_BB}{type1}{RESET}", end="\n")
    print(f"\ttype( datetime(...).strftime( ...format... ) )\t=\t{RED_BB}{type2}{RESET}", end="\n\n")
    
    
    
    #   TEST 3.
    #   3.1.    Get the current DATE and TIME.
    print(f"{CYAN_BB}TEST #3:\n{CYAN_BRIGHT}Get the CURRENT date and time as \"MM-DD-YYYY HH-MM-SS\"...{RESET} ")
    test_3      = dt.datetime.now()
    date_fmt_3  = test_3.strftime( _S_SIZE_CONSTANTS['dor'] )
    print(f"\tdt.datetime.now()\t\t\t\t=\t{date_fmt_3}")
    #
    #   3.2.    GETTING THE TYPE.
    type1       = type(test_3)
    type2       = type(date_fmt_3)
    print(f"\ttype( now() )\t\t\t\t\t=\t{RED_BB}{type1}{RESET}", end="\n")
    print(f"\ttype( now().strftime( ...format... ) )\t\t=\t{RED_BB}{type2}{RESET}", end="\n\n")
    
    
    
    #   TEST 4.
    #   4.1.    CREATE A DATE OBJECT FROM A STRING...
    print(f"{CYAN_BB}TEST #4:\n{CYAN_BRIGHT}Create a date object from a \"MM-DD-YYYY\" string...\" HH-MM-SS\" string...{RESET} ")
    print(f"\t{CYAN_BB}#4.1. DATE:{RESET} ")
    date_str_1  = "28-11-2024"
    obj_1       = dt.datetime.strptime(date_str_1, _S_SIZE_CONSTANTS['dos']).date()
    print(f"\tdt.strptime(string, fmt).date()\t\t\t=\t{obj_1}")
    #
    #   4.1B.   GETTING THE TYPE.
    type1       = type(obj_1)
    print(f"\ttype( obj_1 )\t\t\t\t\t=\t{RED_BB}{type1}{RESET}", end="\n")
    
    
    #   4.2.    CREATE A DATETIME OBJECT FROM A STRING...
    print(f"\n\t{CYAN_BB}#4.2. DATETIME:{RESET} ")
    date_str_2  = "28-11-2024 11:37:15"
    obj_2       = dt.datetime.strptime(date_str_2, _S_SIZE_CONSTANTS['dor'])
    print(f"\tdt.strptime(string, fmt).date()\t\t\t=\t{obj_2}")
    #
    #   4.2B.   GETTING THE TYPE.
    type2       = type(obj_2)
    print(f"\ttype( obj_2 )\t\t\t\t\t=\t{RED_BB}{type2}{RESET}", end="\n")
    
    
    
    
    print("\n\n")
    return






if (__name__ == '__main__'):
    line = f"{MAGENTA_BB}" + '#' * 70 + f"{RESET}"
    #print(f"{line}\n{line}\n")
    
    
    #test_datetime()
    
    #print(f"{line}")
    
    main()
    
    #print(f"{line}\n{line}\n")
