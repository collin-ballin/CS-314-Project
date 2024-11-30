import curses
from curses.textpad import Textbox, rectangle



def main(stdscr):
    # Draw prompt at the top of the screen
    stdscr.addstr(0, 0, "Enter IM message: (press Enter to send)")

    # Create a window for the text box
    editwin = curses.newwin(5, 30, 2, 1)
    rectangle(stdscr, 1, 0, 1 + 5 + 1, 1 + 30 + 1)  # Draw a rectangle around the edit window
    stdscr.refresh()

    # Create the Textbox object
    box = Textbox(editwin)

    while (True):
        # Edit the box manually to capture each key press
        key = box.win.getch()

        if key == curses.KEY_ENTER or key == 10 or key == 13:
            # Break the loop if Enter key is pressed
            break
        elif key in (curses.KEY_BACKSPACE, 127):
            # Handle backspace
            y, x = box.win.getyx()
            if x > 0:
                box.win.delch(y, x - 1)
        else:
            # Add the character to the text box
            box.win.addch(key)

    # Get resulting contents
    message = box.gather()

    # Display the message in the terminal (for testing)
    stdscr.addstr(8, 0, f"Message submitted: {message}")
    stdscr.refresh()

    # Wait for user to see the output before exiting
    stdscr.getch()
    
    
    
    
def test(stdscr):
    stdscr.addstr(0, 0, "Enter IM message: (hit Ctrl-G to send)")

    h=5
    w=10
    x=5
    y=2
    
    xp=0
    yp=0
    hp=1
    wp=0
    editwin = curses.newwin(h, w, y, x)
    rectangle(stdscr, hp,wp, 1+h+1, 1+w+1)
    stdscr.refresh()

    box = Textbox(editwin)

    # Let the user edit until Ctrl-G is struck.
    box.edit()

    # Get resulting contents
    message = box.gather()
    
    
    
def main_curses(stdscr):
    # Turn off cursor
    curses.curs_set(0)

    # Sample content to display in a scrollable manner
    content = [
        "Welcome to the interactive pager-like UI using curses!",
        "Use UP and DOWN arrows to scroll through this content.",
        "Press ENTER to select a section.",
        "Press 'q' to exit.",
        "",
        "SECTION 1: Overview",
        "This is an overview of the application.",
        "",
        "SECTION 2: Instructions",
        "Instructions on how to use the features are listed here.",
        "",
        "SECTION 3: Examples",
        "Here you will find examples of using the application.",
        "",
        "End of Content - Press 'q' to quit."
    ]

    # Initialize variables
    current_line = 0
    max_lines = len(content)

    # Main loop
    while True:
        # Clear screen and refresh
        stdscr.clear()

        # Get screen height to control scrolling
        height, width = stdscr.getmaxyx()

        # Calculate the visible lines
        start_line = max(0, min(current_line, max_lines - height))
        end_line = min(max_lines, start_line + height)

        # Display the visible lines
        for idx, line in enumerate(content[start_line:end_line]):
            stdscr.addstr(idx, 0, line[:width])

        # Refresh screen
        stdscr.refresh()

        # Get user input
        key = stdscr.getch()

        # Navigate content
        if key == curses.KEY_DOWN and current_line < max_lines - 1:
            current_line += 1
        elif key == curses.KEY_UP and current_line > 0:
            current_line -= 1
        elif key == ord('q'):
            break
        elif key == ord('\n'):
            # Placeholder for more detailed section selection
            stdscr.addstr(height - 1, 0, "You pressed ENTER. More interactivity could be added here.")
            stdscr.refresh()
            stdscr.getch()  # Wait for another key press to proceed







if __name__ == "__main__":
    #value = curses.wrapper(main)
    value = curses.wrapper(test)
    print(f"Message recieved was:\n\"{value}\".")
    



































def holder(self, stdscr):
    # Main interaction loop
    while (True):
        # Example prompt and user input handling
        self.UI['out'].clear()
        self.UI['out'].box()
        self.UI['out'].addstr(1, 2, "1 Please enter your 9-digit provider ID number:", curses.color_pair(2))
        #self.UI['out'].refresh()

        # Get user input
        self.UI['in'].clear()
        self.UI['in'].box()
        self.UI['in'].addstr(1, 2, "INPUT", curses.color_pair(3))
        #self.UI['in'].refresh()

        curses.echo()
        input_value = self.UI['in'].getstr(1, 8).decode('utf-8')  # Capture user input
        
        # Display the user's input back in the output area
        self.UI['out'].clear()
        self.UI['out'].box()
        self.UI['out'].addstr(1, 2, f"1 Received: \"{input_value}\"", curses.color_pair(2))
        #self.UI['out'].refresh()

        # Note: Loop will continue and input will be asked again, just like your screenshots showed
        
    return










































def setup_UI(self, stdscr):

    #   0.  INITIALIZE ELEMENTS OF UI...
    #
    #       0.1.    Colors.
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)      #   Header Text.
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)     #   Output Text.
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)       #   Input Text.
    #
    #       0.2.    Initial Commands.
    stdscr.clear()                                                  #   Clear the screen
    #
    #       0.3.    Initial Values.
    #curses.curs_set(0)                                             #   ANSI.HIDE
    curses.noecho()                                                 #   Disable real-time printing of input to screen.
    height, width = stdscr.getmaxyx()                               #   Screen Dimensions.
    
    
    #   2.  CREATE WINDOW FOR EACH SECTION OF OUTPUT...
    #
    #       2.1.    Header Window.
    header_win              = curses.newwin(3, width - 2, 0, 1)  # 3 lines high, full width
    header_win.box()
    header_win.addstr(1, 2, self.prompts['header'], curses.color_pair(1)|curses.A_BOLD)
    header_win.refresh()
    #
    #       2.2.    Program-Output Window.
    output_win              = curses.newwin(6, width - 2, 4, 1)  # 6 lines high, below header
    output_win.box()
    output_win.refresh()
    #
    #       2.3.    User-Input Window.
    input_win               = curses.newwin(3, width - 2, 11, 1)  # 3 lines high, below output
    rectangle(stdscr, 1, 0, 1 + 5 + 1, 1 + 30 + 1)  # Draw a rectangle around the edit window
    stdscr.refresh()

    # Create the Textbox object
    box = Textbox(editwin)
    
    
    input_win               = curses.newwin(3, width - 2, 11, 1)  # 3 lines high, below output
    input_win.box()
    input_win.addstr(1, 2, "INPUT", curses.color_pair(3))  # Red input label
    input_win.refresh()
    
    
    #   3.  ASSIGN EACH WINDOW TO THE CLASS UI...
    self.UI['header']       = header_win
    self.UI['out']          = output_win
    self.UI['in']           = input_win
    
    return
