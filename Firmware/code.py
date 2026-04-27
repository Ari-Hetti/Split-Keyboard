import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

split = Split(
    split_type=SplitType.BLE,
    data_pin=board.D0, 
    use_weighted_priority=True
)

encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.D19, board.D20, board.D6, False),)

keyboard.modules = [split, encoder_handler]

keyboard.col_gpios = (board.D1, board.D2, board.D3, board.D4, board.D5)
keyboard.row_gpios = (board.D10, board.D9, board.D8, board.D7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        #Left Side 
   
        KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,
        KC.A,    KC.S,    KC.D,    KC.F,    KC.G,
        KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,
        KC.NO,   KC.SPACE, KC.NO,   KC.NO,   KC.NO,
        
        #Right Side
        KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,
        KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN,
        KC.N,    KC.M,    KC.DOT,  KC.COMMA, KC.SLSH,
        KC.NO,   KC.NO,   KC.NO,   KC.SPACE,   KC.NO,
    ]
]

encoder_handler.map = [
    ((KC.VOLU, KC.VOLD, KC.MUTE),),
]

if __name__ == '__main__':
    keyboard.go()