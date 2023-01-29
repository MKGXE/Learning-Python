# 3개 더하기 , 빼기, 곱하기, 나누기
# +, -, *, / : 2개만 할 수 있음

def 더하기(num1, num2, num3):
    print(num1+num2+num3)
    pass

print(1+2)
더하기(1,2,3)

# 빼기, 곱하기, 나누기 (3)

def 빼기(num1, num2, num3):
    print(num1 - num2 - num3)
    pass

def 곱하기(num1, num2, num3):
    print(num1 * num2 * num3)
    pass

def 나누기(num1, num2, num3):
    print(num1 / num2 / num3)
    pass

def 절댓값더하기(a, b):
    if a < 0:
        a *= -1
    if b < 0:
        b *= -1
    print(a+b)
    
절댓값더하기(3, 7)      # 10
절댓값더하기(-4, 3)     # 7