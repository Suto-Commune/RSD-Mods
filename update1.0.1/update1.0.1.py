import json
import sys
import requests
import os
from tqdm import tqdm

os.system("chcp 65001")
program_version=str("1.0.1")
#20220430
os.system("title RedStone Update Version: "+program_version)


#创建目录避免报错
if os.path.exists("./.minecraft/mods")==False:
    os.mkdir("./.minecraft/mods")
#判断是否联网
def lianwangpanduan():
    try:
        panduanshifoulianwang=requests.get("http://www.baidu.com",timeout=2)
    except:
        return False
    return  True

#下载条
def download(url: str, fname: str):
    # 用流stream的方式获取url的数据
    resp = requests.get(url, stream=True)
    # 拿到文件的长度，并把total初始化为0
    total = int(resp.headers.get('content-length', 0))
    # 打开当前目录的fname文件(名字你来传入)
    # 初始化tqdm，传入总数，文件名等数据，接着就是写入，更新等操作了
    with open(fname, 'wb') as file, tqdm(
        desc=fname,
        total=total,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in resp.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)

#联网判断
if lianwangpanduan()==False:
    print("未网络.请联网后使用")
    os.system("pause")
    sys.exit()
else:
    print("已链接网络")

#获取json
latest_ = requests.get("https://api.github.com/repos/miangou/republicofredstone/releases/latest")
latest_json = latest_.json()
#写入本地
# file_latest_write.close()

# print(latest_json)
print("The Latest Version: " + latest_json["tag_name"] + " 由 " + latest_json["author"]["login"] + " 上传.")

# #转化为数字
# latest_tag=latest_json["tag_name"]
# latest_version_list=str(latest_tag).split(".")
# latest_version_num=''
# latest_version_num=int(latest_version_num.join(latest_version_list))

# print("Latest version num:"+str(latest_version_num))

latest_file_num = len(latest_json["assets"])

latest_file_name = [0 for i in range(latest_file_num)]
latest_file_download_link = [0 for i in range(latest_file_num)]
latest_file_will_do = [0 for i in range(latest_file_num)]
for i in range(0, latest_file_num):
    latest_file_name[i] = latest_json["assets"][i]["name"]
    latest_file_download_link[i] = latest_json["assets"][i]["browser_download_url"]
    # print(latest_file_name[i])
    # print(latest_file_download_link[i])
    if os.path.exists('./.minecraft/mods/' + latest_file_name[i]):
        latest_file_will_do[i] = 0
    else:
        latest_file_will_do[i] = 1
#上次更新
# print(lastver)
if os.path.exists("version.txt")==True:
    lasttime_ = requests.get("https://api.github.com/repos/miangou/republicofredstone/releases")
    lasttime_json = lasttime_.json()
    lasttime_num = len(lasttime_json)
    lasttime_open = open('version.txt','r')
    lastversion_fangwen_i = 0
    # print(lasttime_open.readlines(1))
    lastver=lasttime_open.readlines(0)
    for i in range(0, lasttime_num):
        # print(str(lasttime_json[i]["tag_name"]))
        if str(lasttime_json[i]["tag_name"]) == str(lastver[0]):
        #     print(lastver)
        # if lasttime_json[i]["tag_name"] == "1.1.3":
            lastversion_fangwen_i=i
            break
    lasttime_open.close()
    lasttime_num=len(lasttime_json[lastversion_fangwen_i]["assets"])
    latest_all_name = [0 for i in range(latest_file_num)]

    lasttime_all_name = [0 for i in range(lasttime_num)]

    for i in range(0,latest_file_num):
        latest_all_name[i]=latest_json["assets"][i]["name"]
    for i in range(0,lasttime_num):
        lasttime_all_name[i]=lasttime_json[lastversion_fangwen_i]["assets"][i]["name"]
        # print(lasttime_json[lastversion_fangwen_i]["assets"][i]["name"]+","+str(i))
    # print(lasttime_all_name)
    # print(latest_all_name)
    #
    old_new_difference = list(set(lasttime_all_name).difference(latest_all_name))
    old_new_difference1 = set(latest_all_name).difference(lasttime_all_name)
    # print(old_new_difference)
    # print(old_new_difference)
    if old_new_difference:
        for i in range(0,len(old_new_difference)):
            latest_file_name.append(old_new_difference[i])
            latest_file_will_do.append(2)
    # print(latest_file_will_do)
    # print(latest_file_will_do)
    # print(latest_file_name)



file_latest_write = open('version.txt',mode='w')
file_latest_write.write(str(latest_json["tag_name"]))
file_latest_write.close()

zhuangtai=0
for i in range(0,len(latest_file_will_do)):
    if latest_file_will_do[i] == 1:
        print("发现Mod依赖丢失: "+latest_file_name[i]+" ,准备下载...")
        download("https://redstone-download.netlify.app/"+latest_file_name[i],"./.minecraft/mods/"+latest_file_name[i])
        zhuangtai+=1
    elif latest_file_will_do[i] == 2 and os.path.exists("./.minecraft/mods/"+latest_file_name[i]):
        print("发现冗余Mod(s): "+latest_file_name[i]+" ,即将删除")
        # if os.path.exists("./.minecraft/mods/"+latest_file_name[i]):
        os.remove("./.minecraft/mods/"+latest_file_name[i])
        zhuangtai += 1
if zhuangtai==0 :
    print("恭喜!您的Mod(s)依赖均为最新!")
os.system("pause")