"""Contains the functions that are used to edit the time, alarm, and game settings."""
from display_7_seg import display_text

time = 0
alarm = 0
games = [["JUMP", "jumping_jack"],[ "MEMY", "memory_game"], ["MOLE", "whackamole"], ["MATH", "math_game"], ["SHAK", "wake_n_shake"], ["PUSH", "pushup"]]
index = 0

def increment_alarm_hour():
    global alarm
    if alarm >= 2300:
        alarm -= 2300
    else:
        alarm += 100
    print("Alarm: ", alarm)

def increment_alarm_minute():
    global alarm
    if alarm % 100 == 59:
        alarm -= 59
        increment_alarm_hour()
    else:
        alarm += 1
    print("Alarm: ", alarm)

def decrement_alarm_hour():
    global alarm
    if alarm <= 100:
        alarm += 2300
    else:
        alarm -= 100
    print("Alarm: ", alarm)

def decrement_alarm_minute():
    global alarm
    if alarm % 100 == 0:
        alarm += 59
        decrement_alarm_hour()
    else:
        alarm -= 1
    print("Alarm: ", alarm)

def edit_game_left():
    global index, games
    if index == 0:
        index = len(games) - 1
    else:
        index -= 1
    display_text(games[index][0])
    print("Selected game: ", games[index][1])
    return games[index][1]

def edit_game_right():
    global index, games
    if index == len(games) - 1:
        index = 0
    else:
        index += 1
    display_text(games[index][0])
    print("Selected game: ", games[index][1])
    return games[index][1]

def increment_time_hour():
    global time
    if time >= 2300:
        time -= 2300
    else:
        time += 100
    print("Time: ", time)

def increment_time_minute():
    global time
    if time % 100 == 59:
        time -= 59
        increment_time_hour()
    else:
        time += 1
    print("Time: ", time)

def decrement_time_hour():
    global time
    if time < 100:
        time += 2300
    else:
        time -= 100
    print("Time: ", time)

def decrement_time_minute():
    global time
    if time % 100 == 0:
        time += 59
        decrement_time_hour()
    else:
        time -= 1
    print("Time: ", time)
    