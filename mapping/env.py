from PIL import Image
import numpy as np

class Env:
    img = Image.open('testmap1.jpg')
    x = np.array(img)
    x[x < 150] = 0
    x[x > 150] = 1

    def __init__(self):
        img = Image.open('testmap1.jpg')
        x = np.array(img)
        x[x < 150] = 0
        x[x > 150] = 1
        self.x_range = x.shape[0]
        self.y_range = x.shape[1]
        self.motions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                        (1, 0), (1, -1), (0, -1), (-1, -1)]
        self.obs = self.obs_map()

    def update_obs(self, obs):
        self.obs = obs

    # def obs_map(self):
    #     """
    #     Initialize obstacles' positions
    #     샘플맵
    #     :return: map of obstacles
    #     """
    #
    #     x = self.x_range
    #     y = self.y_range
    #     obs = set()
    #
    #     for i in range(x):
    #         obs.add((i, 0))
    #     for i in range(x):
    #         obs.add((i, y - 1))
    #
    #     for i in range(y):
    #         obs.add((0, i))
    #     for i in range(y):
    #         obs.add((x - 1, i))
    #
    #     for i in range(10, 21):
    #         obs.add((i, 15))
    #     for i in range(15):
    #         obs.add((20, i))
    #
    #     for i in range(15, 30):
    #         obs.add((30, i))
    #     for i in range(16):
    #         obs.add((40, i))
    #
    #     return obs

    def obs_map(self):
        img = Image.open('testmap1.jpg')
        arr = np.array(img)
        arr[arr < 150] = 0
        arr[arr > 150] = 1


        #반드시 처리가 완료된 이미지를 넣을 것. 1:장애물 0:이동가능
        x = self.x_range
        y = self.y_range
        obs = set()

        for i in range(x):
            for j in range(y):
                if arr[i][j] == 0:
                    obs.add((i, j))

        return obs