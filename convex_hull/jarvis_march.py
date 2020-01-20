import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append("..")
from utils.cg_types import Point
from utils.cg_utils import to_left

def construct_by_jm(points, n):
    """
    作用：
    将点集points构造为凸包
    
    算法思想：
    首先，沿着逆时针方向，构造一个极边s->t
    利用极边的性质：“任何一个极边，他的右侧必然是空的”
    找到下一个极点：使偏转角度最小的点
    直到下一个极点是初始极点，算法完成

    时间复杂度：O(n**2)
    """
    pass

def next_extreme(points, n, s, t):
    """
    作用：
    根据当前极边s->t，沿着逆时针方向找到下一个极点，从而构造新极边

    算法思想：
    """
    pass