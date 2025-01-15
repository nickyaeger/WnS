import rpi_ws281x as ws # type: ignore

# LED configuration
LED_COUNT = 90
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0

# LED strip configuration
strip = ws.PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

#Valid characters
characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/']

# LEDs for each character
A = [2,3,5,8,9,13,14,18,19,20,21]
B = [1,2,3,6,7,8,9,13,14,18,19,20,21]
C = [1,2,3,4,5,6,7,8,9,18]
D = [1,2,3,6,7,8,9,13,14,18]
E = [1,2,3,4,5,6,7,8,9,18,19,21]
F = [1,2,3,4,8,9,18,19,20,21]
G = [1,2,3,4,6,7,8,9,14,18,20,21]
H = [1,4,5,8,9,13,14,18,19,20,21]
I = [2,3,6,7,11,16,21]
J = [2,3,4,6,7,13,14,18]
K = [1,4,5,8,9,12,15,18,19,21]
L = [1,2,5,6,7,8,9,18]
M = [1,4,5,8,9,10,12,13,14,18,21]
N = [1,4,5,8,9,10,13,14,15,18,21]
O = [2,3,6,7,9,13,14,18]
P = [1,2,3,8,9,13,18,19,20,21]
Q = [2,3,5,6,7,9,13,14,15,18]
R = [1,2,3,5,8,9,13,15,18,19,20,21]
S = [2,3,4,6,7,8,9,14,19,20,21]
T = [1,2,3,4,6,7,11,16,21]
U = [1,4,6,7,9,13,14,18]
V = [1,4,8,9,12,17,18,21]
W = [1,4,5,8,9,13,14,15,17,18,21]
X = [1,4,5,8,10,12,15,17,21]
Y = [1,4,10,12,16,21]
Z = [1,2,3,4,5,6,7,8,12,17,21]
ZERO = [2,3,6,7,9,12,13,14,17,18,21]
ONE = [2,6,7,11,16,21]
TWO = [2,3,6,7,13,18,19,20,21]
THREE = [2,3,6,7,13,14,19,20,21]
FOUR = [9,11,16,19,20,21]
FIVE = [2,3,6,7,9,14,19,20,21]
SIX = [2,3,6,7,9,14,18,19,20,21]
SEVEN = [2,3,12,17,21]
EIGHT = [2,3,6,7,9,13,14,18,19,20,21]
NINE = [2,3,6,7,9,13,14,19,20,21]
PLUS = [11,16,19,20,21]
MINUS = [19,20,21]
TIMES = [10,11,12,15,16,17,19,20,21]
DIVIDE = [4,8,12,17,21]

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def display_text(text: str, colon: int, leds: list) -> None:
    """Displays the given text on the LED strip.

    Parameters
    ----------
    text : str
        The text to display. Must be 4 characters long. Use whitespace to turn off a slot, and use underscore to keep a slot unchanged.
    colon : int
        Whether to display the colon. 0 for off, 1 for on, 2 for unchanged.
    leds : list
        The state of each LED. 0 for off, 1 for on, 2 for unchanged. Must be 4 elements long.
    """
    if len(text) != 4:
        raise ValueError("Text must be 4 characters long")
    chars = list(text)
    for i in range(4):
        if chars[i] not in characters:
            raise ValueError("Invalid character")
        if chars[i] == '_':
            continue
        if chars[i] == ' ':
            for j in range(21):
                strip.setPixelColor((i+1)*j, BLACK)
            continue
        
        if chars[i] == 'A':
            for j in A:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == 'B':
            for j in B:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == 'C':
            for j in C:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == 'D':
            for j in D:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == 'E':
            for j in E:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == 'F':
            for j in F:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == 'G':
            for j in G:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == 'H':
            for j in H:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == 'I':
            for j in I:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == 'J':
            for j in J:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == 'K':
            for j in K:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == 'L':
            for j in L:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == 'M':
            for j in M:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == 'N':
            for j in N:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == 'O':
            for j in O:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == 'P':
            for j in P:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == 'Q':
            for j in Q:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == 'R':
            for j in R:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == 'S':
            for j in S:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == 'T':
            for j in T:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == 'U':
            for j in U:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == 'V':
            for j in V:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == 'W':
            for j in W:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == 'X':
            for j in X:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == 'Y':
            for j in Y:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == 'Z':
            for j in Z:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == '0':
            for j in ZERO:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == '1':
            for j in ONE:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == '2':
            for j in TWO:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == '3':
            for j in THREE:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == '4':
            for j in FOUR:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == '5':
            for j in FIVE:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == '6':
            for j in SIX:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == '7':
            for j in SEVEN:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == '8':
            for j in EIGHT:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == '9':
            for j in NINE:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == '+':
            for j in PLUS:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == '-':
            for j in MINUS:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == '*':
            for j in TIMES:
                strip.setPixelColor((i+1)*j, WHITE)
        elif chars[i] == '/':
            for j in DIVIDE:
                strip.setPixelColor((i+1)*j, WHITE)

    if colon == 0:
        strip.setPixelColor(88, BLACK)
        strip.setPixelColor(89, BLACK)
    elif colon == 1:
        strip.setPixelColor(88, WHITE)
        strip.setPixelColor(89, WHITE)
    for i in range(4):
        if leds[i] == 0:
            strip.setPixelColor(i+86, BLACK)
        elif leds[i] == 1:
            strip.setPixelColor(i+86, WHITE)
    ws.show()
