import os
import hashlib
import json

fileinfo_dict = dict()
jar_name = []
jar_md5 = []
fp = r"./"  # 目标文件夹
with os.scandir(fp) as it:
    for i in it:

        print(i.name)  # 打印i变量对应的文件名, .name后面不能加括号
        if ".jar" in i.name:
            jar_name.append(i.name)

for i in range(0, len(jar_name)):
    path = './' + jar_name[i]
    with open(path, 'rb') as f:
        jar_md5.append(hashlib.md5(f.read()).hexdigest())
        f.close()

for i in range(0, len(jar_name)):
    fileinfo_dict[jar_name[i]] = jar_md5[i]
print(fileinfo_dict)
with open("MD5.json", 'w+') as file:
    json.dump(fileinfo_dict, file, ensure_ascii=False)
