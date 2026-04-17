#ramdom 모듈을 이용해서 두 가지 방법으로 lotto 발생 함수를 만드시오.
#2,3번

import random


# 2. shuffle 함수를 이용
lotteList = list(range(1,46))   #1~45까지의 숫자 생성
random.shuffle(lotteList)       #리스트안의 값 섞기
result = lotteList[0:6]         #인덱스 0번부터 6자리까지 가져와 넣기
result.sort()                   #오름차순 정렬
print(result)

# 3. sample 함수를 이용
lotteList1 = list(range(1,46))
result = random.sample(lotteList1)
result.sort()
print(result)