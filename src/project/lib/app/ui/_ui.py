###############################################################################
#
#                        "A_P_P"        M O D U L E.
#
#   "U_S_E_R__I_N_T_E_R_F_A_C_E"        S U B - M O D U L E.
#
#
#                          File:        "_ui.py".
#
###############################################################################
from dataclasses import dataclass, field
from lib.utility.constants import _LW, _PROMPTS, _COMMANDS, _UI
from lib.utility import ANSI
import lib.utility as UTL
from lib.users import Member, Provider
from lib.services import Service

import math, json, sys, time, traceback, textwrap, difflib
from PIL import Image
import curses
from curses import panel
import curses.textpad as tp






#   1.  FREESTANDING FUNCTIONS...
###############################################################################
###############################################################################
#
#
#
#
#
#
#       1.1.    DRAWING FUNCTIONS...
###############################################################################

#   "draw_window"
#
def draw_window(stdscr, dims:tuple, pos:tuple, text:str='', subwindow:bool=False, title_color=_UI['fg'],
                title_offset:int=_UI['title_offset'], title_padding:int=_UI['title_padding'], show_title:bool=True):
    h, w    = dims
    y, x    = pos
    
    if (h > 1):
        window  = stdscr.subwin(h, w,  y+1, x+1) if (subwindow) else curses.newwin(h, w,  y+1, x+1)
        box     = tp.rectangle(stdscr, y, x, 1+h+y, 1+w+1+x )
    else:
        window  = stdscr.subwin(h, w,  y+1, x+1) if (subwindow) else curses.newwin(1, w,  y+1, x+1)
        box     = tp.rectangle(stdscr, y, x, 1+y+1, 1+w+1+x )
    
    if (show_title):
        stdscr.addstr(y, x+title_offset, f"{' '*title_padding}{text}{' '*title_padding}", title_color)
  
    return (window, box)
    


#   "draw_panel"
#
def draw_panel(dims:tuple, pos:tuple, title:str=None,   title_color=_UI['fg'],
                title_offset:int=_UI['title_offset'],   title_padding:int=_UI['title_padding'],
                show_title:bool=True,                   box:bool=True, ):
    h, w    = dims
    y, x    = pos
    window  = curses.newwin(h, w,  y+1, x+1)
        
    window.clear()
    if (box):     window.box()
    
    if (title is not None):
        window.addstr(0, title_padding+1, f"{' '*title_padding}{title}{' '*title_padding}", title_color)
        
    return window
    

#   "set_title"
#
def set_title(win, text:str, title_color=_UI['fg'],
              title_offset:int=_UI['title_offset'], title_padding:int=_UI['title_padding']):
              
    y, x    = win.getbegyx()
    h, w    = win.getmaxyx()
    stdscr.addstr(x, y+title_offset, f"{' '*title_padding}{text}{' '*title_padding}", title_color)
    
    return
    
    
###############################################################################
###############################################################################
#
#
#
#
#
#
#       1.2.    PRINTING FUNCTIONS...
###############################################################################
    
#   "print_scr"
#
def print_scr(win, text:str, clear:bool=False, color=None, attribute=None) -> None:
    if (clear):                     win.clear();
    if (color is None):             color = curses.color_pair(2);
    if (attribute is not None):     color = color|attribute;

    x, y    = win.getyx()
    win.addstr(x, y, text, color)
    win.refresh()
    return

    
###############################################################################
###############################################################################
#
#
#
#
#
#
#       1.3.    GENERAL UTILITY FUNCTIONS...
###############################################################################

#   "_not_implemented"
#
def _not_implemented(self, stdscr):
    raise NotImplementedError()
    return
    
    
#   "quit"
#
def quit(self):
    raise SystemExit("normal exit")
    return


#   "spell_check"
#
def spell_check(self, input:str, n:int=1, cutoff:float=0.6):
    return difflib.get_close_matches( input, self.command_keys, n=n, cutoff=cutoff )

    
###############################################################################
###############################################################################
#
#
#
#
#
#
#       1.4.    APPLICATION CLASS FUNCTIONS...
###############################################################################





###############################################################################
###############################################################################
#   END "UTILITY" FUNCTIONS...






#   "POPUP" CLASS...
#
###############################################################################
###############################################################################
@dataclass(order=True, kw_only=True)
class Popup:
    stdscr:         curses.window   = field(default=None,           init=True,          compare=True,
                                            hash=True,              repr=True)
                                            
    name:           str             = field(default=None,           init=True,          compare=True,
                                            hash=True,              repr=True)
                                            
    dims:           tuple           = field(default=None,           init=True,          compare=True,
                                            hash=True,              repr=True)
                                            
    dims:           tuple           = field(default=None,           init=True,          compare=True,
                                            hash=True,              repr=True)
                                            
    pos:            tuple           = field(default=None,           init=True,          compare=True,
                                            hash=True,              repr=True)
                                            
    win:            curses.window   = field(default=None,           init=False,         compare=True,
                                            hash=True,              repr=True)
                                            
    fields:         list            = field(default_factory=list,   init=True,          compare=True,
                                            hash=True,              repr=True)
                                            
    #   CONSTANTS...
    #
    fdims:          tuple           = field(default=(1,25),         init=True,          compare=True,
                                            hash=True,              repr=True)
    inset:          int             = field(default=4,              init=False,         compare=True,
                                            hash=True,              repr=True)
    space:          int             = field(default=4,              init=False,         compare=True,
                                            hash=True,              repr=True)
    instr_1:        str             = field(default="Use \"ARROW KEYS\" to change entry.",              init=False,
                                            compare=False,          hash=False,                         repr=False)
    instr_2:        str             = field(default="Press \"ENTER\" to submit or \"ESC\" to cancel.",  init=False,
                                            compare=False,          hash=False,                         repr=False)
                                            
    #   STATE VARIABLES...
    #
    visible:        bool            = field(default=True,           init=False,         compare=True,
                                            hash=True,              repr=True)
    has_focus:      bool            = field(default=False,          init=False,         compare=True,
                                            hash=True,              repr=True)
    has_instr:      bool            = field(default=False,          init=False,         compare=True,
                                            hash=True,              repr=True)


###############################################################################
###############################################################################
#
#
#
#   1.  INITIALIZATION / BUILT-IN FUNCTIONS...
###############################################################################
                                        
    #   "__post_init__"
    #
    def __post_init__(self):
        #   0.  INITIAL EXCEPTION CHECKS...
        if (self.dims is None):
            raise ValueError("Popup window has no assigned dimensions")
        if (self.pos is None):
            raise ValueError("Popup window has no assigned position")
            
        #   1.  COMPUTE ADDITIONAL CONSTANTS...
        if ( self.fields is None or len(self.fields) == 0 ):
            self.max_len = 0
        else:
            self.max_len = max(len(s) for s in self.fields)
        self.sep        = self.space + self.max_len
        
        
        #   2.  DYNAMICALLY ADJUST POP-UP WINDOW SIZE (IF NEEDED)...
        required_height = 4 + 3*(len(self.fields))
        required_width  = 2*self.inset + self.max_len + self.space + self.fdims[1]
        if (self.dims[0] < required_width):
            dims        = ( math.ceil(1.1*required_height), self.dims[1] )
            self.dims   = dims
            UTL.log(f"Adjusting height of Popup window \"{self.name}\".", type=ANSI.WARN)
            
        if (self.dims[1] < required_width):
            self.dims[1] = math.ceil(1.1*required_width)
            UTL.log(f"Adjusting width of Popup window \"{self.name}\".", type=ANSI.WARN)
        
        self._init()
        return
        
        
    #   "_init"
    #
    def _init(self):
        stdscr          = self.stdscr
        
        #   1.  DRAW MAIN WINDOW...
        self.win        = draw_panel(self.dims, self.pos, title=self.name)
        self.panel      = panel.new_panel(self.win)
        
        #   2.  DEFINE CONSTANTS...
        entries         = []
        N               = len(self.fields)
        
        #   3.  DRAW EACH "FIELD" / "ENTRY"...
        for i in range(1, N+1):
            label       = self.fields[i-1]
            entry       = {'label':label}
            lpos        = ( 3*(i),                      self.inset )
            bpos        = ( 3*(i)+1,                    self.inset + self.sep )
            fpos        = ( self.pos[0] + 3*i,      self.pos[1] + self.inset + self.sep )
            diff        = self.max_len - len(label)
            
            #       3.1.    Plot the label.
            self.win.addstr(lpos[0], lpos[1], f"{' '*diff}{label}", curses.color_pair(1))
            
            #       3.2.    Plot the field.
            entry['win']        = draw_panel(self.fdims, fpos, box=False)
            self.win.hline(bpos[0], bpos[1], curses.ACS_HLINE, self.fdims[1])
            entry['tbox']       = tp.Textbox(entry['win'])
            entry['panel']      = panel.new_panel(entry['win'])
            entries.append(entry)
        
        self.fields.clear()
        self.fields = entries
        self.hide()
        return


###############################################################################
###############################################################################
#
#
#
#   2.  UTILITY / HELPER FUNCTIONS...
###############################################################################
        
    #   "_lpos"         Get the position of a label.
    #
    def _lpos(self, i:int):
        return ( 3*(i+1),  self.inset )
    
    
    #   "set_label"
    #
    def set_label(self, i:int):
        lpos    = self._lpos(i)
        label   = self.fields[i]['label']
        diff    = self.max_len - len(label)
        self.win.addstr(lpos[0], lpos[1], f"{' '*diff}{label}", curses.color_pair(1))
        return
        
        
    #   "hl_label"
    #
    def hl_label(self, i:int):
        lpos    = self._lpos(i)
        label   = self.fields[i]['label']
        diff    = self.max_len - len(label)
        self.win.addstr(lpos[0], lpos[1], f"{' '*diff}", curses.color_pair(1))
        self.win.addstr(lpos[0], lpos[1]+diff, f"{label}", curses.color_pair(1)|curses.A_STANDOUT)
        return
        
        
    #   "_show_instructions"
    #
    def _show_instructions(self):
        if (self.has_instr):
            return
        
        #   DRAW INSTRUCTIONS AT BOTTOM...
        ipos                = (self.dims[0]-3, 0)
        offset              = ( (self.dims[1] - len(self.instr_1))//2,     (self.dims[1] - len(self.instr_2))//2 )
        self.win.addstr( ipos[0],   ipos[1]+offset[0],     f"{self.instr_1}",     curses.color_pair(3) )
        self.win.addstr( ipos[0]+1, ipos[1]+offset[1],     f"{self.instr_2}",     curses.color_pair(3) )
        self.has_instr = True
        return
        
        
    #   "_hide_instructions"
    #
    def _hide_instructions(self):
        if (not self.has_instr):
            return
            
        L1  = len(self.instr_1);    L2 = len(self.instr_2);
        ipos                = (self.dims[0]-3, 0)
        offset              = ( (self.dims[1] - L1)//2,     (self.dims[1] - L2)//2 )
        self.win.addstr( ipos[0],   ipos[1]+offset[0],     f"{' '*L1}",     curses.color_pair(3) )
        self.win.addstr( ipos[0]+1, ipos[1]+offset[1],     f"{' '*L2}",     curses.color_pair(3) )
        self.has_instr = False
        return
    
    
    #   "set_title"
    #
    def set_title(self, title:str, title_padding:int=_UI['title_padding']):
        self.name = title
        curses.curs_set(0)  #   1.  Clear the title.
        self.win.move(0, 0)
        self.win.clrtoeol()
        self.win.box()
        self.win.addstr(0, title_padding+1, f"{' '*title_padding}{title}{' '*title_padding}", curses.color_pair(1))
        
        if (self.visible):
            self.panel.show()
            for entry in self.fields:
                entry['panel'].show()
            panel.update_panels()
            curses.doupdate()
        
        return
    
    
    #   "focus"
    #
    def focus(self, title_padding:int=_UI['title_padding']):
        if (self.has_focus):
            return
        
        self.show()      # If window is hidden, make it visible (cannot focus a hidden window).
        self.win.addstr(0, title_padding+1, f"{' '*title_padding}{self.name}{' '*title_padding}", curses.color_pair(1)|curses.A_STANDOUT)
        self.win.refresh()
        self.has_focus = True
        self._show_instructions()
        curses.curs_set(0)
        self.win.refresh()
        return
    
    
    #   "unfocus"
    #
    def unfocus(self, title_padding:int=_UI['title_padding']):
        if (not self.has_focus):
            return
        
        self.win.addstr(0, title_padding+1, f"{' '*title_padding}{self.name}{' '*title_padding}", curses.color_pair(1))
        self.win.refresh()
        self.has_focus = False
        return
        
    
    #   "refresh"
    #
    def refresh(self):
        self.win.refresh()
        for field in self.fields:
            if ('win' in field):
                field['win'].refresh()
        return
        
    
    #   "clear"
    #
    def clear(self) -> list:
        curses.curs_set(0)
        for entry in self.fields:
            entry['win'].clear()
            
        return
        
    
    #   "clear_and_refresh"
    #
    def clear_and_refresh(self) -> list:
        self.win.refresh()
        for entry in self.fields:
            entry['win'].clear()
            entry['win'].refresh()
            
        curses.curs_set(0)
        return
    

###############################################################################
###############################################################################
#
#
#
#
#
#
#   2.  OPERATION FUNCTIONS...
###############################################################################
        
    #   "hide"
    #
    def hide(self):
        if (not self.visible):
            return
        
        self.panel.hide()
        for entry in self.fields:
            entry['panel'].hide()
        panel.update_panels()
        curses.doupdate()
        self.visible = False
        return
        
        
    #   "show"
    #
    def show(self):
        if (self.visible):
            return
            
        self.panel.show()
        for entry in self.fields:
            entry['panel'].show()
        panel.update_panels()
        curses.doupdate()
        self.visible = True
        return
        
    
    #   "edit"
    #
    def edit(self):
        if ( (not self.visible) or (not self.has_focus) ):
            self.focus()
        
        try:
            self.edit_entry(self.stdscr)
        #
        #
        except KeyboardInterrupt as e:
            self.unfocus()
            curses.curs_set(2)
            raise(e)
        
        return
        
        
    #   "edit_entry"
    #
    def edit_entry(self, stdscr) -> str:
        editing         = True
        capture         = True
        i               = 0
        N               = len( self.fields)
        curses.cbreak()  # Alternatively: curses.raw()
        curses.noecho()
        stdscr.keypad(True)
        curses.curs_set(2)
        
        
        def change_entry(i:int) -> tuple:
            if not hasattr(change_entry, "prev"):
                change_entry.prev = i
            
            self.set_label(change_entry.prev)
            change_entry.prev   = i if (change_entry.prev != i) else change_entry.prev
            self.hl_label(i)
            win     = self.fields[i]['win']
            box     = self.fields[i]['tbox']
            y, x    = win.getmaxyx()
            return (win, box, x, y)
            

        while (editing):
            win, box, xmax, ymax    = change_entry(i)
            capture                 = True if (editing) else False
        #
        #
        #   1.  ALLOW USER TO PROVIDE INPUT...
            while (capture):
                y, x    = box.win.getyx()
                win.move(y, x)
                key     = box.win.getch()
                
                #   1.1.    SPECIAL CHARACTERS...
                if (key in (curses.KEY_DOWN, curses.KEY_BTAB, 9)):      #   DOWN-ARROW or TAB.
                    i = (i+1) % N
                    capture = False
                #
                elif (key == curses.KEY_UP):                            #   UP-ARROW.
                    i = (i-1) % N
                    capture = False
                #
                elif (key == 27):                                       #   ESCAPE-KEY.
                    self.set_label(i)
                    raise KeyboardInterrupt("User pressed escape-key during input operation.")
                #
                #
                #
                else:
                    #   CASE 1 :    "ENTER"
                    if ( key in (curses.KEY_ENTER, 10, 13) ):
                        i       = i + 1
                        editing = True if (i < N) else False
                        capture = False
                    #
                    #   CASE 2 :    "BACKSPACE"
                    elif (key in (curses.KEY_BACKSPACE, 127)):
                        if ( (x==0) and (0 < y) ):          #   2.1.    Delete at the beginning of a line (skip up to previous line).
                            box.win.move(y-1, xmax)
                            box.win.delch(y-1, xmax)
                        elif (0 < x):                       #   2.2.    Delete in the middle of the line.
                            box.win.delch(y, x-1)
                    #
                    #   CASE 5 :    "NORMAL CHARACTER"
                    else:
                        if ( (x < xmax-1) ):                #   3.1.    Add character normally.
                            box.win.addch(key)
                        else:                               #   3.2.    At the end of input field.
                           pass


        #   3.  RESET THE INPUT BOX...
        self.set_label(i-1)
        return #response.rstrip()
        
        
    #   "gather"
    #
    def gather(self) -> list:
        values = []
        for entry in self.fields:
            values.append( entry['tbox'].gather().rstrip() )
            
        self.unfocus()
        return values
    
    
    #   "load"
    #
    def load(self, values:list) -> None:
        
        for value, field in zip(values, self.fields):
            field['win'].clear()
            field['win'].addstr(0,0,value)
            field['win'].refresh()
            
        return
        

###############################################################################
###############################################################################
#   END OF "POPUP" CLASS...






###############################################################################
###############################################################################
#   END.
