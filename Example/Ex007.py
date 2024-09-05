# sum = 0
# i = 1
#
# while i <= 100:
#     sum += i
#     print(f'{i} : {sum}')
#     i += 1
#
# print('총합은 : ', sum)

word = ('Python is widely used by a number of big companies')
word = word.lower() #모든 문자를 소문자로 변경

i = 0

count = 0

print('모음 : ', end='')

size = len(word)
while i < size:
    if (word[i] == "a" or word[i] == "e"
            or word[i] == "i" or word[i] == "o"
            or word[i] == "u"):
        count = count + 1
        print(word[i], end=" ")
    i += 1

print()
print("모음의 개수 : %d" % count)
