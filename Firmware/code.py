import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.macros import Macros
from kmk.extensions.media_keys import MediaKeys
from kb import data_pin
from kmk.modules.split import Split, SplitType, SplitSide

keyboard = KMKKeyboard()

## Still in Testing - not sure if this is the right way to do it, but we need to add the split module before the layers and macros
split = Split(split_type=SplitType.BLE, split_side=SplitSide.LEFT)
OR
split = Split(split_type=SplitType.BLE, split_side=SplitSide.RIGHT)

split = Split(
    split_flip=False,  # If both halves are the same, but flipped, set this True
    split_side=None,  # Sets if this is to SplitSide.LEFT or SplitSide.RIGHT, or use EE hands
    split_type=SplitType.UART,  # Defaults to UART
    split_target_left=True,  # Assumes that left will be the one on USB. Set to False if it will be the right
    uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
    data_pin=None,  # The primary data pin to talk to the secondary device with
    data_pin2=None,  # Second uart pin to allow 2 way communication
    uart_flip=True,  # Reverses the RX and TX pins if both are provided
    use_pio=False,  # Use RP2040 PIO implementation of UART. Required if you want to use other pins than RX/TX
    add_buttons = 0 # add single-pin buttons, rotary encoder actions, etc. per-side.
)

keyboard.modules.append(split)
keyboard.modules.append(split)
keyboard.modules.append(Layers())
keyboard.modules.append(Macros())
keyboard.extensions.append(MediaKeys())

keyboard.col_gpios = (board.D1, board.D2, board.D3, board.D4, board.D5)
keyboard.row_gpios = (board.D10, board.D9, board.D8, board.D7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

LAYERTOGGLE = KC.TG(1)
WINLOCK = KC.RGUI(KC.L)
PRINT = KC.MACRO("System.out.println();")
MUTE = KC.MUTE

keyboard.keymap = [
    [
        KC.Q,  KC.W, KC.E, R, KC.T,
        KC.A,  KC.S,  KC.D, KC.F, KC.G,
        KC.Z,  KC.X,  KC.C, KC.V, KC.B,
        KC.SPACE,
    ],
    [
        KC.Y,  KC.U, KC.I, KC.O, KC.P,
        KC.H,  KC.J,  KC.K, KC.L, KC.SCOLON,
        KC.N,  KC.M,  KC.DOT, KC.COMMA, KC.SLASH,
        KC.SPACE,
    ],
]

if __name__ == '__main__':
    keyboard.go()