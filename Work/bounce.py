# bounce.py

#一个橡胶球从 100 米的高度掉落，每次撞击地面后
# 反弹起来的高度是掉落高度的 3/5。
# 编写一个名为 bounce.py 的程序，打印出一个表格
# 展示该球前 10 次反弹的高度。

# Exercise 1.5
height_high : float = 100
height_ground : float = 0
for i in range(10):
    height_ground = height_high * 0.6
    height_high = height_ground
    print(i,round(height_ground,4))