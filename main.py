import time
import threading
from datetime import datetime
from games import jumping_jack, memory_game, whackamole, math_game
from display import display_text

# Define states
IDLE = "idle"
SETTINGS = "settings"
ALARM = "alarm"
GAME = "game"
POST_ALARM = "post_alarm"

# Global variables
current_state = IDLE
alarm_time = "07:00"
selected_game = "jumping_jack"
button_input = None  # This will hold the current button action


# Function to handle button inputs
def handle_button_input():
    global current_state, selected_game, alarm_time

    # Example button handling logic (adjust for your setup)
    button = get_button_input()  # Replace with your button input function
    if button == "button1":  # Navigate
        if current_state == SETTINGS:
            # Cycle through settings options (time, alarm, game)
            pass
    elif button == "button2":  # Increment
        if current_state == SETTINGS:
            # Increment values like hour, minute, or game selection
            pass
    elif button == "button3":  # Confirm/Select
        if current_state == SETTINGS:
            # Confirm the current setting
            pass


# Alarm checker (runs in a thread)
def check_alarm():
    global current_state

    while True:
        now = datetime.now().strftime("%H:%M")
        if now == alarm_time and current_state == IDLE:
            current_state = ALARM
        time.sleep(1)


# Main state machine loop
def main_loop():
    global current_state, selected_game

    while True:
        if current_state == IDLE:
            # Display current time
            display_text()
        elif current_state == SETTINGS:
            # Display settings options and allow changes
            display_text("Settings")
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
    else:
        print(f"Unknown game: {game_name}")


# Mock function for getting button input
def get_button_input():
    # Replace this with actual GPIO/button handling logic
    return None


# Main entry point
if __name__ == "__main__":
    # Start the alarm checker thread
    alarm_thread = threading.Thread(target=check_alarm, daemon=True)
    alarm_thread.start()

    # Run the main state machine loop
    main_loop()
