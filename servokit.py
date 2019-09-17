
from app.ada_hid import Keyboard
from app.ada_hid import KeyboardLayoutUS
from app.keycode import Keycode
import time
time.sleep(2)
kbd = Keyboard()
layout = KeyboardLayoutUS(kbd)

# Type 'abc' followed by Enter (a newline).
kbd.press(Keycode.CONTROL, Keycode.ALT, Keycode.T,)
kbd.release_all()

kbd.press(Keycode.CONTROL, Keycode.ALT, Keycode.T,)
kbd.release_all()

kbd.press(Keycode.CONTROL, Keycode.ALT, Keycode.T,)
kbd.release_all()

# Get the keycodes needed to type a '$'.
# The method will return (Keycode.SHIFT, Keycode.FOUR).
keycodes = layout.keycodes('$')
print("done")