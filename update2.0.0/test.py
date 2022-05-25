import sys
import upd2
from tkinter import filedialog

import ttkbootstrap as ttk



def btn_func():
    upd2.upd()

def select_folder():
    # 文件夹选择
    selected_folder = filedialog.askdirectory()  # 使用askdirectory函数选择文件夹
    select_path.set(selected_folder)


root = ttk.Window()
# mystd = myStdout()  # 实例化重定向类

t = ttk.Text(root).grid(column=0,row=0,rowspan=10)  # 输出控制台日志类
# t.pack()  # 放置

b = ttk.Button(root, text='start', command=btn_func,width=20).grid(column=2,row=4,rowspan=3)  # 按钮开始更新操作
#选择文件
select_path = ttk.StringVar()
ttk.Label(root, text="启动器路径：").grid(column=1, row=1, rowspan=3)
ttk.Entry(root, textvariable=select_path, width=50).grid(column=2, row=1, rowspan=3)
ttk.Button(root, text="...", command=select_folder).grid(column=3, row=1,rowspan=3)


# b.pack()  # 防止

root.mainloop()  # 显示窗体
# mystd.restoreStd()  # 恢复标准输出
