import random
import os

numbers = [] # 숫자 세자리를 담을 리스트
number = str(random.randint(0,9))

for i in range(3): 
    while number in numbers :
        number = str(random.randint(0,9)) #리스트에 똑같은 숫자가 있으면 새로운 숫자를 생성
    numbers.append(number) #리스트에 중복되지 않은 수가 있을 때 number를 추가한다.

os.system("cls")

count_strike = 0
count_ball = 0

while count_strike < 3 :          
    count_strike = 0
    count_ball = 0
    num = str(input("숫자 3자리를 입력하세요 >> ")) #사용자가 입력한 세자리 값
    if len(num) == 3 :
        for i in range (0,3) : #사용자가 입력한 값과
            for j in range (0,3) : #컴퓨터가 생성한 값을 비교
                if num[i] == numbers[j] and i == j : #숫자도 같고, 자리도 같을 때
                    count_strike += 1
                elif num[i] == numbers[j] and i != j : #숫자는 같은데, 자리가 다를 때
                    count_ball += 1   
        if count_strike == 0 and count_ball == 0:
            print( "3 아웃!")
        else :
            output = ""
            if count_strike > 0 :
                output += "{} 스트라이크".format(count_strike)
            if count_ball >0:
                output += "{} 볼".format(count_ball)
            print(output.strip())
print("게임성공")
