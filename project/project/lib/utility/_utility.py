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
def log(msg: str, type:ANSI.Log_Tag=ANSI.Log_Tag.LOG, color:bool=True, linewidth:int=ANSI.LOG_LINEWIDTH, log_types=ANSI.LOG_STYLES):
    if not hasattr(log, "counters"):#   0.  Define function 'counter' attributes.
        log.counters = {
            ANSI.Log_Tag.WARN:      0,
            ANSI.Log_Tag.ERROR:     0,
            ANSI.Log_Tag.EVENT:     0,
            ANSI.Log_Tag.NOTE:      0,
            ANSI.Log_Tag.LOG:       0
        }

    if type not in log_types:#          2.  Default value if unknown type is provided...
        type = ANSI.Log_Tag.LOG

    config              = log_types[type]
    log_label           = f"{config['label']} [{log.counters[type]}]:{ANSI.RESET}\t"
    indent              = " " * len(log_label) + "\t"  # Indent for subsequent lines
    segments            = msg.split('\n')
    wrapped_segments    = []
    for idx, segment in enumerate(segments):
        if (idx == 0):      #   First Segment.
            remaining   = linewidth - len(log_label)#   Fallback to a reasonable width.
            if (remaining < 20): remaining = 50
                
            wrapped     = textwrap.fill(
                segment, width=remaining, initial_indent='', subsequent_indent=indent
            )
        else:               #   Subsequent segments.  Use indent for both initial and subsequent indent.
            wrapped = textwrap.fill(
                segment, width=linewidth, initial_indent=indent, subsequent_indent=indent
            )
        wrapped_segments.append(wrapped)
    wrapped_text = '\n'.join(wrapped_segments)

    if (color):#    Apply color coding if enabled
        label_colored = f"{config['color_code']}{log_label}"
        body_colored = f"{config['tag_color']}{wrapped_text}{ANSI.RESET}"
    else:
        label_colored = f"{log_label}"
        body_colored = f"{wrapped_text}"

    print(label_colored, end='')#       3.  Print the label and the message body.
    print(body_colored)
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
