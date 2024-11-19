###############################################################################
#
#       ************************************************************
#       ****        _ U T I L I T Y . P Y  ____  F I L E.       ****
#       ************************************************************
#
#
###############################################################################
import lib.utility.ansi as ANSI
import textwrap, re



#   3.  MISC FUNCTIONS ...
################################################################################
################################################################################

#   "log"
#
def log(msg:str, type:ANSI.Log_Tag=ANSI.LOG, color:bool=True):
    log_label   = ""
    indent      = ""
    text        = ""
    tag         = ""
    
    #   Initialize the counter attribute.
    if not hasattr(log, "count_l"):
        log.count_l = 0
    if not hasattr(log, "count_w"):
        log.count_w = 0
    if not hasattr(log, "count_e"):
        log.count_e = 0
    if not hasattr(log, "count_err"):
        log.count_err = 0
    
    
    #   CASE 1 : WARN
    if (type == ANSI.WARN):
        log.count_w += 1
        tag          = (color) * f"{ANSI.YELLOW}" + (not color) * f"{ANSI.WHITE}"
        log_label    = f"WARN [{log.count_w}]:\t"
        indent       = " " * len(log_label) + "\t"# Indent for subsequent lines
        text         = textwrap.fill(msg, width=70, subsequent_indent=indent)
        text         = f"{ANSI.YELLOW_BOLD}{log_label}{tag}{text}"
    #
    #   CASE 2 : ERROR
    elif (type == ANSI.ERROR):
        log.count_err  += 1
        tag             = (color) * f"{ANSI.RED}" + (not color) * f"{ANSI.WHITE}"
        log_label        = f"ERROR [{log.count_err}]:\t"
        indent          = " " * len(log_label) + "\t"# Indent for subsequent lines
        text            = textwrap.fill(msg, width=70, subsequent_indent=indent)
        text            = f"{ANSI.RED_BOLD}{log_label}{tag}{text}"
    #
    #   CASE 3 : EVENT
    elif (type == ANSI.EVENT):
        log.count_e += 1
        tag          = (color) * f"{ANSI.BLUE}" + (not color) * f"{ANSI.WHITE}"
        log_label    = f"EVENT [{log.count_e}]:\t"
        indent       = " " * len(log_label) + "\t"# Indent for subsequent lines
        text         = textwrap.fill(msg, width=70, subsequent_indent=indent)
        text         = f"{ANSI.BLUE_BOLD}{log_label}{tag}{text}"
    #
    #   CASE 4 : DEFAULT
    else:
        log.count_l += 1
        tag          = (color) * f"{ANSI.GREEN}" + (not color) * f"{ANSI.WHITE}"
        log_label    = f"LOG [{log.count_l}]:\t"
        indent       = " " * len(log_label) + "\t"# Indent for subsequent lines
        text         = textwrap.fill(msg, width=70, subsequent_indent=indent)
        text         = f"{ANSI.GREEN_BOLD}{log_label}{tag}{text}"
       
       
    print(f"{text}{ANSI.RESET}")
    return



#   "signal_handler"
#
def signal_handler(sig, frame):
    raise KeyboardInterrupt(f"SIG: {sig}.  FRAME: {frame}.")
    return
 
 
 
#   "cleanup_all"
#
def cleanup_all():
    return
    


#   "exit_gracefully"
#
def exit_gracefully():
    return





###############################################################################
###############################################################################
#   END "UTILITY".
