'''
1. 특정 숫자를 포함해서 로또 번호를 생성해주는 기능
2. 특정 숫자를 제외해서 로또 번호를 생성해주는 기능
3. 정해진 자릿수만큼 연속 숫자를 포함하는 번호를 생성하는 기능
'''

#numpy : 과학 계산을 위한 라이브러리 (numpy 설치 후 사용 가능 > pip install numpy )
import numpy 

'''
*args : 키워드 되지않은 가변 갯수의 인자(수가 얼마가 될 지 모른다.)들을 함수에 보낼 때 사용
**kwargs : 키워드된 가변 갯수의 인자들을 함수에 보낼 때 사용, 함수가 이름이 지정된 인자를 처리할 때 사용, 특정 값 형태로 함수를 호출할 수 있다.
'''

def make_lotto_number(**kwargs) : 
    #1부터 46까지의 숫자 중 6개의 숫자를 중복되지 않게 선택해라. # choice() : 원소 하나를 선택하는 함수
    rand_number = numpy.random.choice(range(1,46), 6, replace=False) 
    rand_number.sort() #오름차순 정렬

    #최종 로또 번호가 완성될 변수
    lotto = []

    #1. 어떤 숫자를 꼭 포함하고 싶을 때
    if kwargs.get("include") : #kawrgs.get(key[]) : key가 있으면 값을 반환한다.
        include = kwargs.get("include")
        lotto.extend(include)

        cnt_make = 6 - len(lotto) #include된 숫자를 제외하고 랜덤으로 로또 숫자를 뽑을 개수 

        for _ in range (cnt_make) : # _(언더바)는 실제 인코딩을 할 때 변수를 사용하지 않고 돌아갈 때 변수 대신 사용한다.
            for j in rand_number : #랜덤으로 생성한 rand_number가 lotto 번호에 있는가?
                if lotto.count(j) == 0 : #lotto 리스트에 j의 개수를 구한다. 똑같은 값이 없다면 그대로 append한다.
                    lotto.append(j)
                    break
    else :
        lotto.extend(rand_number) 

    #2. 어떤 숫자를 제외하고 싶을 때
    if kwargs.get("exclude") :
        exclude = kwargs.get("exclude")
        lotto = list(set(lotto) - set(exclude)) #set : 집합 자료형, 파이썬에서의 집합은 중복을 허용하지 않는다. 순서가 없다. 
        #차집합 : 로또 리스트에 있는 숫자 중에서 exclude에 있는 숫자를 삭제한다.

        while len(lotto) != 6 :
            for _ in range (6 - len(lotto)) :
                rand_number = numpy.random.choice(range(1,46), 6, replace=False)
                rand_number.sort()

                for j in rand_number :
                    if lotto.count(j) == 0 and j not in exclude :
                        lotto.append(j)
                        break

    #3. 정해진 자릿수만큼 연속 숫자를 포함하고 싶을 때 
    if kwargs.get("continuty") :
        continuty = kwargs.get("continuty")
        start_number = numpy.random.choice(lotto, 1) #lotto에 있는 숫자 하나를 스타트 넘버로 정함

        seq_num  = [] #연속 숫자를 저장할 리스트
        for i in range(start_number[0], start_number[0] + continuty) : #스타트 숫자부터 continuty 개수만큼 숫자 반복
            seq_num.append(i)
        seq_num.sort()

        cnt_make = 6 - len(seq_num)

        lotto = [] #lotto 리스트 초기화
        lotto.extend(seq_num)

        while len(lotto) != 6 :
            for _ in range(6 - len(lotto)) :
                rand_number = numpy.random.choice(range(1,46), 6, replace=False)
                rand_number.sort()

                for j in rand_number :
                    if lotto.count(j) == 0 and j not in seq_num :
                        lotto.append(j)
                        break

                lotto = list(set(lotto)) #중복이 없어야 한다.

    lotto.sort()
    return lotto       

print(make_lotto_number(include=[5, 10])) #5와 10을 무조건 포함
print(make_lotto_number(exclude=[2, 3])) #2와 3은 무조건 제외
print(make_lotto_number(continuty=3)) #연속되는 세자리 숫자 포함