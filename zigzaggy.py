import time
import sys

indent = 0

# Whether the indentation is increasing or not
indent_increase = True 

try:
    while True:
        print(" " * indent, end="")
        print('********')
        # Pause for 1/10th of a second
        time.sleep(0.1)

        if indent_increase:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
                indent_increase = False
        else:
            # Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change Direction:
               indent_increase = True
except KeyboardInterrupt:
    sys.exit()