# colors: list = ['black', 'white', 'red', 'blue']
# print(colors[0]) #get
# colors[0] = 'yellow' #set (write)
# print(colors[0]) #get (read)
# print(colors)
# for i in colors:
#     print(i)
# # [:] -> slice operator
# slice_colors = colors[1:]
# print(slice_colors)
# numbers = list(range(0, 1001))
# print(numbers)
# #list(range(0, 10)) #0 ~ 9

# v = [1, 2, 3]
# V = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# print(V[0][0], V[0][1], V[0][2],
#       V[1][0], V[1][1], V[1][2],
#       V[2][0], V[2][1], V[2][2])
# print(V[0], V[1], V[2])
#
# values1 = V[0][0]  # get = read
# print(values1)
# values1 = V[0]  # scalar
# print(values1)  # 리스트 타입
#
# for i in range(0, 3): #row
#     for j in range(0, 3): #column
#         scalar = V[i][j]
#         print(scalar, end="\t")
#     print()
#
# animals = ['사자', '토끼', '하이에나', '기린']
# index = 0
# size = len(animals)
# while index < size:
#     print(animals[index])
#     index += 1

questions = ['tr_in', 'b_s', '_axi', 'ari_lane']
answers = ['a', 'u', 't', 'p']
count:int = 0

for i in range(len(questions)):
    q = '%s 에서 밑줄(_) 안에 들어갈 알파벳은?' %questions[i]
    ans = input(q)

    if ans == answers[i]:
        print('정답입니다')
        count += 1
    else:
        print('틀렸습니다')

print('#'*50)
print(f'정답을 맞춘 문제 수 : {count}')
print('#'*50)
