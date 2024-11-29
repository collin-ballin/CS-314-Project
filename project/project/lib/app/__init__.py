###############################################################################
#
#       ************************************************************
#       ****        ________  I N I T  ________  F I L E        ****
#       ****                                                    ****
#       ****         For  "_app.py"                             ****
#       ************************************************************
#
#
###############################################################################
from dataclasses import dataclass, field






#from ._app import _PROMPTS



# 	CLASS:  "APP"
#
@dataclass(order=True, kw_only=True)
class App:
	'''Main class to implement the Chochoholics-Anonymous healthcare service application.'''
###############################################################################

    #   Class Methods (Imported from "_name.py" files)...
	from ._app import __post_init__
	from ._app import main
	from ._app import run
 
 
	################################################################
	################        Data Members for        ################
	################		     A P P			    ################
	################################################################
	name: 			str			    = field(default=None,
                                            init=True,              compare=True,
                                            hash=True,              repr=True)
                                            
	lw: 			int			    = field(default=87,
                                            init=False,             compare=True,
                                            hash=True,              repr=True)
                                            
	members: 	    list		    = field(default_factory=list,
                                            init=False,             compare=True,
                                            hash=True,              repr=True)
                                            
	providers: 	    list		    = field(default_factory=list,
                                            init=False,             compare=True,
                                            hash=True,              repr=True)
                                            
	UI: 	        dict		    = field(default_factory=dict,
                                            init=False,             compare=False,
                                            hash=False,             repr=False)
                                            
	pos: 	        dict		    = field(default_factory=dict,
                                            init=False,             compare=False,
                                            hash=False,             repr=False)
                                            
	prompts: 	    dict		    = field(default_factory=dict,
                                            init=False,             compare=False,
                                            hash=False,             repr=False)
  

###############################################################################
#   END OF "APP".
#
#
#
#
#
#
#
#
#
#
#
#
###############################################################################
###############################################################################


# 	CLASS:  "APP_OLD"
#
@dataclass(order=True, kw_only=True)
class App_Old:
	'''OLD IMPLEMENTATION.  REPLACING WITH \"App\" CLASS THAT USES \"curses\" / \"stdwin\" TO 
       CREATE AN INTERACTIVE, COMMAND-LINE USER-INTERFACE...   
       Main class to implement the Chochoholics-Anonymous healthcare service application.'''
###############################################################################

    #   Class Methods (Imported from "_name.py" files)...
	from ._app_old import __post_init__
	from ._app_old import run
 
 
	################################################################
	################        Data Members for        ################
	################		     A P P			    ################
	################################################################
	name: 			str			    = field(default=None,
                                            init=True,              compare=True,
                                            hash=True,              repr=True)
                                            
	lw: 			int			    = field(default=87,
                                            init=False,             compare=True,
                                            hash=True,              repr=True)
                                            
	members: 	    list		    = field(default_factory=list,
                                            init=False,             compare=True,
                                            hash=True,              repr=True)
                                            
	providers: 	    list		    = field(default_factory=list,
                                            init=False,             compare=True,
                                            hash=True,              repr=True)
                                            
	pos: 	        dict		    = field(default_factory=dict,
                                            init=False,             compare=False,
                                            hash=False,             repr=False)
                                            
	prompts: 	    dict		    = field(default_factory=dict,
                                            init=False,             compare=False,
                                            hash=False,             repr=False)
  

###############################################################################
#   END OF "APP_OLD".
#
#
#
#
#
#
###############################################################################
###############################################################################
#   END.
