###############################################################################
#
#       ************************************************************
#       ****        _ U T I L I T Y . P Y  ____  F I L E.       ****
#       ************************************************************
#
#
###############################################################################
import lib.utility.ansi as ANSI
import os, sys, signal, platform, sysconfig, traceback
import textwrap, re



#   1.  MISC FUNCTIONS ...
################################################################################
################################################################################

#   "log"
#
def log(msg: str, type:ANSI.Log_Tag=ANSI.Log_Tag.LOG, color:bool=True, linewidth:int=ANSI.LOG_LINEWIDTH, log_types=ANSI.LOG_STYLES):
    if type not in log_types:#          2.  Default value if unknown type is provided...
        type = ANSI.LOG
        
    log_types[type]['count']   += 1
    config                      = log_types[type]
    log_label                   = f"{config['label']} [{log_types[type]['count']}]:{ANSI.RESET}\t"
    indent                      = " " * len(log_label) + "\t"  # Indent for subsequent lines
    segments                    = msg.split('\n')
    wrapped_segments            = []
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


#   "truncate"
#
def truncate(text, size:int) -> str:
    return text if len(text) <= size else text[:size - 3] + "..."
        
        
#   "hanging_indent"
#
def hanging_indent(input_text:str, level:int=1) -> str:
    if (not input_text):
        return input_text

    indentation = '\n' + '\t' * level
    return input_text.replace('\n', indentation)


#   "make_dboxed"
#
def make_dboxed(text:str, textcolor:str=ANSI.WHITE, boxcolor:str=ANSI.WHITE, lw:int=50) -> str:
    wrapped_lines   = textwrap.wrap(text, width=lw)
    max_lw          = max(len(line) for line in wrapped_lines)
    width           = max_lw + 2
    top             = f"{boxcolor}╔{'═' * width}╗{ANSI.RESET}"
    bottom          = f"{boxcolor}╚{'═' * width}╝{ANSI.RESET}"
    boxed           = [top]
    
    #   Create each line within the box...
    for line in wrapped_lines:
        centered_text = line.center(max_lw)
        colored_text = f"{ANSI.RESET}{textcolor}{centered_text}{ANSI.RESET}"
        box_line = f"{boxcolor}║ {colored_text} {boxcolor}║{ANSI.RESET}"
        boxed.append(box_line)
    
    boxed.append(bottom)
    return "\n".join(boxed)
    
    
    
#   "make_boxed"
#
def make_boxed(text:str, textcolor:str=ANSI.WHITE, boxcolor:str=ANSI.WHITE) -> str:
    w = len(text) + 2
    
    return boxcolor                                         + \
           "╔"      + "═"*w     +  "╗\n"                    + \
           "║ "     + f"{ANSI.RESET}{textcolor}{text}"      + \
           f"{ANSI.RESET}{boxcolor} ║\n"                    + \
           "╚"      + "═"*w     +  "╝"



################################################################################
#
#
#
#   2.  APPLICATION UTILITY FUNCTIONS ...
################################################################################
################################################################################

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


#   "system_info"
#
def system_info():
    sys.stdout.write(f"{ANSI.CLEAR}")
    w1      = 22
    w2      = 20
    sep     = 7 * '.'
    sys.stdout.write(textwrap.dedent(f"""{ANSI.DIM}
    {'OS NAME':>{w1}} {sep} {os.name:<{w2}}
    {'SYSTEM PLATFORM':>{w1}} {sep} {sys.platform:<{w2}}
    {'SYSTEM CONFIGURATION':>{w1}} {sep} {sysconfig.get_platform():<{w2}}
    {'SYSTEM MACHINE':>{w1}} {sep} {platform.machine():<{w2}}
    {'SYSTEM ARCHITECTURE':>{w1}} {sep} {platform.architecture()[0]:<{w2}}{ANSI.RESET_ALL}\n"""))
    
    return
    
    
#   "manual"
#
def manual():
    fmt     = f"{ANSI.RESET_ALL}{ANSI.GREEN_BRIGHT}"
    w1      = 22
    w2      = 20
    sep     = 7 * '.'
        
    def header(text:str):
        return f"{ANSI.CYAN_BB}{text}{fmt}"
        
    def underline(text:str):
        return f"{ANSI.WHITE_BRIGHT}{ANSI.UNDERLINE}{text}{fmt}"
        
    def hl(text:str):
        return f"{ANSI.CYAN_BB}{text}{fmt}"
        
    def auth(name:str, email:str):
        return f"{fmt}{ANSI.WHITE_BRIGHT}{name} <{underline(email)}{ANSI.WHITE_BRIGHT}>{fmt}"
        
    
    manual = textwrap.dedent(f"""
    {fmt}Displaying the \"man\" page for the software package...
    {header('NAME')}
            The {hl('C')}hocoholics anonymous {hl('O')}rganization and {hl('C')}linical {hl('O')}perations {hl('A')}pplication ({hl('COCOA')}).
    
    
    {header('SYNOPSIS')}
            (venv)      python      main.py
    
    
    {header('DESCRIPTION')}
            {hl('COCOA')} is a software application designed to meet the needs of a hypothetical healthcare organization
            \"Chocoholics Anonymous\", or ChocAn, which treats those who struggle with chocolate addiction in a similar manner
            to the real-world organization \"Alcoholics Anonymous\" (AA).
            
            This is a command-line application that is intended to be used by healthcare providers, consultants, or those 
            otherwise affiliated with the ChocAn Network.  
    
        {header('Dependencies')}
            The implementation of this application utilizes several external Python packages and, as such, is required to
            be run within a Python \"{hl('virtual environment')}\" (venv) that has these packages installed.  
            The following is a list of these dependencies...
            "{hl('re')}",                   "{hl('enum')}",                 "{hl('pydantic')}",             "{hl('signal')}",     
            "{hl('signal')}",               "{hl('traceback')}",            "{hl('dataclasses')}",          "{hl('datetime')}",             
            "{hl('unittest')}"
            
    
    {header('ABOUT')}
    {'INSTITUTION':>{w1}} {sep} {hl('Portland State University'):<{w2}}
    {'AFFILIATION':>{w1}} {sep} {hl('Maseeh College of Engineering and Computer Science'):<{w2}}
    {'PROFESSOR':>{w1}} {sep} {hl('Christopher Gilmore'):<{w2}}
    {'COURSE':>{w1}} {sep} {hl('CS-314 Elements of Software Engineering'):<{w2}}
    {'DATE':>{w1}} {sep} {hl('Fall, 2024'):<{w2}}
    
    
    {header('AUTHORS')}
            This project was written and developed by {underline('GROUP #6')} of the CS-314 Class...
            - {auth('Hemu Babis', 'hemu@pdx.edu')},          
            - {auth('Elizabeth Barnett', 'eb32@pdx.edu')},         
            - {auth('Michael Bell', 'bellmic@pdx.edu')},  
            - {auth('Collin Bond', 'collin23@pdx.edu')},
            - {auth('Daniel Huynh', 'dahuynh@pdx.edu')},        
            - {auth('Q Ntsasa', 'ntsasa@pdx.edu')}.
    
    
    {header('MISC')}
            ...
    
    
    {ANSI.RESET_ALL}
    """)
    sys.stdout.write(textwrap.dedent(manual))
    return


################################################################################
#
#
#
#
#
#
###############################################################################
###############################################################################
#   END "UTILITY".
