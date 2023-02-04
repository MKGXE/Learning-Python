class 학생:
    name = ''
    num = 0
    key = 0.0
    def 학생정보보기(self):
        print('이름 :',self.name,', 번호 :',self.num,', 키 :',self.key)
    def 학생정보입력(self, name, num, key):
        self.name = name
        self.num = num
        self.key = key
    def __init__(self, name, num, key):
        self.name = name
        self.num = num
        self.key = key

# 다른 사람들이 '학생'클래스 사용
# 클래스 업데이트 요청

# 상속 : 사람이 복붙을 하면 사람이 고쳐야하기 때문에, 컴퓨터가 복붙을 해서 컴퓨터가 고치게한다 (클래스 복붙)
class 학생2(학생):
    name = ''
    num = 0
    key = 0.0
    def 학생정보보기(self):
        print('이름 :',self.name,', 번호 :',self.num,', 키 :',self.key)
    def 학생정보입력(self, name, num, key):
        self.name = name
        self.num = num
        self.key = key
    def __init__(self, name, num, key):
        # 생성자
        # 객체(변수)가 생성될 때 바로 사용되는 함수
        self.name = name
        self.num = num
        self.key = key
def __del__(self):
    # 소멸자
    # 객체(변수)가 없어질 때 사용되는 함수
    print('프로그램 종료')
