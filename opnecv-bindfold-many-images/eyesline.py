import cv2
import numpy as np
import random
import os
import sys

# 引数格納
params = sys.argv
argc = len(params)

# 画像ディレクトリ定義
inDir = "./input/"
outDir = "./output/output/"
#errDir = "./output/error/"
cloneDir = "./output/copy/"

eye_cascade_path = 'haarcascade_eye.xml'
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

image_path = inDir + params[1]

print(image_path)

src = cv2.imread(image_path)
clone = cv2.imread(image_path)
if(src is None):
    print('画像を開けません。')
    quit()
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
print(src_gray)

eyes = eye_cascade.detectMultiScale(src_gray)
print(eyes)

def main():
    if(argc != 2):
        print('引数を指定して実行してください。')
        quit()

    if len(eyes) == 2:
        print("目の検出に成功しました。")
        print(eyes)
                
        ey1n = np.array([eyes[0,0] + eyes[0,2] // 2, eyes[0,1] + eyes[0,3] // 2])
        ey2n = np.array([eyes[1,0] + eyes[1,2] // 2, eyes[1,1] + eyes[1,3] // 2])
        Increase = ey1n - ey2n
        print(Increase)
        print(ey1n)
        print(ey2n)

        slope = Increase[1] / Increase[0]
        print(slope)

        Segment = ey1n[1] - ey1n[0]*slope
        print(Segment)

        x = np.min([eyes[0,0],eyes[1,0]]) + random.randrange(1,20) #右端のX座標
        print(np.min([eyes[0,0],eyes[1,0]]))
        print(x)

        y = slope * x + Segment
        print(y)

        np.max([eyes[1,0]+eyes[1,2],eyes[0,0]+eyes[0,2]])

        x2 = np.max([eyes[1,0]+eyes[1,2],eyes[0,0]+eyes[0,2]]) +random.randrange(1,20) #左端のX座標
        print(np.max([eyes[1,0]+eyes[1,2],eyes[0,0]+eyes[0,2]]))
        print(x2)

        y2 = slope * x2 + Segment
        print(y2)

        #描画
        new_image_path = outDir + params[1]
        cv2.line(src,(int(x),int(y)),(int(x2),int(y2)),(0,0,0),random.randrange(10,40), cv2.LINE_AA)
        cv2.imwrite(new_image_path, src)
        print(params[1])

        new_clone_path = cloneDir + params[1]
        cv2.imwrite(new_clone_path,clone)



    elif len(eyes) > 2:
        print("目が３つ以上検出されました。"+params[1])
            
    else:
        print("目が検出できません")
            


main()
