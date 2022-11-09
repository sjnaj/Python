'''
Author: fengsc
Date: 2022-03-16 17:48:57
LastEditTime: 2022-03-16 23:58:00
'''
# 使用外部控件实现动画和交互
from turtle import onclick
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import itertools
from matplotlib.widgets import Button


pause = False


def on_click1(event):
    global pause
    pause ^= True  # 按位异或 相当于pause=~pause


def on_click2(event):
    global pause
    plt.close('all')


fig, ax = plt.subplots()
line, = ax.plot([], [], 'y', lw=2)
point, = ax.plot([], [], "o")
ax.set_ylabel('sine', loc='top')
ax.spines['bottom'].set_position(('data', 0))  # x轴调到中间
ax.grid()
xdata, ydata = [], []
text = plt.text(4, 0.8, '', fontsize=16)
btn_pause = Button(plt.axes([0.9, 0.6, 0.08, 0.06]), 'pause',  # 添加按钮 坐标和
                   color="khaki", hovercolor='yellow')
btn_close = Button(plt.axes([0.9, 0.7, 0.08, 0.06]), 'close',  # 添加按钮 坐标和
                   color="blue", hovercolor='red')
btn_pause.on_clicked(on_click1)
btn_close.on_clicked(on_click2)
# fig.canvas.mpl_connect('button_press_event', on_click)  # 点击事件（整个画面）


def init():  # data_gen
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1.2, 1.2)
    ax.set_xticks([x for x in np.arange(0, 2*np.pi, np.pi/2)])  # 范围和坐标值
    ax.set_xticklabels(
        ['$0$']+['$'+str(x)+'\pi$' for x in np.arange(0.5, 2, 0.5)],)
    del xdata[:]  # !保证重新开始的时候不会和上一次的线条冲突,不能修改外部变量引用
    del ydata[:]
    line.set_data(xdata, ydata)
    ax.figure.canvas.draw()

    return line,


def data_gen():
    x = 0
    y = 0
    for t in np.arange(0, 10*np.pi, 0.1):
        while(pause):  # *更新,否则返回上次的返回值实现暂停
            plt.pause(0.1)  # 单位是秒，暂停
        x = t
        y = np.sin(t)
        yield x, y


def run(data):
    x, y = data
    xdata.append(x)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()
    if x >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()  # 更新界面，不加也会自动扩张
        ax.set_xticks([x for x in np.arange(xmin, 2*xmax, np.pi/2)])
        ax.set_xticklabels(
            ['$0$']+['$'+str(x)+'\pi$' for x in np.arange(xmin/np.pi+0.5, 2*xmax/np.pi, 0.5)], rotation='vertical')
    line.set_data(xdata, ydata)
    point.set_data(x, y)  # 更新端点
    point.set_color('r' if y > 0 else 'b')   # 调整颜色

    text.set_text("x=%.3f, y=%.3f" % (x, y))
    return line, point, text  # !需要更新的text句柄都要返回,一个元素时末尾要加逗号


anim = animation.FuncAnimation(
    fig, run, data_gen, interval=10, init_func=init)  # !blit=True优化会影响图形输出，但不影响保存的图片
anim.save('/home/fengsc/Desktop/Python/Basic/Animate/demo2.gif')# 要在show之前save

# plt.show(block=False)# 结束后自动关闭，需要pause确保图片已显示否则会不打开直接关掉,配合repeat=False使用
# plt.pause(0.1)

plt.show()
