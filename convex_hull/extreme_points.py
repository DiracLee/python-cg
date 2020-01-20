import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append("..")
from utils.cg_types import Point
from utils.cg_utils import in_triangle


def set_extreme_point(points, n):
    """
    作用：
    将所有极点用大绿点表示并将其extreme值标为True，
    将所有非极点用小红点表示并将其extreme标为False

    算法思想：
    先将所有的点标记为极点(标记为大绿点)
    然后对每个点关于不包含该点的所有三角形做in_triangle test
    只要它在任何一个三角形的内部，就可以判断它不是极点(标为小红点)
    对每个点加以验证，最终剩下的就是极点(大绿点)
    
    时间复杂度：O(n**4)
    """
    for s in range(n):
        points[s].extreme = True
    for p in range(n):
        for q in range(p + 1, n):
            for r in range(q + 1, n):
                for s in range(n):
                    if s == p or s == q or s == r or not points[s].extreme:
                        continue
                    if in_triangle(points[p], points[q], points[r], points[s]):
                        points[s].extreme = False
                        plt.plot(points[s].x, points[s].y, "r.")
    
    for s in range(n):
        if points[s].extreme:
            plt.plot(points[s].x, points[s].y, "go")

if __name__ == "__main__":        
    n = 50
    points = [Point(x, y) for (x, y) in np.random.uniform(0, 10, (n, 2))]

    set_extreme_point(points, n)

    plt.show()
