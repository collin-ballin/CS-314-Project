###############################################################################
#
#   "C_O_N_S_T_A_N_T_S"          M O D U L E.
#
#             "A_N_S_I"          S U B - M O D U L E.
#
#
#                 File:         "_constants.py".
#
###############################################################################
import curses
from enum import Enum, auto



#   1.  CLASS TO DEFINE TAGS FOR LOG-IN PERMISSIONS ...
###############################################################################
###############################################################################
#   Define an enum for EACH TYPE OF LOG.
class Permissions(Enum):
    MEMBER          = auto()
    PROVIDER        = auto()
    ADMINISTRATOR   = auto()
    ROOT            = auto()
    
    
#   1.1.    CONSTANT VALUES FOR LOG TAGS ...
###############################################################################
#   Log-Type Tags.
MEMBER                      = Permissions.MEMBER
PROVIDER                    = Permissions.PROVIDER
ADMINISTRATOR               = Permissions.ADMINISTRATOR
ROOT                        = Permissions.ROOT






#   2.  DATA FIELD SIZE LIMITS...
###############################################################################
###############################################################################

#                           2.1.    (M) Member Limits.
_M_NAME_SIZE                = 25
_M_ID_SIZE                  = 9
_M_ADDRESS_SIZE             = 25
_M_CITY_SIZE                = 14
_M_STATE_SIZE               = 2
_M_ZIP_SIZE                 = 5

_M_SIZE_CONSTANTS           = {
    "name"          : _M_NAME_SIZE,
    "id"            : _M_ID_SIZE,
    "address"       : _M_ADDRESS_SIZE,
    "city"          : _M_CITY_SIZE,
    "state"         : _M_STATE_SIZE,
    "zip"           : _M_ZIP_SIZE,
}



#                           2.2.    (S) Service Limits.
#
#   1.  Names...
_S_NAME_SIZE                = 20                        #   Name of service.
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
    "dos"                   : "%m-%d-%Y",
    "dor"                   : "%m-%d-%Y %H:%M:%S",
}



#                           2.3.    (P) Provider Limits.
_P_NAME_SIZE                = 25
_P_ID_SIZE                  = 9
_P_ADDRESS_SIZE             = 25
_P_CITY_SIZE                = 14
_P_STATE_SIZE               = 2
_P_ZIP_SIZE                 = 5

_P_SIZE_CONSTANTS           = {
    "name"          : _P_NAME_SIZE,
    "id"            : _P_ID_SIZE,
    "address"       : _P_ADDRESS_SIZE,
    "city"          : _P_CITY_SIZE,
    "state"         : _P_STATE_SIZE,
    "zip"           : _P_ZIP_SIZE,
}



###############################################################################
###############################################################################
#
#
#
#
#
#
#   3.  CONSTANTS FOR THE "APPLICATION" CLASS...
###############################################################################
###############################################################################
#
#
#
#   3.1.    DEFAULT PROMPTS AND MESSAGES...
###############################################################################
_LW         = 87
_PROMPTS    = {
    #   Utility Text...
    "login_status-out"  : "signed-out",
    "login_status"      : "{a}",#"signed-in as {a}",
    "pause"             : "Press any key to continue..:",
    #
    #   Prompts / Output...
    "welcome_1"         : "WELCOME TO COCOA---The Chocoholics-Anonymous Organization and Clinical Operations Application!",
    "welcome_2"         : "To sign-in, please enter your 9-Digit Identification Number (or type \"ADMIN\" to run as administrator).",
    #
    "login_success"     : "LOG-IN SUCCESS...  Signed-in as {a}{b}.  Welcome{c}!\n",
    "login_unknown"     : "LOG-IN FAILURE...  User-ID (#{a}) is not registered in our database.",
    #
    #
    #   Command Prompts...
    "cmd_greeting"      : "Please enter a command:\n",
    "cmd_unknown"       : "The command \"{a}\" is unrecognized.",
    "cmd_suggestion"    : "Perhaps you meant {a}?",
    "not_impl"          : "The command \"{a}\" has not been implemented yet.\n",
    "bad_access"        : "You do not have permission to access the command \"{a}\".\n",
    #
    #
    #   Prompts for Specific Functions...
    "cancel_operation"  : "Cancelling the operation...\n",
    "verify_input"      : "Please verify that the following information is correct (Y/N):\n",
    "operation_success" : "Successfully {a}{b}{c}.\n",
    #
    #
    #   Instructions / Info...
    "display_mode_ON"   : "DISPLAY MODE:  Use arrow-keys to cycle forward/backward through entries.  Press \"q\" to exit.",
    "display_mode_OFF"  : "Exiting Display Mode...",
    #
    #
    #   Exception Handling / Termination...
    "normal_exit"       : "Logging out and saving changes to the database...  Program will now proceed to terminate.\nHave a great day!",
    "ctrl-c_exit"       : "Program recieved CTRL-C Logging out and saving changes to the database...  Program will now proceed to terminate.\nHave a great day!",
    "login_terminate"   : "Maximum number of login attemps has been exceeded.\nProgram will now proceed to terminate.",
    "bad_load"          : "CRITICAL ERROR.  The database file \"{a}\" could not be loaded and/or contains no data.  Program terminating.",
}


###############################################################################
#
#
#
#   3.2.    ACCEPTED COMMANDS FOR THE APPLICATION...
###############################################################################
###############################################################################
_COMMANDS    = {
    #
    #   1.  OPERATION COMMANDS...
    ###########################################################################
    #
    #       1.1.    MEMBER COMMANDS:
    "add member"            : {     "reply"     : "...",
                                    "action"    : None,
                                    "accessors" : PROVIDER,
                              },
    "edit member"           : {     "reply"     : "...",
                                    "action"    : None,
                                    "accessors" : PROVIDER,
                              },
    "remove member"         : {     "reply"     : "...",
                                    "action"    : None,
                                    "accessors" : PROVIDER,
                              },
    "display members"       : {    "reply"     : "Displaying the members...",
                                    "action"    : None,
                                    "accessors" : PROVIDER,
                              },
    #
    #
    #       1.2.    PROVIDER COMMANDS:
    "add provider"          : {     "reply"     : "...",
                                    "action"    : None,
                                    "accessors" : PROVIDER,
                              },
    "edit provider"         : {     "reply"     : "...",
                                    "action"    : None,
                                    "accessors" : PROVIDER,
                              },
    "remove provider"       : {     "reply"     : "...",
                                    "action"    : None,
                                    "accessors" : PROVIDER,
                              },
    "display providers"     : {     "reply"     : "Displaying the providers...",
                                    "action"    : None,
                                    "accessors" : (MEMBER, PROVIDER),
                              },
    #
    #
    #       1.3.    SERVICE COMMANDS:
    "add service"           : {     "reply"     : "...",
                                    "action"    : None,
                                    "accessors" : PROVIDER,
                              },
    "edit service"          : {     "reply"     : "...",
                                    "action"    : None,
                                    "accessors" : PROVIDER,
                              },
    "remove service"        : {     "reply"     : "...",
                                    "action"    : None,
                                    "accessors" : PROVIDER,
                              },
    "display services"      : {     "reply"     : "...",
                                    "action"    : None,
                                    "accessors" : (MEMBER, PROVIDER),
                              },
    ###########################################################################
    #
    #
    #
    #   2.  UTILITY COMMANDS...
    ###########################################################################
    "open the pod bay doors, hal" \
                            : {     "reply"     : "I'm sorry, Dave.  I'm afraid I can't do that.",
                                    "action"    : None,
                                    "accessors" : (MEMBER, PROVIDER),
                              },
    "quit"                  : {     "reply"     : "",
                                    "action"    : None,
                                    "accessors" : (MEMBER, PROVIDER),
                              },
    "test"                  : {     "reply"     : "...",
                                    "action"    : None,
                                    "accessors" : ROOT,
                              },
    "set title"             : {     "reply"     : "Setting the application title..,",
                                    "action"    : None,
                                    "accessors" : ROOT,
                              },
    ###########################################################################
}
###############################################################################
###############################################################################






#   4.0.    INITIAL CONSTANTS FOR THE USER-INTERFACE.
###############################################################################
###############################################################################
_HEAD_POS   = (3, 2)
_INSET      = 1
_HEAD       = {
    'height'        : 1,
    'width'         : None,
    'pos'           : _HEAD_POS,
    'title'         : 'COCOA (CHOC-AN ORGANIZATION AND CLINICAL OPERATIONS APPLICATION)'
}
_OUT        = {
    'height'        : 15,
    'width'         : None,
    'pos'           : ( 3 + _HEAD_POS[0],       0 + _HEAD_POS[0] + _INSET ),
    'title'         : 'OUTPUT'
}
_IN         = {
    'height'        : 1,
    'width'         : None,
    'pos'           : ( 25 + _HEAD_POS[0],      3 + _HEAD_POS[1] + _INSET ),
    'title'         : 'INPUT'
}

_INIT_UI    = {
    'head'          : _HEAD,
    'out'           : _OUT,
    'in'            : _IN,
}
 
 
        
#   4.0.    CONSTANTS FOR THE USER-INTERFACE.
###############################################################################
###############################################################################
_UI         = {
    #   General Constant Values...
    "fg"                    : curses.COLOR_WHITE,
    #
    #   Constants for Title...
    "title_offset"          : 2,
    "title_padding"         : 1,
}



#   5.0.    GENERAL APPLICATION CONSTANTS.
###############################################################################
###############################################################################
_GENERAL         = {
    "word_bank"             : ["add", "remove", "edit", "display"],
    "login-attempts"        : 5,
    "files"                 : {
        'all'       : "data/all.json",
        'backup'    : "data/all_copy.json",
        'members'   : "data/members.json",
        'providers' : "data/providers.json",
        'backup_1'  : "data/members_copy.json",
        'backup_2'  : "data/providers_copy.json",
    },
}


###############################################################################
###############################################################################












###############################################################################
###############################################################################
#   END "UTILITY" :: "_CONSTANTS".
