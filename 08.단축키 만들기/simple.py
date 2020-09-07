# 키보드는 누르는 이벤트 & 떼는 이벤트 두 개로 이루어져 있다.

from pynput.keyboard import Key, Listener, KeyCode

def key_pressed(key) :
    print("Pressed {}". format(key))

def Key_released(key) :
    print("Released {}". format(key))

    #ESC를 누르면 종료
    if key == Key.esc : 
        return False 

with Listener(on_press = key_pressed, on_release = Key_released) as listener :
    listener.join()
