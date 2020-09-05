import time
import random
import os

word_list = [
    "동해물과 백두산이 마르고 닳도록",
    "1 더하기 1은 2이다.",
    "10 * 10 + 20 = 120",
    "여름이었다.",
    "1886 이화여자대학교",
    "EWHA WOMEN UNIVERSITY",
    "사과, 배, 딸기, 수박, 참외"
]

random.shuffle(word_list)

for q in word_list :
    os.system("cls")
    start_time =time.time() #time.time() : 현재시각
    user_input = str(input(q + '\n')).strip()
    end_time = time.time() - start_time

    if user_input == "/exit" :
        break

    correct = 0
    for i, c in enumerate(user_input) :
        if i >=len(q) : #글자 수가 넘어가면 오류 뜸
            break
        if c == q[i] :
            correct += 1

    total_len = len(q) #문구의 총 길이
    c = correct / total_len * 100 #정확도
    e = (total_len - correct) / total_len * 100 #오타율
    speed = (correct / end_time) * 60 #속도

    print("속도 : {:0.2f} 정확도 : {} 오타율 : {}". format(speed, c, e))
    os.system("pause")
