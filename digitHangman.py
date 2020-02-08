answerList = []
temp = input()
proposition = temp.split(" ")
answerList.append("_ "*12)
count = 0
for i in range(5):
    guess = input()
    temp = answerList[i].split(" ")
    for j in range(12):
        if guess == proposition[j]:
            temp[j] = guess
    if guess in proposition:
        answerList.append(' '.join(temp))
        count += temp.count(guess)
    else:
        answerList.append(' '.join(temp) + guess + ' ')
for text in answerList:
    print(text)
print(count)
