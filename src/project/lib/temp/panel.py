import curses
from curses import panel




def main(stdscr):
    # Disable cursor and enable keypad input
    curses.curs_set(0)
    stdscr.keypad(1)

    # Clear and refresh the main window
    stdscr.clear()
    stdscr.refresh()

    # Add labels for the windows
    stdscr.addstr(0, 1, "Base Window: Display Area")
    stdscr.addstr(15, 1, "Base Window: Input Area")
    stdscr.refresh()

    # Create a base display window (output area)
    display_win = curses.newwin(15, 60, 1, 1)
    display_win.box()
    display_win.addstr(1, 1, "This is the display area")

    # Create a base input window (input area)
    input_win = curses.newwin(4, 60, 16, 1)
    input_win.box()
    input_win.addstr(1, 1, "This is the input area")

    # Create panels for both base windows
    display_panel = panel.new_panel(display_win)
    input_panel = panel.new_panel(input_win)

    # Create a pop-up window
    popup_win = curses.newwin(10, 40, 5, 10)
    popup_win.box()
    popup_win.addstr(1, 1, "Enter your data here:")
    popup_panel = panel.new_panel(popup_win)
    popup_panel.hide()  # Start with pop-up hidden

    # Create a child input line window for the pop-up
    child_input_win = curses.newwin(3, 38, 11, 11)  # One line input window within pop-up
    child_input_win.box()
    child_input_win.addstr(1, 1, "Type here: ")
    child_input_panel = panel.new_panel(child_input_win)
    child_input_panel.hide()  # Start with pop-up hidden

    # Update panels to reflect initial state
    panel.update_panels()
    curses.doupdate()

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP:
            # Show the pop-up window and its child input window
            popup_panel.show()
            child_input_panel.show()
            stdscr.addstr(4, 10, "Pop-up Window")
            stdscr.refresh()
        elif key == curses.KEY_DOWN:
            # Hide the pop-up window and its child input window
            popup_panel.hide()
            child_input_panel.hide()
            stdscr.move(4, 10)
            stdscr.clrtoeol()
            stdscr.refresh()
        
        # Update panels to reflect changes
        panel.update_panels()
        curses.doupdate()
    
    
    
    
    
    
if (__name__ == '__main__'):
    curses.wrapper(main)
