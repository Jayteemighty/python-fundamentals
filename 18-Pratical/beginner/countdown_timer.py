# Ask user for seconds to count down from
# Print a message when it counts down

import time

def countdown():
    print("Welcome to the countdown timer!")
    
    try:
        t = int(input("\nPlease Enter the time in seconds: "))
        if t <= 0:
            print("Please enter a postive number of seconds.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    print("Countdown starting...")
    
    while t:
        mins, secs = divmod(t, 60) # Using secs to countdown
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    
    print(" "  * 10, end='\r')    # clear last timer display
    print("Timer completed!")
    
if __name__ == '__main__':
    countdown()
