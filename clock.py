import time

def stopwatch():  
    global total_seconds  
    total_seconds = 0  
    while True:  
        time.sleep(1)  
        total_seconds += 1

def print_seconds_elapsed():  
    print("Total seconds elapsed:", total_seconds)

start_time = time.time()  
while True:  
    stopwatch()  
    print_seconds_elapsed()  
    time.sleep(1)  
