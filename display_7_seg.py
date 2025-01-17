#Valid characters
characters = ['_',' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/']

def display_text(
    text: str,
    colon: int = 0,
    leds: list = [0, 0, 0, 0],
    colors: list = [(255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255)]
) -> None:
    """Simulates displaying the given text on the LED strip by printing inputs and expected operations."""
    if len(text) != 4:
        raise ValueError("Text must be 4 characters long")

    print(f"Input Text: {text}")
    print(f"Colon State: {colon} (0: Off, 1: On, 2: Unchanged)")
    print(f"LED States: {leds} (0: Off, 1: On, 2: Unchanged)")
    print(f"Character Colors: {colors}")
    
    chars = list(text)
    for i in range(4):
        if chars[i] not in characters:
            raise ValueError(f"Invalid character: {chars[i]}")
        if chars[i] == '_':
            print(f"Character {i + 1}: Unchanged")
            continue
        if chars[i] == ' ':
            print(f"Character {i + 1}: Turned off")
            continue

        print(f"Character {i + 1}: {chars[i]}, Color: {colors[i]}")

    if colon == 0:
        print("Colon: Turned off")
    elif colon == 1:
        print("Colon: Turned on")
    elif colon == 2:
        print("Colon: Unchanged")

    for i, led in enumerate(leds):
        if led == 0:
            print(f"LED {i + 1}: Turned off")
        elif led == 1:
            print(f"LED {i + 1}: Turned on")
        elif led == 2:
            print(f"LED {i + 1}: Unchanged")

    print("Simulated LED strip update complete.")

# Example usage
display_text("TEST", colon=1, leds=[1, 0, 2, 1], colors=[(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)])
