import sys
import upd2
from tkinter import filedialog
import ttkbootstrap as ttk
import os

os.system("chcp 65001")


class myStdout():  # 重定向类
    def __init__(self):
        # 将其备份
        self.stdoutbak = sys.stdout
        self.stderrbak = sys.stderr
        # 重定向
        sys.stdout = self
        sys.stderr = self

    def write(self, info):
        # info信息即标准输出sys.stdout和sys.stderr接收到的输出信息
        t.insert('end', info)  # 在多行文本控件最后一行插入print信息
        t.update()  # 更新显示的文本，不加这句插入的信息无法显示
        t.see(ttk.END)  # 始终显示最后一行，不加这句，当文本溢出控件最后一行时，不会自动显示最后一行

    def restoreStd(self):
        # 恢复标准输出
        sys.stdout = self.stdoutbak
        sys.stderr = self.stderrbak


def btn_func():
    if not select_path.get():
        select_path.set("./minecraft")
    upd2.upd(select_path.get())


def select_folder():
    # 文件夹选择
    selected_folder = filedialog.askdirectory()  # 使用askdirectory函数选择文件夹
    select_path.set(selected_folder)


root = ttk.Window()
mystd = myStdout()  # 实例化重定向类
root.title("Redstone Installer - 2.0.0 Beta whit GUI , By LolingNatsumi")

t = ttk.Text(root)
# .grid(column=0,row=0,rowspan=10)  # 输出控制台日志类
# t.pack()  # 放置
t.grid(column=0, row=0, rowspan=10)

b = ttk.Button(root, text='start', command=btn_func, width=20)
b.grid(column=2, row=4, rowspan=3)  # 按钮开始更新操作
# 选择文件

select_path = ttk.StringVar()
select_path.set("./minecraft")
ttk.Label(root, text=".minecraft文件夹路径：").grid(column=1, row=1, rowspan=3)
ttk.Entry(root, textvariable=select_path, width=50).grid(column=2, row=1, rowspan=3)
ttk.Button(root, text="...", command=select_folder).grid(column=3, row=1, rowspan=3)

root.mainloop()  # 显示窗体
mystd.restoreStd()  # 恢复标准输出
