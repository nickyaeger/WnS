# Wake 'N Shake - Smart Alarm Clock

A fun and interactive smart alarm clock for Raspberry Pi that wakes you up with engaging games and exercises. Instead of just buzzing, this alarm clock makes you complete a fun challenge to turn it off!

## Features

### Core Functionality
- **Customizable Alarm Time**: Set alarm hours and minutes using intuitive button controls
- **Internal Time Management**: Maintains accurate time tracking independent of system time
- **7-Segment LED Display**: Shows current time, settings, and game information
- **Multi-Game Selection**: Choose from 5 different wake-up games

### Wake-Up Games
1. **Jumping Jack** - Physical activity counter
2. **Memory Game** - Test your memory with sequence challenges
3. **Whack-a-Mole** - Quick reaction time game
4. **Wake 'N Shake** - Full-body movement challenge
5. **Push-up** - Push-up counter challenge

### Hardware Components
- **Button Interface**: 6 buttons (left, right, up, down, center, demo) with LED feedback
- **7-Segment Display**: 4-character display via I2C interface
- **Camera Integration**: Camera support for motion detection
- **Audio System**: Sound effects and voice feedback

## Hardware Requirements

- Raspberry Pi (tested on Pi 4/5)
- 7-segment LED display (I2C address 0x71)
- 6 buttons with corresponding LEDs:
  - GPIO Pin 22 (Left) → LED Pin 21
  - GPIO Pin 24 (Up) → LED Pin 23
  - GPIO Pin 32 (Right) → LED Pin 31
  - GPIO Pin 36 (Down) → LED Pin 35
  - GPIO Pin 38 (Center) → LED Pin 37
  - GPIO Pin 40 (Demo)
- Camera module
- Audio output system

## Installation

### Prerequisites
```bash
pip install RPi.GPIO
pip install smbus2
```

### Setup
1. Clone or download this project to your Raspberry Pi
2. Install required dependencies
3. Ensure GPIO is properly configured
4. Connect hardware components according to pin mapping

## Usage

### Starting the Alarm Clock
```bash
python main.py
```

### Button Controls
- **Left/Right**: Navigate settings or select options
- **Up/Down**: Increment/decrement values (hours, minutes, game selection)
- **Center**: Confirm selection or toggle states
- **Demo**: Trigger demo mode

### Operation States

| State | Description |
|-------|-------------|
| IDLE | Normal time display, waiting for input |
| ALARM_SET_HOUR | Setting alarm hour value |
| ALARM_SET_MINUTE | Setting alarm minute value |
| GAME_SET | Selecting wake-up game |
| TIME_SET_HOUR | Adjusting current hour |
| TIME_SET_MINUTE | Adjusting current minute |
| ALARM | Alarm triggered, game in progress |
| GAME | Running selected wake-up game |
| POST_ALARM | Post-alarm state |

## Project Structure

```
WnS/
├── main.py              # Main application logic and state machine
├── settings.py          # Settings management (time, alarm, game selection)
├── buttons.py           # GPIO button and LED control
├── display.py           # 7-segment display interface (I2C)
├── display_21_seg.py    # Alternative display driver
├── camera.py            # Camera integration module
├── sounds.py            # Audio playback and sound effects
├── games/               # Game modules
│   ├── jumping_jack.py
│   ├── memory_game.py
│   ├── whackamole.py
│   ├── math_game.py
│   ├── wake_n_shake.py
│   └── pushup.py
├── audio/               # Audio files for sounds and alerts
└── README.md            # This file
```

## Key Components

### Main Application (`main.py`)
- State machine managing alarm clock operation
- Thread-safe time tracking
- Event handling and game orchestration

### Settings (`settings.py`)
- Alarm time configuration
- Game selection menu
- Time adjustment functions

### Hardware Interface
- **buttons.py**: GPIO control for buttons and LEDs
- **display.py**: I2C communication with 7-segment display
- **camera.py**: Optional camera module integration

### Games (`games/`)
Each game module implements a specific wake-up challenge with:
- Game logic and rules
- User input handling
- Sound and visual feedback
- Completion detection

## Configuration

### I2C Display Address
Default I2C address is `0x71`. To verify your display address:
```bash
i2cdetect -y 1
```

### GPIO Pin Mapping
Edit the pin mappings in `buttons.py` if your hardware uses different pins:
```python
self.button_pins = {
    "left": 22,
    "up": 24,
    "right": 32,
    "down": 36,
    "center": 38,
    "demo": 40,
}
```

## Development Notes

- Thread-safe operations use locks for time management
- Non-blocking button input handling
- Game selection via menu interface
- Extensible game framework for adding new challenges

## Troubleshooting

### Display Not Showing
- Check I2C address: `i2cdetect -y 1`
- Verify I2C pins (GPIO 2 and 3 on Pi 4)
- Ensure smbus2 is installed

### Buttons Not Responding
- Verify GPIO pin configuration
- Check GPIO permissions: `sudo usermod -a -G gpio $USER`
- Test pins with `raspi-gpio` utility

### Audio Issues
- Check audio output configuration on Raspberry Pi
- Verify audio files exist in `audio/` directory
- Check volume settings