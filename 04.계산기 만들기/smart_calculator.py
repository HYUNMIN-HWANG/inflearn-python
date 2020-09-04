import os

operator = ["+","-","*","/","="] #사용할 수 있는 연산자 종류

def string_calculator(user_input, show_history=False) : #계산기 함수 만들기
    string_list = [] #사용자가 입력한 숫자와 연산자를 하나 씩 저장할 리스트
    lop = 0  # 마지막 연산자를 기억하는 변수

    if user_input[-1] not in operator : #사용자가 입력한 문자열의 마지막 글자에 오프레이터가 없을 때,
        user_input += "=" #맨 마지막에 임의로 =를 넣는다.

    for i,s in enumerate(user_input) : #i번째 인덱스 번호, s에 값을 변환
        if s in operator : #연산자인 경우에
            if user_input[lop:i].strip() != "": #연산자 전까지의 내용이 공백이 아니라면
                string_list.append(user_input[lop:i]) #유저 인풋의 lop에서부터 i까지를 잘라서 리스트에 추가한다.
                string_list.append(s) #오퍼레이터를 리스트에 추가한다.
                lop = i + 1
    string_list = string_list[:-1] #맨 마지막에 있는 "="를 없앤다.

    pos = 0
    while True :
        if pos + 1 > len(string_list) :
            break
        if len(string_list) > pos + 1 and string_list[pos] in operator : #오퍼레이터를 기준으로
            temp = string_list[pos-1] + string_list[pos] + string_list[pos+1] #오퍼레이터 앞과 오퍼레이트 뒤의 값을 계산한다.
            del string_list[0:3] #  계산한 숫자와 연산을 지운다.
            string_list.insert(0,str(eval(temp))) #지워진 자리에 계산한 값을 넣는다.
            pos = 0
            if show_history : 
                print(string_list)
        pos += 1 #연산자가 아니라면 위치 +1
      
    if len(string_list) > 0 :
        result = float(string_list[0]) 
        
    return round(result,4) #소수점 4째자리까지 출력

while True :
    os.system("cls")
    user_input = input("계산식을 입력하세요.")
    if user_input == "/exit" :
        break
    result = string_calculator(user_input, show_history=True)
    print("결과 : {}".format(result))
    os.system("pause")