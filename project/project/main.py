###############################################################################
#
#       ************************************************************
#       ****            M A I N . P Y  ____  F I L E.           ****
#       ************************************************************
#
#
#     AUTHORS:      GROUP #6:
#                   Hemu Babis,         Elizabeth Barnett,
#                   Michael Bell,       Collin Bond,
#                   Daniel Huynh,       Q Ntsasa.
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
import os, sys, signal, traceback

    
    
#   "main"
#
def main() -> int:
    status = 0
    signal.signal(signal.SIGINT, UTL.signal_handler)
    
    print(f"{ANSI.MAGENTA}Invoking 'main()'...  Press Ctrl+C to interrupt.\n" + '#'*70 + f"{ANSI.RESET}\n")
    
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
        print(f"\n{ANSI.MAGENTA}" + '#'*70)
        
        if (status==0):
            print("Successful program termination" + f" {ANSI.GREEN}(exit status \"{status}\").",end="")
        else:
            print("Unuccessful program termination" + f" {ANSI.RED}(exit status \"{status}\").",end="")
        print(f"{ANSI.RESET}")
    
    return status


    
###############################################################################

#   Hook for the "main" function...
#
if (__name__ == '__main__'):
    sys.exit( main() )






###############################################################################
###############################################################################
#   END.
