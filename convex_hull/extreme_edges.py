import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append("..")
from utils.cg_types import Point
from utils.cg_utils import to_left


def mark_ee(points, n):
    """
    作用：
    将所有极点用大绿点表示并将其extreme值标为True，
    将所有非极点用小红点表示并将其extreme标为False
    将所有极边用绿线连接

    算法思想：
    先将所有点标记为非极点(小红点)，即所有边都是非极边
    然后对每一条边做check_edge操作

    时间复杂度：O(n**3)
    """
    for k in range(n):
        points[k].extreme = False
        plt.plot(points[k].x, points[k].y, "r.")
    for p in range(n):
        for q in range(p + 1, n):
            check_edge(points, n, p, q)


def check_edge(points, n, p, q):
    """
    作用：
    判断一对点是否构成极边，
    若是极点，将其extreme值标为True，用大绿点表示，并用绿线将其连接

    算法思想：
    遍历所有的点，若所有的点都在其同一侧，则说明该边是极边
    """
    l_empty = r_empty = True
    for k in range(n):
        if not (l_empty or r_empty):
            break
        if k == p or k == q:
            continue
        if to_left(points[p], points[q], points[k]):
            l_empty = False
        else:
            r_empty = False

    if l_empty or r_empty:
        points[p].extreme = True
        points[q].extreme = True
        plt.plot(points[p].x, points[p].y, "go")
        plt.plot(points[q].x, points[q].y, "go")
        plt.plot((points[p].x, points[q].x), (points[p].y, points[q].y), "g-")


if __name__ == "__main__":
    n = 50
    points = [Point(x, y) for (x, y) in np.random.uniform(0, 10, (n, 2))]

    mark_ee(points, n)

    plt.show()
