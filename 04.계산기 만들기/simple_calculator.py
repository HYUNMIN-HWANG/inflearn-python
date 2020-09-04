import os

while True : 
    os.system("cls")
    s = input ("계산식 입력 >")
    print("결과 : {}".format(eval(s))) #eval : 스트링을 계산 가능한 식으로 만들어준다.
    os.system("pause") #아무키나 누르세요.
