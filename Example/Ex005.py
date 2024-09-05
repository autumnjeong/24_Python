# score = int(input("점수 입력 : "))
#
# result:str = ''
#
# if score > 90 :
#     result = 'A'
# elif score > 80 :
#     result = 'B'
# elif score > 70 :
#     result = 'C'
# elif score > 60 :
#     result = 'D'
# else :
#     result = 'F'
#
# print(f'Your grade is {result}.')

print('기능 선택')
print('1. 더하기')
print('2. 빼기')
print('3. 곱하기')
print('4. 나누기')
print()

s = int(input('기능을 선택하세요 : '))
print()

num1 = int(input('첫번째 숫자를 입력하세요 : '))
num2 = int(input('두번째 숫자를 입력하세요 : '))
print()

result:int = 0

if s == 1 :
    result = num1 + num2
elif s == 2 :
    result = num1 - num2
elif s == 3 :
    result = num1 * num2
elif s == 4 :
    result = num1 % num2

print(f'계산한 값 : {result}')