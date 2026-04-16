# 함수 정의
def hello():
    print("hello world")

hello(); # 호츌

#가변 매개변수
def hello4(greeting, *names):
    for name in names:
        print(greeting, name)
hello4('안녕', "진", "슈가","RM")

#호출시 매개변수명을 사용
def function(first, second, third):
    return first+second+third

print(function(3,5,7))
print(function(second = 3, first = 5, third = 7))