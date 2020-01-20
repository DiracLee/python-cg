import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append("..")
from utils.cg_types import Point
from utils.cg_utils import to_left

def construct_convex_hull(points, n):
    """
    作用：
    将点集points构造为凸包

    算法思想：
    先取任意三个点按照逆时针顺序纳入极点序列cp
    然后遍历剩余点集，做 in_convex_polygon test

    时间复杂度：O(n**2)
    """
    pass

def in_convex_polygon(points, n, x, cp):
    """
    作用：
    判断某个点x是否在给定凸多边形内部
    若在内部，则什么也不做
    若在外部，点x应当成为新的极点，并且之前极点序列中的某些点不再
    具有极性，应当从几点序列中移除

    算法思想：
    当前凸多边形cp(凸包)中的点按照逆时针有序存储
    逆时针依次遍历cp中的点k，以从x到k的射线为基础，对k的前驱与后继进行判断：
        若k的前驱与后继在射线x->k的两侧LR => k 应当从极点队伍中移除
        若k的前驱与后继在射线x->k的两侧RL => k 应当保留为极点
        若k的前驱与后继均在射线x->k的左侧LL => k 应当保留为极点队伍的第一个极点
        若k的前驱与后继均在射线x->k的右侧RR => k 应当保留为极点队伍的最后一个极点
    若没有LL或RR的情况，说明x在凸多边形cp的内部

    时间复杂度：O(n)
    """
    pass


if __name__ == "__main__":        
    n = 50
    points = [Point(x, y) for (x, y) in np.random.uniform(0, 10, (n, 2))]

    construct_convex_hull(points, n)

    plt.show()