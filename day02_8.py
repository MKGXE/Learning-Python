# 1
# 횟수를 입력받아서 그 수만큼 Hello 출력하는 프로그램
# 5를 입력하면
# 1번째 Hello
# 2번째 Hello
# 3번째 Hello
# 4번째 Hello
# 5번째 Hello

# p = 0
# i = int(input('숫자를 입력해주세요>>'))

# while p <= i:
#     print(p,'번째 Hello')
#     p += 1
# print('종료')

# 2
# 1~100 사이에서 7의 배수만 출력하는 프로그램 (while안에서 if를 사용)

# i = 1
# while i <= 100:
#      if i % 7 == 0:
#          print(i)
#          i += 1
# print('종료')

# 3
# 커피 1잔에 300원, 금액을 입력하여 몇잔의 커피와 잔돈이 얼마가 남는지 출력
# == 실행 예 ==

# price = 300
# 금액 = int(input('금액은 얼마인가요?'))
# 커피잔수 = 0

# while 금액 >= price:      # 횟수로써 i = 0, 범위로써 금액 >= price
#   금액 -= price:
#   커피잔수 += 1
#   print('커피',커피잔수,'잔, 잔돈',금액,'원')

m = int(input('금액을 입력하세요>>'))
p = 1
i = 300

while (m-(i*p)) >= 0:
    e = (m-(i*p))
    print('개수는',p,'잔돈은',e)
    p += 1
print('종료')