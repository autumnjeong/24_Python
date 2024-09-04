"""
조건문
if
"""
# 만약 점수가 80점 이상이면 합격이고 80점 미만이면 불합격이다
x = int(input('점수를 입력하세요 : '))

if x>=80 :
    print('합격')
else :
    print('불합격')

# 만약 나이가 65세 이상일 경우에는 입장료가 무료이다
age = int(input('나이를 입력하세요 : '))

if age >= 65 :
    print('입장료가 무료입니다')
else :
    print('입장료가 부과됩니다')

#주민번호 앞자리가 3이면 남성이다
y = int(input('주민등록번호 뒷자리의 젓 자리를 입력하세요 : '))

if y == 3 :
    print('남성입니다')
elif y == 4 :
    print('여성입니다')

# 비밀번호가 맞으면 로그인된다
pw = int(input('비밀번호 다섯 자리를 입력하세요 : '))

if pw == 12345 :
    print("로그인 되었습니다")
else :
    print('로그인 실패하셨습니다')




# """
# 논리 연산자
# and, or, not
# """
#
# # and 논리연산자
# pilgi = 85
# silgi = 90
#
# pilgi >= 80 and silgi >= 80
#
# silgi = 70
# pilgi >= 80 and silgi >= 80
#
# # or 논리연산자
# x = 20
# x % 2 == 0 or x % 3 == 0
#
# x = 11
# x % 2 == 0 or x % 3 == 0
#
# # not 논리연산자
# x = 10
# not x == 10
#
# x = 5
# not x % 2 == 0
