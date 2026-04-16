# if 조건문
adult = 18
age = 17
if age < adult:
  print('당신은 미성년자입니다.')
  print('당신은 입장할 수 없습니다.')

#if~else
gender = 'female'
if gender == 'male' :
  print('당신은 남자입니다.')
else :
  print('당신은 남자가 아닙니다.')

#if~elif 하나만 체크 else if 와 같은 기능
score = 90
if score >= 90:
  result = 'A'
elif score >= 80:
  result = 'B'
elif score >= 70:
  result = 'C'
elif score >= 60:
  result = 'D'
else:
  result = 'F'
print(result)

#for ~ in
for i in range(10):
  print('Hello World')
for i in range(1,10):
  print("hello world!", i)
for i in range(10, 0, -1):
  print(i)

list1 = [1,2,3,4,5,6,7,8,9,10]
for num in list1:
    print(num)
fruits = ('apple', 'orange', 'grape')
for fruit in fruits:
    print(fruit)
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for num in tuple1:
    print(num)

#input 함수를 이용해서 입력받은 횟수만큼 반복
str_count = input('반복할 횟수를 입력하세요: ')
count = int(str_count)

for i in range(count):
    print("hello, world", i)

for i in range(10):
  for fruit in fruits:
    print(i, fruit)

# 구구단 출력
# 원하는 단수를 입력받아 for루프를 이용해서 출력하시요.
str_num = input("출력하고 싶은 단을 입력하세요: ")
dan = int(str_num)
# dan = int(input("출력하고 싶은 단을 입력하세요: "))

for i in range(1,10):
    print('{} x {} = {}'.format(dan, i, dan * i))

#전체 구구단 출력
for dan in range(2,10):
    for j in range(1,10):
        print('{} x {} = {}'.format(dan, j, dan * j))

#홀수 출력
# for루프, continue, %(나머지 연산자)를 이용해서 0~10 사이의 홀수를 출력하라.
for num in range(0,10):
    result = num % 2
    if result == 0:
      continue
    print(result)

#packing, unpacking
nums = 1,2,3
print(nums)
print(type(nums))
num1, num2, num3 = nums
