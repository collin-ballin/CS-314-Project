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



#   1.  DATA FIELD SIZE LIMITS...
###############################################################################
###############################################################################

#                           1.1.    (M) Member Limits.
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



#                           1.2.    (S) Service Limits.
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
    "dos"                   : "%d-%m-%Y",
    "dor"                   : "%d-%m-%Y %H:%M:%S",
}



#                           1.3.    (P) Provider Limits.
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
#   2.  CONSTANTS FOR THE "APPLICATION" CLASS...
###############################################################################
###############################################################################
#
#
#
#   2.1.    DEFAULT PROMPTS AND MESSAGES...
###############################################################################
_LW         = 87
_PROMPTS    = {
    #   Utility Text...
    #   ...
    #
    #   Prompts / Output...
    "provider_1"        : f"Please enter your 9-digit provider ID number: ",
    #
    #
    #   Command Prompts...
    "cmd_unknown"       : "The command \"{a}\" is unrecognized.",
    "cmd_suggestion"    : "Perhaps you meant \"{a}\"?",
    #
    #
    #   Instructions / Info...
    "display_mode_ON"   : "DISPLAY MODE:  Use arrow-keys to cycle forward/backward through entries.  Press \"q\" to exit.",
    "display_mode_OFF"  : "Exiting Display Mode...",
    #
    #
    #   Exception Handling / Termination...
    "not_impl"          : "The command \"{a}\" is not implemented yet",
    "normal_exit"       : "Program terminating...  Have a great day!",
}


###############################################################################
#
#
#
#   2.2.    ACCEPTED COMMANDS FOR THE APPLICATION...
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
                              },
    "edit member"           : {     "reply"     : "...",
                                    "action"    : None,
                              },
    "remove member"         : {     "reply"     : "...",
                                    "action"    : None,
                              },
    "display members"       : {    "reply"     : "Displaying the members...",
                                    "action"    : None,
                              },
    #
    #
    #       1.2.    PROVIDER COMMANDS:
    "add provider"          : {     "reply"     : "...",
                                    "action"    : None,
                              },
    "edit provider"         : {     "reply"     : "...",
                                    "action"    : None,
                              },
    "remove provider"       : {     "reply"     : "...",
                                    "action"    : None,
                              },
    "display providers"     : {     "reply"     : "Displaying the providers...",
                                    "action"    : None,
                              },
    #
    #
    #       1.3.    SERVICE COMMANDS:
    "add service"           : {     "reply"     : "...",
                                    "action"    : None,
                              },
    "edit service"          : {     "reply"     : "...",
                                    "action"    : None,
                              },
    "remove service"        : {     "reply"     : "...",
                                    "action"    : None,
                              },
    "display services"      : {     "reply"     : "...",
                                    "action"    : None,
                              },
    ###########################################################################
    #
    #
    #
    #   2.  UTILITY COMMANDS...
    ###########################################################################
    "test"                  : {     "reply"     : "Placeholder..,",
                                    "action"    : None,
                              },
    "set title"             : {     "reply"     : "Setting the application title..,",
                                    "action"    : None,
                              },
    ###########################################################################
}
###############################################################################
###############################################################################



###############################################################################
#
#
#
#   2.2.    ACCEPTED COMMANDS FOR THE APPLICATION.
###############################################################################
_UI         = {
    #   General Constant Values...
    "fg"                    : curses.COLOR_WHITE,
    #
    #   Constants for Title...
    "title_offset"          : 2,
    "title_padding"         : 1,
}


###############################################################################
###############################################################################










###############################################################################
###############################################################################
#   END "UTILITY" :: "_CONSTANTS".
