import time
import ctypes

MOUSEEVENTF_LEFTDOWN = 0x02
MOUSEEVENTF_LEFTUP = 0x04
user32 = ctypes.windll.user32
is_mouse_down = False
mouse_down_time = None

while True:
    if user32.GetKeyState(0x01) & 0x8000:
        if not is_mouse_down:
            is_mouse_down = True
            mouse_down_time = time.time()
        else:
            duration = time.time() - mouse_down_time
            if duration > 0.1:  # 300 milliseconds
                user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
                is_mouse_down = False
    else:
        is_mouse_down = False
    time.sleep(0.01)
