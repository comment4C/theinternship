textList = []
answerList = []
number = int(input())
for i in range(number):
    textList.append(input())

for text in textList:
    temp = ""
    for char in text:
        if char == char.upper() and char != ' ':
            temp += char
    answerList.append(temp)
answerList.sort(key=len)
answerList.reverse()
for i in answerList:
    print(i)
