# 나만의 단축키 만들기

from pynput.keyboard import Key, Listener, KeyCode
import win32api

#딕셔너리 {Key1:Value1, Key2:Value2, Key3:Value3, ...}
MY_HOT_KEYS = [
    {"function1" : {Key.ctrl_l, Key.alt_l, KeyCode(char="p")}}
    ]

#현재 누르고 있는 키보드를 저장하기 위한 집합
current_keys = set() #집합으로 표시하면 중복이 사라진다.

def function1() : #계산기 프로그램 실행
    print("함수 1 호출")
    win32api.WinExec("calc.exe") 

def key_pressed(key) :
    print("Pressed {}".format(key))
    for data in MY_HOT_KEYS :
        FUNCTION = list(data.keys())[0] #function1
        KEYS = list(data.values())[0] #{Key.ctrl_l, Key.alt_l, KeyCode(char="p")}

        if key in KEYS :
            current_keys.add(key)

            if all(k in current_keys for k in KEYS ) :
            # checker = True
            # for k  in KEYS :
            #     if k not in current_key : #모든 키가 눌리지 않았다면,
            #         checker = False
            #         break
            # if checker :
                function = eval(FUNCTION) #eval() : string 값을 넣으면 해당 값을 그대로 실행하여 결과를 출력
                function()

def Key_released(key) :
    print("Released {}".format(key))

    if key in current_keys : 
        current_keys.remove(key)

    #ESC를 누르면 종료
    if key == Key.esc : 
        return False 

with Listener(on_press = key_pressed, on_release = Key_released) as listener :
    listener.join()
#on_press : 키보드를 누르면 Key_pressed가 실행, on_release : 키보드를 떼면 Key_released가 실행