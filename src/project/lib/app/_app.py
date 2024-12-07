###############################################################################
#
#       ************************************************************
#       ****            _ A P P . P Y  ____  F I L E.           ****
#       ************************************************************
#
#
###############################################################################
from dataclasses import dataclass, field
import numpy as np
from lib.utility import Cstring
from lib.utility.constants import _LW, _PROMPTS, _COMMANDS, _INIT_UI, _UI, _GENERAL
from lib.utility.constants import Permissions, MEMBER, PROVIDER, ADMINISTRATOR, ROOT
from lib.utility import ANSI
import lib.utility as UTL
from lib.users import Member, Provider, find_member_by_attributes, find_provider_by_attributes
from lib.services import Service
from lib.app.ui import Popup
from lib.app.ui import draw_window, draw_panel, set_title, print_scr, _not_implemented, quit, spell_check


import json, sys, signal, traceback, time, textwrap, difflib, math, copy
from PIL import Image
import curses
from curses import panel
import curses.textpad as tp




#   UTILITY FUNCTIONS...
###############################################################################
###############################################################################
    
#   "_assign_commands"
#
def _assign_commands(self):
    textwrap.dedent(f"""A helper function that assigns a \"function-pointer\" to each command that the application
    recognizes.  We need to do this here instead of inside the \"lib/utility/constants/_constants.py\" file 
    because certain actions depend on private/local functions that are defined only inside THIS file and
    should not be imported to other modules.""")

    #   1.  OPERATION COMMANDS...
    #
    #       1.1.    MEMBER COMMANDS...
    self.commands["add member"]["action"]           = add_member
    self.commands["edit member"]["action"]          = _not_implemented
    self.commands["remove member"]["action"]        = _not_implemented
    self.commands["display members"]["action"]      = display_members
    #
    #       1.2.    PROVIDER COMMANDS...
    self.commands["add provider"]["action"]         = _not_implemented
    self.commands["edit provider"]["action"]        = _not_implemented
    self.commands["remove provider"]["action"]      = _not_implemented
    self.commands["display providers"]["action"]    = display_providers
    #
    #       1.3.    SERVICE COMMANDS...
    self.commands["add service"]["action"]          = _not_implemented
    self.commands["edit service"]["action"]         = _not_implemented
    self.commands["remove service"]["action"]       = _not_implemented
    self.commands["display services"]["action"]     = _not_implemented
    
    
    #   2.  UTILITY COMMANDS...
    self.commands["test"]["action"]                 = test
    self.commands["add service"]["action"]          = _not_implemented
    
    
    self.command_keys                               = list( self.commands.keys() )
    return
    
    
###############################################################################
###############################################################################
    

#   "test"
#
def test(self, stdscr):
    test_panel(self, stdscr)
    return
    
    
    
#   "test_panel"
#
def test_panel(self, stdscr):
    sw  = {
        'show'              : False,
        'focus'             : False,
        'instructions'      : False,
        'title'             : False,
        'edit'              : False,
    }
    
    pop_up  = self.popups["member"]
    #pop_up.edit()
 
    
 
    while True:
        key = stdscr.getch()
        
        #   1.  SHOW/HIDE
        if (key == ord('s')):
            if (sw['show']):
                self.popups["member"].hide()
                sw['show']          = False
            else:
                self.popups["member"].show()
                sw['show']          = True
        #
        #   2.  FOCUS/UNFOCUS.
        if (key == ord('f')):
            if (sw['focus']):
                self.popups["member"].unfocus()
                sw['focus'] = False
            else:
                self.popups["member"].focus()
                sw['focus']         = True
                sw['show']          = True
                sw['instructions']  = True
        #
        #   3.  INSTRUCTIONS.
        if (key == ord('i')):
            if (sw['instructions']):
                self.popups["member"]._hide_instructions()
                self.popups["member"].win.refresh()
                sw['instructions']  = False
            else:
                self.popups["member"]._show_instructions()
                self.popups["member"].win.refresh()
                sw['instructions']  = True
        #
        #   4.  TITLE.
        if (key == ord('t')):
            if (sw['title']):
                self.popups["member"].set_title("Title #1")
                sw['title']         = False
            else:
                self.popups["member"].set_title("Title #2")
                sw['title']         = True
        #
        #   5.  EDIT.
        if (key == ord('e')):
            try:
                sw['focus']         = True
                sw['show']          = True
                sw['instructions']  = True
                self.popups["member"].edit()
            except KeyboardInterrupt as e:
                sw['focus']         = False
        #
        #   6.  LOADING VALUES.
        if (key == ord('l')):
            sw['focus']         = True
            sw['show']          = True
            sw['instructions']  = True
            values = ["Collin Bond", "120446007", "2371 SE Dove St", "Portland", "OR", "97009"]
            self.popups["member"].load(values)
            self.popups["member"].focus()
        #
        #   7.  GETTING VALUES.
        if (key == ord('g')):
            sw['focus']         = False
            sw['show']          = False
            gather  = self.popups["member"].gather()
            data    = ''
            for item in gather:
                data += f"'{item}', "
                
            printw(self, data)
            self.popups["member"].hide()
        #
        #
        elif key == curses.KEY_ENTER:
            break
    
    
    stdscr.getch()
    pop_up.clear()
    
    
    #   5.  REFRESH ALL, WAIT FOR KEY, ETC...
    stdscr.getch()
    self.UI['out']['win'].refresh()
    self.UI['in']['win'].refresh()
    return
    

###############################################################################
###############################################################################






#   1.  "APPLICATION" CLASS FUNCTIONS...
###############################################################################
###############################################################################
#
#
#
#
#
#
#       1.1  INITIALIZATION / BUILT-IN METHODS...
###############################################################################
###############################################################################

#   "__post_init__"
#
def __post_init__(self):
    self.files  = _GENERAL['files']
    with open(self.files['backup'], 'w') as file:   #   Open file in 'w'-mode (CLEARS THE FILE).
        pass
    
    #   1.  TRY-BLOCK...
    try:
        #   1.1.    Loading User Data (Members and Providers)...
        load_info_1     = load_users(self, self.files['all'])
        #load_info_2     = load_users(self, self.files['providers'])
    #
    #
    #   2.  CATCH-BLOCK...
    except ValueError as e:             #   2.1.    Could not get position of the terminal cursor.
        UTL.log("CAUGHT A \"VALUE ERROR\" EXCEPTION.",type=ANSI.ERROR)
        UTL.log(f"{e}",color=False)
        raise(e)
    #
    except FileNotFoundError as e:      #   2.2.    Could not open the external data file.
        UTL.log("CAUGHT A \"FILE NOT FOUND\" EXCEPTION.",type=ANSI.ERROR)
        UTL.log(f"{e}",color=False)
        raise(e)
    #
    except ValueError as e:             #   2.3.    Unknown IOError occured.
        UTL.log("CAUGHT AN \"IOERROR\" EXCEPTION.",type=ANSI.ERROR)
        UTL.log(f"{e}",color=False)
        raise(e)
    #
    #
    #   3.  FINALLY-BLOCK...
    finally:
        if (load_info_1[0] < 1):
            raise IOError(_PROMPTS['bad_load'].format(a=self.files['all']))
            
        UTL.log(f"Loaded {load_info_1[0]} total items from file \"{self.files['members']}\": {load_info_1[1]} Members and {load_info_1[2]} Providers.")
        
        
        #   3.1.    Initializing Prompts.
        self.prompts    = _PROMPTS
        
        #   3.2.    Initializing Commands (Assign the function 'pointers').
        self.commands   = _COMMANDS
        _assign_commands(self)
        
        #   3.3.    Initializing UI Dimensions.
        self.UI['head']     = _INIT_UI['head']
        self.UI['out']      = _INIT_UI['out']
        self.UI['in']       = _INIT_UI['in']
    
    return


#   "setup_UI"
#
def setup_UI(self):
    stdscr = self.stdscr
    
    #   0.  INITIALIZE ELEMENTS OF UI...
    #       0.1.    Colors.
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE,     curses.COLOR_BLACK)         #   Normal Text.
    curses.init_pair(2, curses.COLOR_GREEN,     curses.COLOR_BLACK)         #   Output Text.
    curses.init_pair(3, curses.COLOR_RED,       curses.COLOR_BLACK)         #   Input Text.
    curses.init_pair(4, curses.COLOR_BLACK,     curses.COLOR_WHITE)         #   HEADER TEXT...
    #
    #       0.2.    Initial Commands.
    stdscr.clear()                                                          #   Clear the screen
    #
    #       0.3.    Initial Values.
    #curses.curs_set(0)                                                     #   ANSI.HIDE
    curses.noecho()                                                         #   Disable real-time printing of input to screen.
    _H, _W                      = stdscr.getmaxyx()                         #   Screen Dimensions.
    _SCALE                      = 3
    _RATIO                      = (5, 4)
    if (_SCALE is not None):
        _W = ( (_SCALE * _W) // _RATIO[0])
        _H = ( (_SCALE * _H) // _RATIO[1])
    
    h = _H-3; w = _W-4;
    height                      = h
    width                       = w
    self.UI['global']           = { 'height':height, 'width':width }
    self.UI['head']['height']   = h
    self.UI['head']['width']    = w
    self.UI['hl_fmt']           = curses.color_pair(4)
    self.UI['hlbf_fmt']         = curses.color_pair(4)|curses.A_BOLD
    
    self.UI['in']['width']      = width-6
    self.UI['out']['width']     = width-6
    
    
    #   2.  CREATE WINDOW FOR EACH SECTION OF PROGRAM...
    #
    #       2.1.    Header Window.
    pos                     = (self.UI['head']['pos'][0], self.UI['in']['pos'][1])
    dims                    = (self.UI['head']['height'], self.UI['in']['width'])
    title                   = self.UI['head']['title']
    head_win, head_box      = draw_window( stdscr, (h, w), pos, subwindow=True, text=title,
                                           title_color=curses.color_pair(1) )
    #
    #
    #       2.2.    Program-Output Window.
    pos                     = (self.UI['out']['pos'][0], self.UI['in']['pos'][1])
    dims                    = (self.UI['out']['height'], self.UI['in']['width'])
    title                   = self.UI['out']['title']
    output_win, output_box  = draw_window( stdscr, dims, pos, text=title,
                                           title_color=curses.color_pair(2)|curses.A_BOLD )
    output_tbox             = tp.Textbox(output_win)
    #
    #
    #       2.3.    User-Input Window.
    pos                     = (self.UI['in']['pos'][0], self.UI['in']['pos'][1])
    dims                    = (self.UI['in']['height'], self.UI['in']['width'])
    title                   = self.UI['in']['title']
    input_win, input_box    = draw_window( stdscr, dims, pos, text=title,
                                           title_color=curses.color_pair(3)|curses.A_BOLD )
    input_tbox              = tp.Textbox(input_win)
    
    
    #   3.  ASSIGNING EACH WINDOW TO DICTIONARY...
    self.UI['head']['win']      = head_win
    self.UI['head']['box']      = head_box
    
    self.UI['in']['win']        = input_win
    self.UI['in']['box']        = input_box
    self.UI['in']['tbox']       = input_tbox
    
    self.UI['out']['win']       = output_win
    self.UI['out']['box']       = output_box
    self.UI['out']['tbox']      = output_tbox
    
    
    curses.curs_set(0)
    stdscr.refresh()
    self.UI['head']['win'].refresh()
    self.UI['out']['win'].refresh()
    self.UI['in']['win'].refresh()
    self.UI['in']['win'].clear()
    
    
    setup_popup_windows(self)
    update_login_status(self)
    return
    
    
#   "update_login_status"
#
def update_login_status(self):
    window      = self.UI['in']
    win         = window['win']
    y,    x     = win.getbegyx()
    ymax, xmax  = win.getmaxyx()
    info        = ''
    
    if (self.permission is None):
        info = f" [{self.prompts['login_status-out']}]{' '*_UI['title_padding']}"
    else:
        if (self.permission     == ADMINISTRATOR):  status = "Administrator"
        elif (self.permission   == MEMBER):         status = "Member"
        elif (self.permission   == PROVIDER):       status = "Provider"
        elif (self.permission   == ROOT):           status = "ROOT"
        else:                                       status = "???"
        info = ' [' + self.prompts['login_status'].format(a=status) + f"]{' '*_UI['title_padding']}"
    
    W           = len(info)
    pos         = ( x+_UI['title_offset'] + len(window['title']), y+ymax-2)
    self.stdscr.addstr(pos[1], pos[0], ' '*W, curses.color_pair(3))
    self.stdscr.addstr(pos[1], pos[0], info, curses.color_pair(3))
    self.stdscr.refresh()
    return
    
    
#   "setup_popup_windows"
#
def setup_popup_windows(self):
    stdscr      = self.stdscr
    h, w        = self.UI['out']['win'].getmaxyx()
    y, x        = self.UI['out']['win'].getbegyx()
    
    #   1.  CREATE POP-UP WINDOW RELATIVE TO "OUTPUT" WINDOW...
    pos_s       = (1, 10)                   #   Offset of the Pop-Up Win. POS from the OUTPUT Win. POS.
    #dim_s       = ( -3, -80 )               #   Offset of the Pop-Up Win. DIM from the OUTPUT Win. DIM.
    #dims        = ( h+dim_s[0], w+dim_s[1]  )
    pos_m       = ( y+pos_s[0], x+pos_s[1]  )
    pos_p       = ( y+pos_s[0], x+pos_s[1]+10  )
    dims        = (25, 50)
    
    
    #       2.1.    CREATING "MEMBER" POP-UP WINDOW...
    m_fields                    = [ "MEMBER NAME", "ID", "ADDRESS", "CITY", "STATE", "ZIP" ]
    p_fields                    = [ "PROVIDER NAME", "ID", "ADDRESS", "CITY", "STATE", "ZIP" ]
    self.popups['member']       = Popup(stdscr=self.stdscr, name="MEMBER", dims=dims, pos=pos_m, fields=m_fields)
    self.popups['provider']     = Popup(stdscr=self.stdscr, name="PROVIDER", dims=dims, pos=pos_p, fields=p_fields)
    
    
    panel.update_panels()
    curses.doupdate()
    return


###############################################################################
#
#
#
#
#
#
#       1.2  UTILITY / HELPER FUNCTIONS...
###############################################################################
###############################################################################
    
#   "load_users"
#
def load_users(self, file_path:str) -> tuple:
    idx     = 0
    m_idx   = 0
    p_idx   = 0
    
    with open(file_path, 'r') as file:
        data = json.load(file)

    for item in data:
        #   CASE 1 :    Loaded a "Member" from the file.
        if (item["type"] == "Member"):
            #           1.1.    Load the main fields of the member.
            user = Member(
                name=item["name"],      id=item["id"],          address=item["address"],
                city=item["city"],      state=item["state"],    zip=item["zip"],
            )
            #           1.2.    Load the historical records of the member.
            for record in item.get("history", []):
                user.history.append( Service(name=record["name"],           id=record["id"],
                                     provider_name=record["provider_name"], provider_id=record["provider_id"],
                                     patient_name=record["patient_name"],   patient_id=record["patient_id"],
                                     dos=record["dos"],                     dor=record["dor"],
                                     comments=record["comments"],           fee=record["fee"]) )
                
            self.members.append(user)
            idx     += 1
            m_idx   += 1
        #
        #   CASE 2 :    Loaded a "Provider" from the file.
        elif (item["type"] == "Provider"):
            user = Provider(
                name    =item["name"],
                id      =item["id"],
                address =item["address"],
                city    =item["city"],
                state   =item["state"],
                zip     =item["zip"],
            )
            #           2.2.    Load the historical records of the provider.
            for record in item.get("history", []):
                user.history.append( Service(name=record["name"],           id=record["id"],
                                     provider_name=record["provider_name"], provider_id=record["provider_id"],
                                     patient_name=record["patient_name"],   patient_id=record["patient_id"],
                                     dos=record["dos"],                     dor=record["dor"],
                                     comments=record["comments"],           fee=record["fee"]) )
            self.providers.append(user)
            idx     += 1
            p_idx   += 1
        #
        #   CASE 3 :    Loaded a "Provider" from the file.
        else:
            UTL.log("Error while loading user-data from \"{file}\": data at entry \"{idx}\" has an unsupported type.", ANSI.WARN)
            idx += 1
            
    return (idx, m_idx, p_idx)
    
    
    
#   "write_data"
#
def write_data(self, filename:str) -> None:
    data = [member.to_dict() for member in self.members] + \
           [provider.to_dict() for provider in self.providers]

    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
            
    except IOError as e:
        UTL.log(f"ERROR.  Could not save user data to {filename}.\n{e}", ANSI.ERROR)
        
    return
    
###############################################################################
#
#
#
#
#
#
#       1.3.  MAIN FUNCTIONS...
###############################################################################
###############################################################################


#   "signal_handler"
#
def signal_handler(self, sig, frame):
    self.write()

    self.UI['in']['win'].clear()
    printw(self, self.prompts['ctrl-c_exit'], clear=True)
    self.UI['in']['win'].refresh()
    self.stdscr.refresh()
    
    time.sleep(3)
    
    return
    
    
  
#   "quit"
#
def quit(self):
    raise SystemExit("normal exit")
    return
    
    
    
#   "_exit"
#
def _exit(self):
    self.write()

    self.UI['in']['win'].clear()
    printw(self, self.prompts['normal_exit'], clear=True)
    self.UI['in']['win'].refresh()
    self.stdscr.refresh()
    
    time.sleep(3)
    return
    
    
    
#   "write"
#
def write(self):
    write_data(self, self.files['all'])
    write_data(self, self.files['backup'])
    return



#   "run"
#
def run(self) -> int:
    status = 0
    signal.signal( signal.SIGINT, lambda sig, frame: signal_handler(self, sig, frame) )
    
    #   1.  TRY-BLOCK...
    try:
        curses.wrapper(self.main)
    #
    #   2.  EXCEPTION-CATCHING BLOCKS...
    except KeyboardInterrupt as e:
        UTL.log(f"Caught CTRL-C Keyboard Interuption.  Exiting...")
        UTL.log(f"{e}", color=False)
        
    except SystemExit as e:
        
        status = 0
        
    except Exception as e:
        UTL.log("FALLBACK EXCEPTION CASE.  An unspecified exception has been thrown.",type=ANSI.ERROR)
        UTL.log(f"{e}", color=False)
        traceback.print_exc()
        status = 1
    #
    #   3.  FINALLY...
    finally:
        pass
    
    return status

    
    
#   "logout"
#
def logout(self):
    self.permission = None
    update_login_status(self)
    return
    


#   "login"
#
def login(self):
    stdscr      = self.stdscr
    run         = True

    printw(self, self.prompts['welcome_1'], color=curses.color_pair(2)|curses.A_STANDOUT, at=ANSI.TOP)
    printw(self, '\n' + self.prompts['welcome_2'])
    
    #   2.  GET THE LOG-IN INFORMATION FROM THE CLIENT...
    while(run):
        #   1.1.    FETCH INPUT FROM USER...
        input = get_input(self, stdscr)
        
        #   CASE 1 :    SIGN-IN AS ADMIN...
        if (input == "ADMIN" or input == "admin"):
            self.permission = ADMINISTRATOR
            printw(self, self.prompts['login_success'].format( a=f"ADMINISTRATOR", b='', c=''), clear=True )
            run = False
        #
        #
        #   CASE 2 :    SIGN-IN AS EITHER "MEMBER" OR "PROVIDER"...
        else:
            my_member   = find_member_by_attributes(self.members, id=input)
            my_provider = find_provider_by_attributes(self.providers, id=input)
            
            #   2.1.    MEMBER...
            if (my_member is not None):
                self.permission = MEMBER
                printw(self, self.prompts['login_success'].format( a=f"MEMBER", b=f" with ID# {input}",c=f", {my_member.name}" ), clear=True )
                run = False
            
            #   2.2.    SIGN-IN AS PROVIDER...
            elif (my_provider is not None):
                self.permission = PROVIDER
                printw(self, self.prompts['login_success'].format( a=f"MEMBER", b=f" with ID# {input}",c=f", {my_member.name}" ), clear=True )
                run = False
            #
            #   CASE 3 :    INVALID LOG-IN INFORMATION...
            else:
                printw(self, '\n' + self.prompts['login_unknown'].format(a=input), at=ANSI.BOTTOM)
        
    return
    
    
    
#   "main"
#
def main(self, stdscr):
    run         = True
    self.stdscr = stdscr
    
    
    setup_UI(self)
    login(self)
    update_login_status(self)
    
    
    #   MAIN PROGRAM LOOP...
    while(run):
        #   1.0.    FETCH INPUT FROM USER...
        printw(self, self.prompts['cmd_greeting'])
        input = get_input(self, stdscr).lower()
        printw(self, '', clear=True)
        
        #   CASE 1 :    RECOGNIZED COMMAND...
        if (input in self.commands):
            task = self.commands[input]
            printw(self, f"I recognize the command \"{input}\":\n{task['reply']}\n", clear=True)
            
            #   1.1.    Check if user has permissions for this command.
            if ( (self.permission == ADMINISTRATOR) or
                 ('accessors' in task and (self.permission in task['accessors'])) ):
    
                #   1.1A.    Invoking the action for this command (if it exists).
                if ('action' in task):
                    try:                                    #   TRY-BLOCK...
                        task['action'](self, stdscr)
                    #
                    #
                    except NotImplementedError as e:        #   CATCH-BLOCK...
                        printw( self, self.prompts['not_impl'].format(a=UTL.truncate(input, 24)), color=curses.COLOR_RED)
                    #
                    #
                    finally:                                #   FINALLY...
                        pass
            #
            #   1.1B.   User DOES NOT have permissions.
            else:
                printw(self, self.prompts['no_access'].format(a=UTL.truncate(input, 24)), color=curses.COLOR_RED)
        #
        #
        #   CASE 2 :    UNRECOGNIZED / UNKNOWN COMMAND...
        else:
            matches     = 1 + sum(1 for word in _GENERAL['word_bank'] if word in input)
            suggestions = self.spell_check(input, n=matches)
            
            printw(self, self.prompts['cmd_unknown'].format(a=UTL.truncate(input, 24)), color=curses.COLOR_RED)
            if (suggestions):
                N       = len(suggestions)
                temp    = ''
                
                if (N > 1):
                    for i in range(0, N):
                        temp += f"\"{suggestions[i]}\", " if (i != N-1) else f"or \"{suggestions[i]}\""
                else:
                    temp = f"\"{suggestions[0]}\""
                    
                    
                suggestions_fmt = "\n" + self.prompts['cmd_suggestion'].format(a=UTL.truncate(temp, 45) )
                printw(self, suggestions_fmt)
            #
            else:
                printw(self, "\n")
            
    #   2.  RESET THE INPUT BOX AND DISPLAY ON OUTPUT CONSOLE...
    self.UI['out']['win'].clear()
    self.UI['in']['win'].clear()
    self.UI['out']['win'].addstr(0, 0, input, curses.color_pair(2))
    
    #   3.  REFRESH THE SCREEN...
    self.UI['out']['win'].refresh()
    self.UI['in']['win'].refresh()
    self.stdscr.refresh()

    #   5.  WAIT FOR ENTER-KEY BEFORE CLOSING...
    return
    
    
    
#   "add_member"
#
def add_member(self, stdscr):
    run     = True
    popup   = self.popups["member"]
    popup.focus()
    
    while (run):
        try:
            popup.edit()
            
        #   1.2.    Catch exception if user pressses ESC-Key.
        except KeyboardInterrupt as e:
            popup.clear()
            printw(self, self.prompts['cancel_operation'], clear=True)
            run = False
            
        #   1.3.    If NO EXCEPTION.
        else:
            data        = popup.gather()
            new_member  = Member(name=data[0],   id=data[1],     address=data[2],
                                 city=data[3],   state=data[4],  zip=data[5])
                      
            popup.hide()
            printw(self, self.prompts['verify_input'], color=curses.color_pair(1), clear=True)
            printw(self, f"{new_member}")
            input = get_input(self, stdscr).lower()
            
            if (input == 'y'):          #   "Anything other than a 'yes' is NO" - John Mayer
                self.members.append(new_member)
                printw(self, self.prompts['operation_success'].format(a="added", b=" the member", c=" to our database"),
                             color=curses.color_pair(1), clear=True)
                run = False
            else:
                popup.focus()
                run = True
    
    
    popup.clear()
    popup.hide()
    return
        

###############################################################################
###############################################################################
#
#
#
#
#
#
#       1.3.  UTILITY / HELPER FUNCTIONS...
###############################################################################
###############################################################################

#   "display_members"
#
def display_members(self, stdscr):
    N1          = len(self.members)
    N2          = 0
    x           = 0
    y           = 0
    capturing   = True
    curses.curs_set(0)

    #   "get_entry"
    def get_entry(x:int, y:int, N0:int=N1) -> tuple:
        N       = len( self.members[x].history )
        head_1  = f"PATIENT #{x+1} OF {N0}:"
        body_1  = f"{self.members[x]}"
        head_2  = f"RECORD #{y+1} OF {N}:" if (N > 0) else f"NO RECORD OF PRIOR HEALTHCARE SERVICE"
        body_2  = f"{self.members[x].history[y]}" if (N > 0) else ''
        
        return ( (head_1, body_1), (head_2, body_2) )
    
    #   "display_entry"
    def display_entry(x:int, y:int) -> None:
        entry = get_entry(x, y)
        self.UI['out']['win'].clear()
        
        self.UI['out']['win'].addstr(0, 0, entry[0][0], curses.color_pair(2)|curses.A_STANDOUT)
        self.UI['out']['win'].addstr(1, 0, entry[0][1], curses.color_pair(2))
        self.UI['out']['win'].addstr(3, 0, entry[1][0], curses.color_pair(2)|curses.A_STANDOUT)
        self.UI['out']['win'].addstr(4, 0, entry[1][1], curses.color_pair(2))
        
        self.UI['out']['win'].refresh()
        return
    
    
    #   0.  CONFIGURE TERMINAL FOR REAL-TIME INPUT...
    curses.cbreak()  # Alternatively: curses.raw()
    curses.noecho()
    stdscr.keypad(True)  # Enable special key handling like arrows
    
    #   CASE 1 :    NO DATA TO DISPLAY...
    if (N1 == 0):
        raise ValueError("No data on record to display.")

    #   1.  CLEAR INPUT/OUTPUT SCREENS, FETCH INITIAL ENTRY, AND DISPLAY INSTRUCTIONS...
    self.UI['in']['win'].clear()
    self.UI['in']['win'].addstr(0, 0, self.prompts['display_mode_ON'], curses.color_pair(3)|curses.A_STANDOUT)
    self.UI['in']['win'].refresh()
    display_entry(x, y)

    #   2.  MAIN, REAL-TIME INPUT LOOP...
    while (capturing):
        key = stdscr.getch()
    
        #   2.1.    GET THE USER'S KEY-INPUT.
        if (key == ord('q')):
            capturing = False
        #
        elif (key == curses.KEY_LEFT):
            x   = (x-1)%N1
            y   = 0
            N2  = len(self.members[x].history)
        #
        elif (key == curses.KEY_RIGHT):
            x   = (x+1)%N1
            y   = 0
            N2  = len(self.members[x].history)
        #
        elif (key == curses.KEY_UP):
            y = (y+1)%N2 if (N2 > 0) else 0
        #
        elif (key == curses.KEY_DOWN):
            y = (y-1)%N2 if (N2 > 0) else 0

        #   2.2.    Fetch and Display the selected entry.
        display_entry(x, y)
        
    #   3.  CLEANING THE SCREEN.  DISPLAYING EXIT MESSAGE...
    self.UI['in']['win'].clear()
    self.UI['out']['win'].clear()
    self.UI['in']['win'].addstr(0, 0, self.prompts['display_mode_OFF'], curses.color_pair(3)|curses.A_STANDOUT)
    self.UI['out']['win'].refresh()
    self.UI['in']['win'].refresh()
    return
    


#   "display_providers"
#
def display_providers(self, stdscr):
    N1          = len(self.providers)
    N2          = 0
    x           = 0
    y           = 0
    capturing   = True
    curses.curs_set(0)

    #   "get_entry"
    def get_entry(x:int, y:int, N0:int=N1) -> tuple:
        N       = len( self.providers[x].history )
        head_1  = f"PROVIDER #{x+1} OF {N0}:"
        body_1  = f"{self.providers[x]}"
        head_2  = f"RECORD #{y+1} OF {N}:" if (N > 0) else f"NO RECORDS OF PRIOR HEALTHCARE SERVICE"
        body_2  = f"{self.providers[x].history[y]}" if (N > 0) else ''
        return ( (head_1, body_1), (head_2, body_2) )
    
    #   "display_entry"
    def display_entry(x:int, y:int) -> None:
        entry = get_entry(x, y)
        self.UI['out']['win'].clear()
        
        self.UI['out']['win'].addstr(0, 0, entry[0][0], curses.color_pair(2)|curses.A_STANDOUT)
        self.UI['out']['win'].addstr(1, 0, entry[0][1], curses.color_pair(2))
        self.UI['out']['win'].addstr(3, 0, entry[1][0], curses.color_pair(2)|curses.A_STANDOUT)
        self.UI['out']['win'].addstr(4, 0, entry[1][1], curses.color_pair(2))
        
        self.UI['out']['win'].refresh()
        return
    
    
    #   0.  CONFIGURE TERMINAL FOR REAL-TIME INPUT...
    curses.cbreak()  # Alternatively: curses.raw()
    curses.noecho()
    stdscr.keypad(True)  # Enable special key handling like arrows
    
    #   CASE 1 :    NO DATA TO DISPLAY...
    if (N1 == 0):
        raise ValueError("No data on record to display.")

    #   1.  CLEAR INPUT/OUTPUT SCREENS, FETCH INITIAL ENTRY, AND DISPLAY INSTRUCTIONS...
    self.UI['in']['win'].clear()
    self.UI['in']['win'].addstr(0, 0, self.prompts['display_mode_ON'], curses.color_pair(3)|curses.A_STANDOUT)
    self.UI['in']['win'].refresh()
    display_entry(x, y)

    #   2.  MAIN, REAL-TIME INPUT LOOP...
    while (capturing):
        key = stdscr.getch()
    
        #   2.1.    GET THE USER'S KEY-INPUT.
        if (key == ord('q')):
            capturing = False
        #
        elif (key == curses.KEY_LEFT):
            x   = (x-1)%N1
            y   = 0
            N2  = len(self.providers[x].history)
        #
        elif (key == curses.KEY_RIGHT):
            x   = (x+1)%N1
            y   = 0
            N2  = len(self.providers[x].history)
        #
        elif (key == curses.KEY_UP):
            y = (y+1)%N2 if (N2 > 0) else 0
        #
        elif (key == curses.KEY_DOWN):
            y = (y-1)%N2 if (N2 > 0) else 0

        #   2.2.    Fetch and Display the selected entry.
        display_entry(x, y)
        
    #   3.  CLEANING THE SCREEN.  DISPLAYING EXIT MESSAGE...
    self.UI['in']['win'].clear()
    self.UI['out']['win'].clear()
    self.UI['in']['win'].addstr(0, 0, self.prompts['display_mode_OFF'], curses.color_pair(3)|curses.A_STANDOUT)
    self.UI['out']['win'].refresh()
    self.UI['in']['win'].refresh()
    return
    
    

#   "get_input"
#
def get_input(self, stdscr) -> str:
    window      = self.UI['in']
    win         = window['win']
    box         = window['tbox']
    ymax, xmax  = win.getmaxyx()
    capture     = True
    
    win.clear()
    win.move(0, 0)
    win.refresh()
    curses.curs_set(1)

    #   1.  ALLOW USER TO PROVIDE INPUT...
    while (capture):
        key     = box.win.getch()
        y, x    = box.win.getyx()

        #   CASE 1 :    "ENTER"
        if ( (key == curses.KEY_ENTER) or (key == 10) or (key == 13) ):
            capture = False
        #
        #   CASE 2 :    "BACKSPACE"
        elif key in (curses.KEY_BACKSPACE, 127):

            if ( (x==0) and (0 < y) ):#     2.1.    Delete at the beginning of a line (skip up to previous line).
                box.win.move(y-1, xmax)
                box.win.delch(y-1, xmax)
                
            elif (0 < x):#                  2.2.    Delete in the middle of the line.
                box.win.delch(y, x-1)
        #
        #   CASE 3 :    "NORMAL CHARACTER"
        else:
            if ( (not (y < ymax)) and (not (x < xmax)) ):#    3.2.    At the end of input text-box.
                pass
            else:#                                      3.1.    Adding character normally.
                box.win.addch(key)
                

    #   2.  FETCHING USER'S INPUT...
    response = box.gather()

    #   3.  RESET THE INPUT BOX...
    curses.curs_set(0)
    win.clear()
    win.refresh()

    return response.rstrip()
    
 
 
#   "set_output"
#
def set_output(self, text:str, pos:tuple=None, clear:bool=False, attribute=None) -> None:
    pos = (0,0) if (pos is None) else pos
    
    if (clear):
        self.UI['out']['win'].clear()
    
    if (attribute is None):
        self.UI['out']['win'].addstr(pos[0], pos[1], text, curses.color_pair(2))
    else:
        self.UI['out']['win'].addstr(pos[0], pos[1], text, curses.color_pair(2)|attribute)
        
    self.UI['out']['win'].refresh()
    return
    
 
 
#   "printw"            Like "printf" but for "print-to-window"...
#
def printw(self, text:str, win=None, clear:bool=False, color=None, attribute=None, at:ANSI.Pos_Tag=None) -> None:
    if (win is None):               win = self.UI['out']['win'] if (win is None) else win;
    if (clear):
        win.clear();
        win.move(0,0)
        
    if (color is None):             color = curses.color_pair(2);
    if (attribute is not None):     color = color|attribute;
    
    if (at is not None):
        return _printw(self, text, win, color, at)

    y, x    = win.getyx()
    win.addstr(y, x, text, color)
    win.refresh()
    return
    
    
#   "_printw"
#
def _printw(self, text:str, win, color, at:ANSI.Pos_Tag) -> None:
    y0,   x0    = win.getyx()
    y,    x     = win.getyx()
    ymax, xmax  = win.getmaxyx()
    L           = len(text)
    N           = math.floor( L / xmax ) + text.count('\n')
    
    if (at == ANSI.CRETURN):                    #   1.  Print BEGINNING of current-line (Carriage Return).
        win.addstr(y, 0, ' '*(xmax-1), curses.color_pair(1))
        win.move(y, 0)
        y, x = win.getyx()
    
    elif (at == ANSI.TOP):                      #   2.  Print at TOP of window.
        for i in range(0, N):
            win.addstr(0 + i, 0, ' '*(xmax-1), color)
        win.move(0, 0)
        y, x = win.getyx()
    
    elif (at == ANSI.BOTTOM):                   #   3.  Print at BOTTOM of window.
        yi  = ymax-N-1
        for i in range(0, N):
            win.addstr(yi + i, 0, ' '*(xmax-1), curses.color_pair(1))

        win.addstr(yi, 0, text, color)
        win.refresh()
        return
    
    
    win.addstr(y, x, text, color)
    win.refresh()
    return
    
    
###############################################################################
###############################################################################
#
#
#
###############################################################################
###############################################################################
#   END OF "APPLICATION" CLASS...
    





###############################################################################
###############################################################################
#   END.
