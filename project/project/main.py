###############################################################################
#
#       ************************************************************
#       ****            M A I N . P Y  ____  F I L E.           ****
#       ************************************************************
#
#
#     AUTHORS:      ╔══  GROUP #6  ═════════════════════════════╗
#                   ║                                           ║
#                   ║  Hemu Babis,         Elizabeth Barnett,   ║
#                   ║  Michael Bell,       Collin Bond,         ║
#                   ║  Daniel Huynh,       Q Ntsasa.            ║
#                   ╚═══════════════════════════════════════════╝
#
#   PROFESSOR:      Christopher Gilmore
#
#      COURSE:      CS-314 Elements of Software Engineering.
#
#       DATED:      Fall, 2024.
#
###############################################################################
from lib.utility import ANSI
import lib.utility as UTL
import lib as app
import termios, tty, select
import os, sys, signal, traceback
import textwrap


    
#   "main"
#
def main() -> int:
    status                  = 0
    fd                      = sys.stdin.fileno()
    init_terminal_settings  = termios.tcgetattr(fd)
    signal.signal(signal.SIGINT, UTL.signal_handler)
    
    print(f"\n{ANSI.DIM}Invoking 'main()'...  Press Ctrl+C to interrupt.\n" + '#'*70 + f"{ANSI.RESET_ALL}\n")
    
    #   1.  MAIN PROGRAM LOOPS ...
    try:
        my_app = app.App()
        my_app.main()
    #
    #
    #   2.  EXCEPTION-CATCHING BLOCKS ...
    except KeyboardInterrupt as e:
        UTL.log(f"Caught CTRL-C Keyboard Interuption.  Exiting...")
        UTL.log(f"{e}",color=False)
        
    except Exception as e:
        UTL.log("FALLBACK EXCEPTION CASE.  An specified exception has been thrown.",type=ANSI.ERROR)
        UTL.log(f"{e}",color=False)
        
        traceback.print_exc()
        status = 1
    #
    #
    #   3.  ALWAYS RUNS (W/O NOT EXCEPTION IS THROWN) ...
    finally:
        print(f"\n{ANSI.DIM}" + '#'*70)
        
        if (status==0):
            print("Successful program termination" + f" {ANSI.GREEN}(exit status \"{status}\").",end="")
        else:
            print("Unuccessful program termination" + f" {ANSI.RED}(exit status \"{status}\").",end="")
        print(f"{ANSI.RESET_ALL}")
    
        termios.tcsetattr(fd, termios.TCSADRAIN, init_terminal_settings)
    
    
    return status


    
###############################################################################

#   Hook for the "main" function...
#
if (__name__ == '__main__'):

    #   CASE 1 :    Prevent from running on Windows.        ** TEMPORARY **
    if ( sys.platform.startswith('win') ):
        raise NotImplementedError(textwrap.dedent("""**TEMPORARY ERROR**
        I am developing on a Macintosh.  The ANSI Escape-Codes that I have used to
        format output to the command line (bold, underlined, or colorized text, etc)
        may not work on a Windows machine.  
        We can use the \"colorama\" package for cross-platform functionality here."""))
        
    
    UTL.system_info()
    #UTL.manual()
    sys.exit( main() )






###############################################################################
###############################################################################
#   END.
