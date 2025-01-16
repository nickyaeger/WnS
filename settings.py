import time
from datetime import datetime
from display import display_text


time = "0000"
alarm = "0000"
games = [["JUMP", "jumping_jack"],[ "MEMY", "memory_game"], ["MOLE", "whackamole"], ["MATH", "math_game"], ["SHAK", "wake_n_shake"]]
index = 0

def edit_alarm_hour(time: str):
    display_text(time[0] + time[1] + "  ", colon=1, colors=[(255, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0)])
    

def edit_alarm_minute(time: str):
    display_text("  " + time[3] + time[4], colon=1, colors=[(0, 0, 0), (0, 0, 0), (255, 0, 0), (255, 0, 0)])
    

def increment_alarm_hour(time: str):
    
    pass

def increment_alarm_minute(time: str):
    
    pass

def edit_game_left():
    index -= 1
    display_text(games[index][0])

def edit_game_right():
    index += 1
    display_text(games[index][0])
