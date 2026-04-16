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
