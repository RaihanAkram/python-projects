import time

# countdown function
def countdown(t):
    while t:
        hours, remainder = divmod(t, 3600) #calculates number of hours and the remaining seconds by dividing time entered by 3600.
        mins, secs = divmod(remainder, 60) #calculates number of minutes from the seconds left after calculating the hours. And gives the number of seconds left.
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs) 
        print(timer, end="\r")  # end = "\r" used to output the time on the same line after updating it
        time.sleep(1)  # delays the running of code by 1 second
        t -= 1

    print('Time up !')

t = input("\nPlease enter time (in seconds) to start the countdown: ")

countdown(int(t))

