import random

#한글 키과 영어 값으로 구성된 딕셔너리
words_dic = { 
    "사자": "lion",
    "호랑이": "tiger",
    "사과": "apple",
    "비행기": "airplane"
}

words = []

#딕셔너리에 있는 단어들을 words 리스트에 랜덤으로 섞는다.
for word in words_dic : 
    words.append(word)
random.shuffle(words)


chance = 3 #기회는 세 번
#딕셔너리에 있는 단어 모두 한 번씩 출력
for i in range(0, len(words)) :
    q = words[i] #리스트에 있는 한 단어

    for j in range (0, chance) :
        user_input = str(input("{} 의 영어 단어를 입력하세요.>".format(q)))
        english = words_dic[q] #q 자리에 있는 영어 단어가 저장된다.

        if user_input.strip().lower() == english.lower() :
            print("정답입니다.")
            break 
        else :
            print("틀렸습니다.")
    if user_input != english :
        print("정답은 {} 입니다.".format(english))
print("문제가 더이상 없습니다.")