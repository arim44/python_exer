
#생성
dic1 = {}   #빈 딕셔너리 생성
print(dic1)

dic2 = dict()   # 생성자를 이용해서 딕셔너리 생성
print(dic2)

dic3 = {'name':'item', 1:3.5, False:[1,2,3]}
print(dic3)

#아이템 값 가져오기
student = {'name':'홍길동', 'major':'정통과','score':3.5}
print(student['name'])
print(student['score'])
scores = {1:3.5, 2:4.0, 3:4.3, 4:4.2}
print(scores[1])
print(scores[2])

#아이템 수정, 추가
student['major']='정보통신과'
print(student)
student['grade'] = 4
print(student)

scores[2] = '4.5'
print(scores)

#아이템 삭제
del student['name']
print(student)
del scores[1]
print(scores)

#Key, value 가져오기
student = {'name':'홍길동', 'major':'정통과', 'score':3.5}

print(list(student.items()))
print(list(student.keys()))
print(list(student.values()))

#packing, unpacking
nums = 1,2,3    #패킹
print(nums)
print(type(nums))
num1, num2, num3 = nums #언패킹
print(num1, num2, num3)

nums = [1,2,3,4,5]

*num1, num2, num3 = nums
print(num1, num2, num3)

nums = (6,7,8)
_,_,num3 = nums
print(num3)
#unpacking 시 Set : 키만 줌
student = {'name':'홍길동', 'major':'정보통신','grade':3}
a,b,c = student
print(a,b,c)
set1 = {1,2,3,4}
a, *b, c= set1
print(a,b,c)