from PIL import Image
import numpy as np

#이미지(맵) 불러오기
img = Image.open('testmap1.jpg')
# 이미지를 np array로 변환
originalmap = np.array(img)
# 명암 값에 따라 갈 수 없는 곳은 1, 갈 수 있는 곳은 0으로 바꿔줌
# 여기서의 기준값은 220
originalmap[originalmap < 220] = 1
originalmap[originalmap > 220] = 0
pass

#-----장애물 두께 넓히기-----#
# 성능 최악!!!!!!!!! 어차피 global map은 처음 한번만 돌리니 성능 신경쓰지 않았음... 4중 반복문><
goThicker = True #True일때만 작동
# 얼마나 두껍게 할건지
thicker = 5
newmap = np.array(np.zeros(originalmap.shape))

if goThicker:
    for i in range(originalmap.shape[0]):
        for j in range(originalmap.shape[1]):
            if originalmap[i][j] == 1:
                for n in range(-(thicker-1), thicker):
                    for m in range(-(thicker-1), thicker):
                        if (0 <= i + n < originalmap.shape[0]) and (0 <= j + m < originalmap.shape[1]):
                            newmap[i + n][j + m] = 1



np.save('originalmap.npy',originalmap)
np.save('newmap.npy', newmap)

pass

