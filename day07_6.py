# 학생 클래스
# 속성(멤버변수) : 이름, 번호, 키
# 기능(메서드) : 학생정보보기, 학생정보입력,__init__

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

철수 = 학생('김철수', 1, 177.7)
영희 = 학생('박영희', 2, 155.5)
짱구 = 학생('신짱구', 3, 173.3)

철수.학생정보보기()     # 이름 : 김철수, 번호 : 1, 키 : 177.7
영희.학생정보보기()     # 이름 : 박영희, 번호 : 2, 키 : 155.5
짱구.학생정보보기()     # 이름 : 신짱구, 번호 : 3, 키 : 173.3

짱구.학생정보입력('짱구', 4, 174.0)
짱구.학생정보보기()     # 이름 : 짱구, 번호 : 4, 키 : 174.0