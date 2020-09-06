import random

count = int(input("로또 번호를 몇 개 생성할까요? > "))
for j in range (count) :
    lotto = []
    random_num = random.randint (1,46)

    for i in range (6) :
        while random_num in lotto :
            random_num = random.randint(1,46) #랜덤으로 나온 숫자가 이미 리스트에 있다면 다시 랜덤으로 숫자를 돌린다.
        lotto.append(random_num)

    lotto.sort() #오름차순 정렬

    print("{} 로또번호 : {}".format(j, lotto))