#초성, 중성, 종성으로 분리하여 타이핑

import time
import random
import os

'''
한글을 '초성, 중성, 종성'으로 분리하기 위한 식
한글 = ((초성 * 21) + 중성) * 28 +종성 + 44032
    # 44032 : 유니코드 '가'를 10진수로 변환한 값
초성 = ((x-44032) / 28) /21 #초성에 대한 인덱스가 나온다.
중성 = ((x-44032) / 28) % 21 #중성 인덱스
종성 = (x-44032) % 28 #종성 인덱스
'''

#초성 19개
cho = ["ㄱ","ㄲ","ㄴ","ㄷ","ㄸ","ㄹ","ㅁ","ㅂ","ㅃ","ㅅ","ㅆ","ㅇ","ㅈ","ㅉ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"]
#중성 21개
jung = ["ㅏ","ㅐ","ㅑ","ㅒ","ㅓ","ㅔ","ㅕ","ㅖ","ㅗ","ㅘ","ㅙ","ㅚ","ㅛ","ㅜ","ㅝ","ㅞ","ㅟ","ㅠ","ㅡ","ㅢ","ㅣ"]
#종성 28개
jong = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

#한글을 초성, 중성, 종성으로 분리하는 함수 만들기
def break_korean(string) :
    word_list = str(string)
    break_word = []

    for k in word_list :
        if ord(k) >= ord("가") and ord(k) <= ord("힣") : #한글 아스키코드 "가"에서부터 "힣"까지 있다.
            #유니코드 상 몇 번째 글자인지 인덱스를 구합니다.
            char_index = ord(k) - ord('가')

            #초성 = (유니코드인덱스 / 28) /21 #초성에 대한 인덱스가 나온다.
            char1 = int((char_index / 28) /21)
            break_word.append(cho[char1])

            #중성 = (유니코드인덱스 / 28) % 21
            char2 = int((char_index / 28) % 21)
            break_word.append(jung[char2])

            #종성 = 유니코드인덱스 % 28
            char3 = int(char_index % 28)

            #종성(받침)이 있는 경우에만 종성 추가
            if char3 > 0 :
                break_word.append(jong[char3])

        else : #정상적인 한글이 아닌 경우
            break_word.append(k)
    return break_word

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

    src = break_korean(q) #주어진 문장을 초성, 중성, 종성 분리
    tar = break_korean(user_input) #입력된 문장을 초성, 중성, 종성 분리


    if user_input == "/exit" :
        break

    correct = 0
    for i, c in enumerate(tar) :
        if i >=len(src) : #글자 수가 넘어가면 오류 뜸
            break
        if c == src[i] :
            correct += 1

    total_len = len(src) #문구의 총 길이
    c = correct / total_len * 100 #정확도
    e = (total_len - correct) / total_len * 100 #오타율
    speed = (correct / end_time) * 60 #속도

    print("속도 : {:0.2f} 정확도 : {} 오타율 : {}". format(speed, c, e))
    os.system("pause")