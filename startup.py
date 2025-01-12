import time
from clock import Clock

clock = Clock()
mode = "clock"

while True:
    if mode == "clock":
        while mode == "clock":
            current_time = time.localtime()
            clock.update(time.strftime("%H%M", current_time), True, [False, False, False, False])
            print(time.strftime("%H:%M:%S", current_time))
            print(clock.char0, clock.char1, clock.char2, clock.char3, clock.colon, clock.led0)
            time.sleep(1)
    
    elif mode == "time_config":
        pass

    elif mode == "alarm_config":
        pass

    elif mode == "ringtone_config":
        pass

    elif mode == "challenge_config":
        pass

    elif mode == "alarm":
        pass