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
    
