import time
import sys

try:
    # The main program loop
    while True:  
        # Draw lines with increasing length:
        for i in range(1, 9):
            print('-' * (i * i))
            time.sleep(0.1)

        # Draw lines with decreasing length:
        for i in range(7, 1, -1):
            print('-' * (i * i))
            time.sleep(0.1)
            
except KeyboardInterrupt:
    sys.exit()