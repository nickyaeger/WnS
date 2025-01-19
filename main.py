import time
import threading
from datetime import datetime, timedelta
from games import sounds
from games import jumping_jack, memory_game, whackamole, math_game, wake_n_shake, pushup
from display import display_digits
from buttons import Buttons
import settings
from camera import CameraManager
import sounds

# Define states
IDLE = "idle"
ALARM_SET_HOUR = "alarm_set_hour"
ALARM_SET_MINUTE = "alarm_set_minute"
GAME_SET = "game_set"
TIME_SET_HOUR = "time_set_hour"
TIME_SET_MINUTE = "time_set_minute"
ALARM = "alarm"
GAME = "game"
POST_ALARM = "post_alarm"

# Global variables
current_state = IDLE
alarm_time = "0700"
selected_game = "jumping_jack"
current_time = datetime.now()  # Internal time starts with the current system time
time_lock = threading.Lock()  # To safely update the time across threads
buttons = Buttons()
start_alarm = False


# Function to increment internal time
def increment_internal_time():
    global current_time

    while True:
        with time_lock:
            current_time += timedelta(seconds=1)  # Increment the internal clock
        time.sleep(1)


# Function to handle button inputs
def handle_button_input():
    global current_state, selected_game, alarm_time, current_time

    button = get_button_input(buttons)  # Get the pressed button
    if button:
        buttons.light_up_led(button)  # Light up the corresponding LED
    
    # Button handling logic
    if button == "left":  # Navigate left
        if current_state == IDLE:
            print("Setting alarm...")
            settings.alarm = int(alarm_time)
            current_state = ALARM_SET_HOUR
        elif current_state == ALARM_SET_HOUR:
            print("Setting alarm minute...")
            current_state = ALARM_SET_MINUTE  # Switch to minute setting
        elif current_state == ALARM_SET_MINUTE:
            print("Setting alarm hour...")
            current_state = ALARM_SET_HOUR  # Switch to hour setting
        elif current_state == GAME_SET:
            print("Editing game...")
            selected_game = settings.edit_game_left()  # Cycle left through game options
        elif current_state == TIME_SET_HOUR:
            print("Setting time minute...")
            current_state = TIME_SET_MINUTE  # Switch to minute setting
        elif current_state == TIME_SET_MINUTE:
            print("Setting time hour...")
            current_state = TIME_SET_HOUR  # Switch to hour setting
    elif button == "up":  # Increment
        if current_state == IDLE:
            print("Setting game...")
            current_state = GAME_SET
        elif current_state == ALARM_SET_HOUR:
            settings.increment_alarm_hour()
        elif current_state == ALARM_SET_MINUTE:
            settings.increment_alarm_minute()
        elif current_state == TIME_SET_HOUR:
            settings.increment_time_hour()
        elif current_state == TIME_SET_MINUTE:
            settings.increment_time_minute()
    elif button == "right":  # Navigate right
        if current_state == IDLE:
            print("Setting time...")
            settings.time = int(current_time.strftime("%H%M"))
            current_state = TIME_SET_HOUR
        elif current_state == ALARM_SET_HOUR:
            print("Setting alarm minute...")
            current_state = ALARM_SET_MINUTE  # Switch to minute setting
        elif current_state == ALARM_SET_MINUTE:
            print("Setting alarm hour...")
            current_state = ALARM_SET_HOUR  # Switch to hour setting
        elif current_state == GAME_SET:
            print("Editing game...")
            selected_game = settings.edit_game_right()  # Cycle right through game options
        elif current_state == TIME_SET_HOUR:
            print("Setting time minute...")
            current_state = TIME_SET_MINUTE  # Switch to minute setting
        elif current_state == TIME_SET_MINUTE:
            print("Setting time hour...")
            current_state = TIME_SET_HOUR  # Switch to hour setting
    elif button == "down":  # Decrement
        if current_state == IDLE:
            pass
        elif current_state == ALARM_SET_HOUR:
            settings.decrement_alarm_hour()
        elif current_state == ALARM_SET_MINUTE:
            settings.decrement_alarm_minute()
        elif current_state == TIME_SET_HOUR:
            settings.decrement_time_hour()
        elif current_state == TIME_SET_MINUTE:
            settings.decrement_time_minute()
    elif button == "center":  # Confirm/Select
        if current_state == IDLE:
            pass
        elif current_state == ALARM_SET_HOUR or current_state == ALARM_SET_MINUTE:
            alarm_time = str(settings.alarm)  # Confirm the current setting
            print("Alarm set to:", alarm_time)
            current_state = IDLE
        elif current_state == GAME_SET:
            selected_game = settings.games[settings.index][1]  # Confirm the current setting
            print("Confirmed game:", selected_game)
            current_state = IDLE
        elif current_state == TIME_SET_HOUR or current_state == TIME_SET_MINUTE:
            current_time = datetime.strptime(str(settings.time), "%H%M")  # Confirm the current setting
            print("Time set to:", current_time.strftime("%H:%M"))
            current_state = IDLE
    elif button == "demo":  # Start demo
        print("Demo button pressed...")
        current_state = ALARM


# Alarm checker (runs in a thread)
def check_alarm():
    global current_state, start_alarm

    while True:
        with time_lock:
            now = current_time.strftime("%H%M")  # Use internal time
            now_with_seconds = current_time.strftime("%H:%M:%S")
            print("Current time:", now_with_seconds)
            if current_state == IDLE:
                display_digits(current_time.strftime("%H%M"))
        if now == alarm_time and current_state == IDLE:
            current_state = ALARM
        if current_state == ALARM or current_state == GAME:
            if start_alarm:
                sounds.playAlarm()
        time.sleep(1)


# Main state machine loop
def main_loop():
    global current_state, selected_game, start_alarm
    print("Entering main loop...")
    print("Welcome to the Wake 'n' Shake Alarm Clock! Press Ctrl+C to exit.")
    print("The current state is:", current_state)
    print("The current time is:", current_time.strftime("%H:%M"))
    print("The current alarm is set to:", alarm_time)
    print("The selected game is:", selected_game)
    sounds.playMenu()
    while True:
        if current_state == IDLE:
            # Display current time
            # with time_lock:
                # display_digits(current_time.strftime("%H%M"))
                # time.sleep(0.05)
            pass
        elif current_state == ALARM_SET_HOUR:
            # display_digits(str(settings.alarm)[0] + str(settings.alarm)[1] + "  ", colon=1, colors=[(255, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0)])
            if settings.alarm < 10:
                display_digits("000" + str(settings.alarm))
            elif settings.alarm < 100:
                display_digits("00" + str(settings.alarm))
            elif settings.alarm < 1000:
                display_digits("0"+ str(settings.alarm))
            else:
                display_digits(str(settings.alarm))
        elif current_state == ALARM_SET_MINUTE:
            # display_digits("  " + str(settings.alarm)[2] + str(settings.alarm)[3], colon=1, colors=[(0, 0, 0), (0, 0, 0), (255, 0, 0), (255, 0, 0)])
            if settings.alarm < 10:
                display_digits("000" + str(settings.alarm))
            elif settings.alarm < 100:
                display_digits("00" + str(settings.alarm))
            elif settings.alarm < 1000:
                display_digits("0"+ str(settings.alarm))
            else:
                display_digits(str(settings.alarm))
        elif current_state == GAME_SET:
            display_digits("000" + str(settings.index))
        elif current_state == TIME_SET_HOUR:
            # display_digits(str(settings.time)[0] + str(settings.time)[1] + "  ", colon=1, colors=[(0, 0, 255), (0, 0, 255), (0, 0, 0), (0, 0, 0)])
            if settings.time < 10:
                display_digits("000" + str(settings.time))
            elif settings.time < 100:
                display_digits("00" + str(settings.time))
            elif settings.time < 1000:
                display_digits("0"+ str(settings.time))
            else:
                display_digits(str(settings.time))
        elif current_state == TIME_SET_MINUTE:
            # display_digits("  " + str(settings.time)[2] + str(settings.time)[3], colon=1, colors=[(0, 0, 0), (0, 0, 0), (0, 0, 255), (0, 0, 255)])
            if settings.time < 10:
                display_digits("000" + str(settings.time))
            elif settings.time < 100:
                display_digits("00" + str(settings.time))
            elif settings.time < 1000:
                display_digits("0"+ str(settings.time))
            else:
                display_digits(str(settings.time))
        elif current_state == ALARM:
            # Trigger alarm
            print("Alarm triggered!")
            sounds.playWakeup()
            start_alarm = True
            # for i in range(3):
                # display_text("WAKE")
                # time.sleep(0.4)
                # display_text("AKE ")
                # time.sleep(0.4)
                # display_text("KE U")
                # time.sleep(0.4)
                # display_text("E UP")
            # time.sleep(2)
            # display_text("GAME")
            current_state = GAME
        elif current_state == GAME:
            # Run the selected game
            run_game(selected_game)
            current_state = POST_ALARM
        elif current_state == POST_ALARM:
            # Resume idle state after alarm/game
            # display_text("GOOD")
            # time.sleep(0.4)
            # display_text("OOD ")
            # time.sleep(0.4)
            # display_text("OD M")
            # time.sleep(0.4)
            # display_text("D MO")
            # time.sleep(0.4)
            # display_text(" MOR")
            # time.sleep(0.4)
            # display_text("MORN")
            # time.sleep(0.4)
            # display_text("ORNI")
            # time.sleep(0.4)
            # display_text("RNIN")
            # time.sleep(0.4)
            # display_text("NING")
            # display_text("    ")
            time.sleep(3)  # Pause for a bit
            current_state = IDLE

        # Check for button input in every loop iteration
        handle_button_input()
        time.sleep(0.1)


# Run the selected game
def run_game(game_name):
    if game_name == "jumping_jack":
        sounds.playJump()
        jumping_jack.start_game()
    elif game_name == "memory_game":
        sounds.playMemory()
        memory_game.start_game()
    elif game_name == "whackamole":
        sounds.playWhackamole()
        whackamole.start_game()
    elif game_name == "math_game":
        math_game.start_game()
    elif game_name == "wake_n_shake":
        sounds.playShake()
        wake_n_shake.start_game()
    elif game_name == "pushup":
        pushup.start_game()
    else:
        print(f"Unknown game: {game_name}")
    CameraManager.release_camera()


# Getting button input using the Buttons class
def get_button_input(buttons):
    return buttons.get_pressed_button()


# Main entry point
if __name__ == "__main__":
    # Start the alarm checker thread
    alarm_thread = threading.Thread(target=check_alarm, daemon=True)
    alarm_thread.start()
    print("Alarm checker started...")

    # Start the internal clock thread
    clock_thread = threading.Thread(target=increment_internal_time, daemon=True)
    clock_thread.start()
    print("Internal clock started...")

    # Run the main state machine loop
    try:
        print("Starting main loop...")
        main_loop()
    finally:
        buttons.cleanup()  # Clean up GPIO pins
