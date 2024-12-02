from lib.utility import ANSI
import lib.utility as UTL
import lib as app
import termios, tty, select
import os, sys, signal, traceback
import curses



#   "main"
#
def main(stdscr):
    # Initialize
    curses.curs_set(0)  # Hide the default cursor
    stdscr.nodelay(False)  # Make getch() blocking
    stdscr.keypad(True)  # Enable special keys
    
    # Starting position
    y, x = stdscr.getmaxyx()
    y //= 2
    x //= 2
    stdscr.addch(y, x, '*')
    stdscr.refresh()
    
    while True:
        key = stdscr.getch()
        stdscr.addch(y, x, ' ')  # Clear previous position
        
        if key == curses.KEY_UP:
            y = max(0, y - 1)
        elif key == curses.KEY_DOWN:
            y = min(curses.LINES - 1, y + 1)
        elif key == curses.KEY_LEFT:
            x = max(0, x - 1)
        elif key == curses.KEY_RIGHT:
            x = min(curses.COLS - 1, x + 1)
        elif key == ord('q'):
            break  # Exit on 'q' key
        
        stdscr.addch(y, x, '*')  # Draw at new position
        stdscr.refresh()
    
    return status



###############################################################################

#   Hook for the "main" function...
#
if (__name__ == '__main__'):
    curses.wrapper(main)
    #sys.exit( main() )






###############################################################################
###############################################################################
#   END.



















#   STORAGE...
###############################################################################
###############################################################################

def timer():
    for i in range(10, -1, -1):
        print(f"\rTime remaining: {i} seconds", end='')
        time.sleep(1)
        
    print("\nTime's up!")
 
    for i in range(0, len(image)):
        row = image[i]
        for j in range(0, len(row)):
            print(row[j], sep='', end='')
        print('')
        
    return









#   "image_to_ascii"
#
def image_to_ascii(image_path, columns:int=50, threshold=0.5, exposure=0.5):
    ASCII_CHARS = [
                    f"{ANSI.WHITE_BB}▓{ANSI.RESET}",    f"{ANSI.WHITE}▒{ANSI.RESET}",
                    #f"{ANSI.WHITE}░{ANSI.RESET}",
                    #f"{ANSI.WHITE_BB} {ANSI.RESET}",
                    f"{ANSI.BLACK} {ANSI.RESET}",
                    f"{ANSI.BLACK}█{ANSI.RESET}"
                ]
    
    #ASCII_CHARS = ["@", "%", "#", "*", "+", "=", "-", ":", ".", " "]
    #ASCII_CHARS = ["█", "▓", "▒", "░", " "]
    ASCII_CHARS = np.array(["@", "%", "#", "*", "+", "=", "-", ":", ".", " "])

    try:
        # Load the image
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file {image_path}.")
        print(e)
        return None  # Return None if the image cannot be opened

    # Convert the image to grayscale
    image = image.convert("L")

    # Resize the image according to the specified number of columns
    width, height = image.size
    aspect_ratio = height / width
    new_width = columns
    new_height = int(aspect_ratio * new_width * 0.55)  # Adjust for character height
    image = image.resize((new_width, new_height))

    # Get the pixel data from the image
    pixels = list(image.getdata())

    # Adjust pixel values based on the threshold and exposure
    adjusted_pixels = []
    for pixel in pixels:
        # Normalize pixel value to 0-1
        normalized_pixel = pixel / 255.0

        # Apply threshold adjustment
        if normalized_pixel < threshold:
            # Scale darker pixels towards 0
            adjusted_pixel = (normalized_pixel / threshold) * 0.5
        else:
            # Scale brighter pixels towards 1
            adjusted_pixel = 0.5 + ((normalized_pixel - threshold) / (1 - threshold)) * 0.5

        # Apply exposure adjustment using gamma correction
        # Map exposure (0 to 1) to gamma values (2.0 to 0.5)
        gamma = 2.0 - exposure * 1.5  # Gamma decreases as exposure increases

        # Ensure gamma is not less than 0.1 to prevent division by zero
        gamma = max(gamma, 0.1)

        # Apply gamma correction
        adjusted_pixel = adjusted_pixel ** gamma

        # Scale back to 0-255
        adjusted_pixel = int(adjusted_pixel * 255)
        adjusted_pixels.append(adjusted_pixel)

    # Map each adjusted pixel to an ASCII character
    new_pixels = [
        ASCII_CHARS[adjusted_pixel * (len(ASCII_CHARS) - 1) // 255] for adjusted_pixel in adjusted_pixels
    ]

    # Create a 2D array (list of lists) of ASCII characters
    ascii_image = [
        new_pixels[index: index + new_width]
        for index in range(0, len(new_pixels), new_width)
    ]

    return ascii_image
    
    
    
#   "animate"
#
def animate(ascii_image, frames=20, interval=0.1):
    #sys.stdout.write(f"{ANSI.HIDE}")
    
    
    # ASCII characters used to build the output text
    ASCII_CHARS = np.array(["@", "%", "#", "*", "+", "=", "-", ":", ".", " "])

    # Create a mapping from character to index
    char_to_index = {char: idx for idx, char in enumerate(ASCII_CHARS)}
    vectorized_char_to_index = np.vectorize(char_to_index.get)
    ascii_indices = vectorized_char_to_index(ascii_image)

    # Invert the indices to create the inverted image
    inverted_ascii_indices = len(ASCII_CHARS) - 1 - ascii_indices
    inverted_ascii_image = ASCII_CHARS[inverted_ascii_indices]

    num_lines   = len(ascii_image)
    pause       = 1
    speed       = 0.03


    # Print the initial frame
    for row in ascii_image:
        time.sleep(speed)
        print(''.join(row))
    sys.stdout.flush()

    
    
    time.sleep(pause)
        
        
    #   Start the animation loop
    sys.stdout.write(f"{ANSI.UP(num_lines)}")
    for row in ascii_image:
        time.sleep(speed)
        ANSI.down(1)
        #print(''.join(row))
    sys.stdout.flush()
        
        
    #sys.stdout.write(f"{ANSI.SET(i, 0)}{ANSI.CLEAR_LINE}")
    sys.stdout.flush()
        
        
        
    print(f"\nDone.{ANSI.RESET_ALL}")
    return
    



###############################################################################
###############################################################################
#   END...
