import pandas as pd
import matplotlib.pyplot as pt

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname = "C:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family = font_name)
#년도별 & 지역별 평균 구하기

def ploty(a):
    x = [0, 1, 2, 3, 4]
    x1 = [14, 15, 16, 17, 18]
    pt.plot(x, a, 'bo-')
    pt.xticks(x, x1)
    pt.xlabel('년도')
    pt.ylabel('미세먼지농도')
    pt.show()
def plots(a):
    x = [0, 1, 2, 3]
    x1 = ['봄', '여름', '가을', '겨울']
    pt.plot(x, a, 'bo-')
    pt.xticks(x, x1)
    pt.xlabel('분기')
    pt.ylabel('미세먼지농도')
    pt.show()
def meany(data, num):
    for i in range(5):
       j = i + 14
       dfy = data[(data['지점명'] == num) & (data['년도'] == j)].mean()
       df.append(dfy.loc[['미세먼지농도']])
    ploty(df)
def means(data, num):
    for i in range(3):
        dfs = data[(data['지점명'] == num) & (data['월자'] <= 5 + i*3) & (data['월자'] >= 3 + i*3)].mean()
        df.append(dfs.loc[['미세먼지농도']])
    dfs = data[(data['지점명'] == num) & ((data['월자'] == 12) | (data['월자'] <= 2))].mean()
    df.append(dfs.loc[['미세먼지농도']])
    plots(df)
if __name__ == "__main__":
    data = pd.read_csv('pm10_20142018a.txt', sep = '\t', header = 0, encoding = 'CP949')
    llist = ['서울', '부산', '대구', '인천', '광주', '대전', '울산']
    while True:
        num = input("지역번호입력(1:서울, 2:부산, 3:대구, 4:인천, 5:광주, 6:대전, 7:울산)")
        if (num == 'end'): break
        sea = input("1:연평균 그래프, 2:분기별 그래프")
        num = int(num)
        df = []
        if (sea == '1') : meany(data, llist[num - 1])
        if (sea == '2') : means(data, llist[num - 1])


