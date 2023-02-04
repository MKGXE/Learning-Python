# 자동차 클래스를 만들어보세요
# 속성(변수) : 차주인, 색상, 차종
# 기능(메서드) : 차정보

class 자동차:
    own = ''
    col = ''
    car = ''
    def 차정보(self):
        print(self.own, self.col, self.car)
    def 차운전(self):
        print(self.own,'가 차를 운전합니다')
    def __init__(self, own, col, car):
        self.own = own
        self.col = col
        self.car = car

엄마차 = 자동차('엄마', 'white', 'ssangyong TiVOLi armor')
아빠차 = 자동차('아빠', 'gray', 'bmw M760Li')
내차 = 자동차('나', 'blue','subaru WRX STi 2016')

엄마차.차정보()
아빠차.차정보()
내차.차정보()

엄마차.차운전()
아빠차.차운전()
내차.차운전()

# 메서드가 같아도 객체가 다르면 그 객체에 해당하는 메서드와 매개변수로 사용됨
