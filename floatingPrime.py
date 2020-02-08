def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True


while True:
    numberFloatString = input()
    if numberFloatString == '0.0':
        break
    temp = ""
    for i in numberFloatString:
        if i != '.':
            temp += i
    if isprime(int(temp[:2])) or isprime(int(temp[:3])) or isprime(int(temp[:4])):
        print("TRUE")
    else:
        print("FALSE")
