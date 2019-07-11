import random #randomのインポート
import sys, time
import time

a = 0 #変数aを宣言
c = 1000000 #計算する回数
print(c)
s = time.time() #現在時刻を取得
for i in range(c): #計算する回数 十億
    sys.stdout.write("\r%d" % i) #計算回数を表示
    sys.stdout.flush()
    x, y = random.random(), random.random()
    if x**2 + y**2 < 1: #x2+y2≤1x2+y2≤1 なら a+1        x2+y2>1x2+y2>1 なら何もしない
        a += 1 #a+1
print("-end")
print(a *4 / c) #４を掛け、計算した数で割る
t = time.time() - s #現在時刻から最初に取得した現在時刻を引き、処理にかかった時間を算出
print("かかった時間:{0}".format(t) + "[sec]") #かかった時間を表示【:{0}】がおそらく大事
 # 3.1446  3.141607008
#gitテスト