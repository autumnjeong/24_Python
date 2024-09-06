# scores = []
#
# while True:
#     score = int(input('성적을 입력하세요(종료 시 -1 입력):'))
#
#     if score == -1:
#         break
#     else:
#         scores.append(score)
#
# print('%s' % scores)
#
# sum = 0
# size = len(scores)
#
# for i in range(size):
#     sum += scores[i]
#     i += 1
#
# ave = sum / size
#
# print(f'총 합계 : {sum}')
# print(f'평균 값 : {ave}')

numbers = [[10, 20, 30], [40, 50, 60, 70, 80]]

for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        print('numbers[%d][%d] = %d' % (i, j, numbers[i][j]))