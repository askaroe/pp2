import time
import math

def multiplicationOfList(list):
    product = 1
    for i in range(0, len(list)):
        product *= i
    return product

def countingLetters():
    s = input()
    upperL = 0
    lowerL = 0
    for i in s:
        if(ord(i) >= 65 and ord(i) <= 90):
            upperL += 1
        elif(ord(i) >= 97 and ord(i) <= 122):
            lowerL += 1
    return f"Lower cases: {lowerL}\nUpper cases: {upperL}"
# print(countingLetters())

def palindromeChecker():
    s = input()
    l = list(s)
    rl = reversed(l)
    s1 = ""
    for i in rl:
        s1 += i
    if(s1 == s):
        print(f"This string is palindrome, because {s} = {s1}")
    else:
        print(f"This string is not palindrome, because {s} != {s1}")
# palindromeChecker()

def sqrtInvoke():
    num = int(input())
    wait = int(input())
    time.sleep(wait / 1000)
    print(f"Square root of {num} after {wait} miliseconds is {math.sqrt(num)}")
# sqrtInvoke()

def trueTuple():
    cnt = 0
    t = (0, True, 6, "Olzhas", 1, False)
    for i in t:
        if(bool(i)):
            return False
    return True
# i could use all()
# print(trueTuple())
