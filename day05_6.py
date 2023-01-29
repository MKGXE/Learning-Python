# 외부 함수를 사용하는 법 : import
# 모듈 : 부품

# import 모듈명
# import 모듈명 as 별명
# form 모듈명 import 함수명

# 모듈명을 plt로 사용
import matplotlib.pyplot as plt
# 모듈 중에 font_manager와 rc 부분만 가져옴
from matplotlib import font_manager, rc

font = font_manager.FontProperties(fname='H2PORL.ttf').get_name()
rc('font', family=font)

lst = [10,20,10,30,40,90,60,10,40,30]
plt.title('분포도')         # 제목 써줘
plt.xlabel('점수')          # X축 제목
plt.ylabel('갯수')          # Y축 제목
plt.hist(lst)             # 막대그래프로 그려줘
plt.show()                # 보여줘

