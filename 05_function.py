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

def function1(first=1, second = 3, third=5):
    return first+second+third
print(function1(first=2, third=3))

def function2(first, second, third=5):
    return first+second+third
print(function2(second= 5, first=2))
print(function2(1, second = 3))

#반환형이 콜렉션일때 unpacking
def function():
    return 1, "Hello", True

a,b,c = function()  # 언패킹
print(a,b,c)
a = function()
print(a)
print(type(a))  #반환형 타입 튜플


#리스트를 반환했을떄
def ret_list():
    return [1,2]
l = ret_list()
print(l)
n1, _ = ret_list()
print(n1)

# 실습_피젯수와 젯수(정수형)
# 두수를 입력받아 몫과 나머지를 튜플로 반환
num1 = int(input('첫번째 정수를 1개입력하세요: '))
num2 = int(input('첫번째 정수를 1개입력하세요: '))

def divide( num1, num2):
    q = num1 // num2
    r = num1 % num2
    return (q,r)

t = divide(10,2)
print(t)

s = divide(num1, num2)
print(s)

