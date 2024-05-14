import math
import numpy as np
from PIL import Image, ImageDraw
from PIL import ImagePath


class perfab():
    def __init__(self, dx, dy):
        self.perfab = dict()
        self.dx, self.dy = dx, dy

    def support_parallelpentagon_img(self):
        dx, dy = self.dx, self.dy
        path = [[1.5, 0], [0, 0], [0, 5], [0.2, 5], [1.5, 1.5]]
        imgPath = [(i/dx, j/dy) for i,j in path]
        image = ImagePath.Path(imgPath).getbbox()
        size = list(map(int, map(math.ceil, image[2:])))
        img = Image.new("L", size, 0)
        img1 = ImageDraw.Draw(img)
        img1.polygon(imgPath, fill=255, outline=255)
        # return img.transpose(Image.ROTATE_270)
        return img.transpose(Image.FLIP_TOP_BOTTOM)

    # width unit => mm
    def support(self, width):
        if width in self.perfab:
            return self.perfab[width]

        dx, dy = self.dx, self.dy
        height = 5
        size = (width, int(height/dy))
        img = Image.new("L", size, 0)
        pentagon1 = self.support_parallelpentagon_img()
        pentagon2 = self.support_parallelpentagon_img().transpose(Image.FLIP_LEFT_RIGHT)
        img.paste(pentagon1, (0, 0))
        img.paste(pentagon2, (width-pentagon2.size[0], 0))
        img_np = np.asarray(img)
        self.perfab[width] = img_np
        return img_np

if __name__ == '__main__':
    pf = perfab(0.043, 0.043)
    # img = pf.support_parallelpentagon_img(0.043, 0.043)
    img = pf.support(width=int(25/0.043))
    img.show()