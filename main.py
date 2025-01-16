import time
import threading
from datetime import datetime, timedelta
from games import jumping_jack, memory_game, whackamole, math_game, wake_n_shake
from display import display_text
from buttons import left, up, right, down, center, demo
import settings

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


# Function to increment internal time
def increment_internal_time():
    global current_time

    while True:
        with time_lock:
            current_time += timedelta(seconds=1)  # Increment the internal clock
        time.sleep(1)


# Function to handle button inputs
def handle_button_input():
    global current_state, selected_game, alarm_time

    # Button handling logic
    button = get_button_input()
    if button == "left":  # Navigate left
        if current_state == IDLE:
            current_state = ALARM_SET_HOUR
        elif current_state == ALARM_SET_HOUR:
            current_state = ALARM_SET_MINUTE  # Switch to minute setting
        elif current_state == ALARM_SET_MINUTE:
            current_state = ALARM_SET_HOUR  # Switch to hour setting
        elif current_state == GAME_SET:
            selected_game = settings.edit_game_left(selected_game)  # Cycle left through game options
        elif current_state == TIME_SET_HOUR:
            current_state = TIME_SET_MINUTE  # Switch to minute setting
        elif current_state == TIME_SET_MINUTE:
            current_state = TIME_SET_HOUR  # Switch to hour setting
    elif button == "up":  # Increment
        if current_state == IDLE:
            current_state = GAME_SET
    elif button == "right":  # Navigate right
        if current_state == IDLE:
            current_state = TIME_SET_HOUR
        elif current_state == ALARM_SET_HOUR:
            current_state = ALARM_SET_MINUTE  # Switch to minute setting
        elif current_state == GAME_SET:
            selected_game = settings.edit_game_right(selected_game)  # Cycle right through game options
        elif current_state == TIME_SET_HOUR:
            current_state = TIME_SET_MINUTE  # Switch to minute setting
        elif current_state == TIME_SET_MINUTE:
            current_state = TIME_SET_HOUR  # Switch to hour setting
    elif button == "down":  # Decrement
        if current_state == IDLE:
            pass
    elif button == "center":  # Confirm/Select
        if current_state == IDLE:
            pass
        elif current_state == ALARM_SET_HOUR or current_state == ALARM_SET_MINUTE:
            current_state = IDLE  # Confirm the current setting
        elif current_state == GAME_SET:
            selected_game = settings.games[settings.index][1]  # Confirm the current setting
            current_state = IDLE
        elif current_state == TIME_SET_HOUR or current_state == TIME_SET_MINUTE:
            current_state = IDLE  # Confirm the current setting
    elif button == "demo":  # Start demo
        current_state = ALARM


# Alarm checker (runs in a thread)
def check_alarm():
    global current_state

    while True:
        with time_lock:
            now = current_time.strftime("%H%M")  # Use internal time
        if now == alarm_time and current_state == IDLE:
            current_state = ALARM
        time.sleep(1)


# Main state machine loop
def main_loop():
    global current_state, selected_game

    while True:
        if current_state == IDLE:
            # Display current time
            with time_lock:
                display_text(current_time.strftime("%H%M"))
        elif current_state == ALARM_SET_HOUR:
            pass
        elif current_state == ALARM_SET_MINUTE:
            pass
        elif current_state == GAME_SET:
            pass
        elif current_state == TIME_SET_HOUR:
            pass
        elif current_state == TIME_SET_MINUTE:
            pass
        elif current_state == ALARM:
            # Trigger alarm
            display_text("Wake Up!")
            current_state = GAME
        elif current_state == GAME:
            # Run the selected game
            run_game(selected_game)
            current_state = POST_ALARM
        elif current_state == POST_ALARM:
            # Resume idle state after alarm/game
            display_text("Good Morning!")
            time.sleep(3)  # Pause for a bit
            current_state = IDLE

        # Check for button input in every loop iteration
        handle_button_input()
        time.sleep(0.1)


# Run the selected game
def run_game(game_name):
    if game_name == "jumping_jack":
        jumping_jack.start_game()
    elif game_name == "memory_game":
        memory_game.start_game()
    elif game_name == "whackamole":
        whackamole.start_game()
    elif game_name == "math_game":
        math_game.start_game()
    elif game_name == "wake_n_shake":
        wake_n_shake.start_game()
    else:
        print(f"Unknown game: {game_name}")


# Getting button input
def get_button_input():
    if left.is_pressed:
        return "left"
    elif up.is_pressed:
        return "up"
    elif right.is_pressed:
        return "right"
    elif down.is_pressed:
        return "down"
    elif center.is_pressed:
        return "center"
    elif demo.is_pressed:
        return "demo"
    else:
        return None


# Main entry point
if __name__ == "__main__":
    # Start the alarm checker thread
    alarm_thread = threading.Thread(target=check_alarm, daemon=True)
    alarm_thread.start()

    # Start the internal clock thread
    clock_thread = threading.Thread(target=increment_internal_time, daemon=True)
    clock_thread.start()

    # Run the main state machine loop
    main_loop()
