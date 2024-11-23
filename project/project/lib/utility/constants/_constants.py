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



#   1.  DATA FIELD SIZE LIMITS...
###############################################################################
###############################################################################

#                           1.1.    (M) Member Limits.
_M_NAME_SIZE                = 25
_M_ID_SIZE                  = 9
_M_STREET_ADR_SIZE          = 25
_M_CITY_SIZE                = 14
_M_STATE_SIZE               = 2
_M_ZIP_SIZE                 = 5

_M_SIZE_CONSTANTS           = {
    "name"          : _M_NAME_SIZE,
    "id"            : _M_ID_SIZE,
    "address"       : _M_STREET_ADR_SIZE,
    "city"          : _M_CITY_SIZE,
    "state"         : _M_STATE_SIZE,
    "zip"           : _M_ZIP_SIZE,
}



#                           1.2.    (S) Service Limits.
_S_DATE_FMT                 = "MM-DD-YYYY"
_S_PROVIDER_NAME_SIZE       = 25
_S_SERVICE_NAME_SIZE        = 20

_S_SIZE_CONSTANTS           = {
    "date_fmt"      : _S_DATE_FMT,
    "p_name"        : _S_PROVIDER_NAME_SIZE,
    "s_name"        : _S_SERVICE_NAME_SIZE,
}



#                           1.3.    (P) Provider Limits.
_P_NAME_SIZE                = 25
_P_ID_SIZE                  = 9
_P_STREET_ADR_SIZE          = 25
_P_CITY_SIZE                = 14
_P_STATE_SIZE               = 2
_P_ZIP_SIZE                 = 5

_P_SIZE_CONSTANTS           = {
    "name"          : _P_NAME_SIZE,
    "id"            : _P_ID_SIZE,
    "address"       : _P_STREET_ADR_SIZE,
    "city"          : _P_CITY_SIZE,
    "state"         : _P_STATE_SIZE,
    "zip"           : _P_ZIP_SIZE,
}



###############################################################################
###############################################################################
#   END "UTILITY" :: "_CONSTANTS".
