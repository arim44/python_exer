#타입
print(type(10))  #<class 'int'>
print(type(1.1))
s = 'Hello'
print(type(s))

#연산
print(2+3)
num=4
print(num)
num**=2
print(num)

#비교연산자
print(5<6)
print(11 != 5)

#비교, 논리 연산자
print(True or False)
print(not False)
print(5<6 and True)

#print 함수
print("Hello world")
age = 20
name = '홍길동'
print(name, age)
print('이름은', name, '나이는', age)
print('이름은 '+ name + '나이는 '+ str(age))

#string.format()
str1 = "{}".format(10)
print(str1)

str2 = "{}과 {}".format(10,20)
print(str2)

num1 = 10
num2 = 20
str3 = "{}x{}={}".format(num1, num2, num1*num2)
print(str3)

age = 20
name = '홍길동'

str4 = '이름은 {} 나이는 {}'.format(name, age)
print(str4)

str5 = '이름은 {0} 나이는 {1}'.format(name, age)
print(str5)
# s : string d 정수, f :float,
str7 = '이름은 {:s} 나이는 {:d}'.format(name, age)
print(str7)
print('pi = {:f}'.format(3.141592))
print('pi={:10f}'.format(3.141592))
print('pi={:5.2f}'.format(3.141592))
print('pi={:.2f}'.format(3.141592))

# string 서식지정자
print('이름은 %s 나이는 %d'%(name, age))
print('이름은 %s 나이는 %5d'%(name, age))   #전체가 5자리
print('이름은 %s 나이는 %05d'%(name, age))  #전체가 5자리인데 0으로 채움
print('pi = %f'%3.141592)               #pi = 3.141592
print('pi = %5.2f'%3.141592)            #pi =  3.14 전체가 5자리이고 소수점 이하 2자리
print('pi = %.2f'%3.141592)             #pi = 3.14 전체길이는 없고 소수점이하 2자리

#List
scores = [30,50,90,56,87]
score0 = scores[0]
print(score0)
#print(scores[5]) #에러
print(scores[-1])
print(scores[-3])

scores[1] = 100
print(scores)

scores.append(99)
scores.append('Hello')
print(scores)
 
scores.insert(1,33)
scores.insert(2, 'World')
print(scores)

#list 활용 (list는 +,* 연산자 사용가능)
list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9,10]

print(list1 + list2)
print(list2+list1)
print(list1 *3)
print(list2 *2)