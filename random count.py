import random
import os

def input_check(msg, casting=int):
    while True :
        try : #실행할 코드
            user_input = casting(input("무슨 숫자일까요?"))
            return user_input
        except : #예외가 발생했을 때 실행
            continue

chance = 10
count = 0

number = random.randint(1, 99) #1과 99사이의 랜덤 정수를 리턴한다.
os.system("cls") #python console의 내용을 지운다.

print("1부터 99까지의 숫자를 10번 안에 맞춰 보세요.")

while count < chance :
    count += 1
    user_input = input_check("무슨 숫자일까요?")

    if number == user_input :
        break
    elif user_input < number :
        print("{}보다 큰 숫자 입니다.".format(user_input))
    elif user_input > number :
        print("{}보다 작은 숫자 입다.".format(user_input))

if user_input == number :
    print("성공! {} 이 맞습니다.".format(number))
else :
    print("실패! 정답은 {}입니다.".format(number))