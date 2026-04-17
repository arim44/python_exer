#내장 함수
max_value = max(1,35,70)
print(max_value)

min_value = min(1,35,70)
print(min_value)
# 문자열은 아스키코드로 비교
max_str = max('AAC', 'ABC', 'ACC')
print(max_str)
min_str = min('AAC', 'ABC', 'ACC')
print(min_str)

length = len("안녕하세요")  #길이
print(length)

result = eval("10+20+30+40")
print(result)

result = eval("not 40>50")  #비교
print(result)

list = [2,5,5,3,9,1]
result = sorted(list)
print(result)

str1 = "안녕하세요"
str_id = id(str1)
print(str_id)
list_id = id([1,2,3,4,5])
print(hex(list_id))
print(oct(list_id))
print(type(3.14))
print(type([1,2,3,4,5]))
print(abs(-5))

# 내장 모듈 활용 - datetime

import datetime #import 키워드를 사용해서 모듈을 추가
#오늘 날짜
today = datetime.date.today()
print(today)
# 오늘 날짜, 시간
now = datetime.datetime.now()
print(now)

print(now.year)
print(now.month)
print(now.day)
dir(datetime)

import datetime as dt
today = dt.date.today()
print(today)

now = dt.datetime.now()
print(now)

know = now + dt.timedelta(hours=9)
print(know)

time_diff = know - now
print(time_diff)

from datetime import datetime, date
xmas1 = datetime(2023, 12, 25, 0, 0, 0)
print(xmas1)
xmas2 = date(2023, 12, 15)
print(xmas2)

#내장모듈 활용 - time
import time
print(time.time())

local_time = time.localtime(time.time())
str_time = time.strftime('%Y-%m-%d %H:%M:%S', local_time)
print(str_time)

#내장모듈 활용 - random
import random
print(random.random())          # 0~1미만의 실수 난수 발생
print(random.randrange(1,7))    #1~6까지의 정수 난수 발생
print(random.randint(1,7))      #1~7까지의 정수 난수 발생

list1 = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(list1)           # list의 아이템 순서를 바꿈
print(list1)
print(random.choice(list1))     # list의 아이템 중 하나를 임의로 선택
print(random.sample(list1, 5))  # list의 아이템 중 5개의 아이템을 임의로 선택

# 내장모듈 활용 - os
import os
dir(os)

print(os.sep)
cur_dir = os.getcwd() # 현재 작업경로
print(cur_dir)
test_dir = os.path.join(cur_dir, 'test')# 경로 생성
print(test_dir)
print(os.path.exists(test_dir)) #경로 유무
if not os.path.exists(test_dir):
    os.mkdir(test_dir) #디렉터리 생성
print(os.path.exists(test_dir))

#file 읽기
with open('test1.txt', 'r') as f:
    print(f.readline(), end="")
    print(f.readline(), end="")
    print(f.readline(), end="")
    print(f.readline(), end="")

with open('test1.txt','r', encoding='utf8') as f:
    texts = f.readline()
    for text in texts:
        if not text : break
        print(text, end='')

#file 쓰기
text = "안녕하세요.\n 파이썬입니다.\n 반갑습니다."
with open('test1.txt', 'w') as f:
    f.write(text)

# 예외 처리
# Try-except 0넣어보기
str1 = input("피젯수를 넣으세요 ")  # 나눔을 당하는 수
str2 = input("젯수를 넣으세요 ")    # 0넣어보기 나누는 순

# 함수로 해서 다시 입력받게 하는중
def inputStr():
    str1 = input("피젯수를 넣으세요 ")  # 나눔을 당하는 수
    str2 = input("젯수를 넣으세요 ")    # 0넣어보기 나누는 순

try:
    num1 = int(str1)
    num2 = int(str2)
    result = num1/num2
    print('{}/{}={}'.format(num1, num2, num1/num2))
#except:
    print('입력값을 확인하세요 ')
except Exception as e:  #에러 메시지 출력
    print("exception:", e)
except ValueError:      #숫자가 아닌 값이 매개변수로 전달될때 발생
    print('숫자를 입력하세요')
except ZeroDivisionError: #0으로 나눌때 발생
    print('0으로 나눌수 없습니다')
else:   #예외가 발생하지 않으면 실행
    print('{}/{}={}'.format(num1, num2, num1/num2))
finally:    #예외가 생겼어도 꼭 해야하는거
    print('처리가 완료 되었습니다.')

# 실습
# test11.txt 파일을 읽기모드로 여는데 예외가 발생했을때 
# '파일을 여는중 예외가 발생했습니다.' 라고 출력하는 코드를작성하시오.

try:
    with open('test11.txt','r') as f:
        text = f.read()
        print(text)
        print(f.readline(), end="")
except:
    print('파일을 여는중 예외가 발생했습니다.')

#람다(Lambda)
def add(x,y):
    return x+y

f = lambda x, y : x+y
print(add(1,2))
print(f(1,3))