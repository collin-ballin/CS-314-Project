import sys
import tty
import termios
import re

def get_cursor_position():
    fd              = sys.stdin.fileno()
    old_settings    = termios.tcgetattr(fd)
    
    try:
        tty.setraw(fd)
        sys.stdout.write("\033[6n")
        sys.stdout.flush()

        # Initialize an empty response
        response = ''
        while True:
            # Read one character at a time
            char = sys.stdin.read(1)
            if char == 'R':
                response += char
                break
            response += char

        # The response should be in the format ESC [ rows ; cols R
        # Example: '\x1b[24;80R'
        match = re.match(r'\x1b\[(\d+);(\d+)R', response)
        if match:
            row, col = match.groups()
            return int(row), int(col)
        else:
            raise ValueError("Unexpected response: {}".format(response))
    finally:
        # Restore the original terminal settings
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def main():
    try:
        row, col = get_cursor_position()
        print(f"\nCursor Position -> Row: {row}, Column: {col}")
    except Exception as e:
        print(f"\nError: {e}")



if __name__ == "__main__":

    #main()
