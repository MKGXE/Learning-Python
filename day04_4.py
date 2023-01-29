# 문자열을 저장하는 리스트
lst = []
num = 0
b = 0

# 사용자에게 입력을 받아 리스트를 구성
# 1: 추가하기, 2: 수정하기, 3: 삭제하기, 4: 전체보기
while True:
    num = int(input('1:추가, 2:수정, 3:삭제, 4:조회>>'))
    if num == 1:
        lst.append(input('숫자를 입력해주세요>>'))            # 추가할 값을 입력
    elif num == 2:      
        a = input('수정하고자하는 값을 입력해주세요>>')            # 값을 수정 (수정하고자 하는 값, 수정할 값)
        b = lst.index(a)
        print('해당 값이 저장되어있는 위치는',b)
        lst[b] = input('수정 할 값을 입력해주세요>>')
        print('수정된 값은',lst)
    elif num == 3:      
        lst.remove(input('제거할 값을 입력해주세요>>'))            # 삭제할 값 입력
        print('삭제된 후 값은',lst)
    elif num == 4:
        for i in lst:
            print(i)            # 전체조회
    elif num == 0:
        print('프로그램 종료')      # 프로그램 종료
        break           
    else:
        print('없는 번호입니다.')