import codecs
import time
import json
import configparser

import random
import requests
from selectolax.parser import HTMLParser
import configparser

import os, pathlib
from pathlib import Path


def this_host():
    config = configparser.ConfigParser()  # 类实例化

    path = r'host.ini'
    config.read(path)
    prot = config['base']['prot']

    return "http://127.0.0.1:" + str(prot) + "/";





def get_contenttxt(path):
    f = open(path, encoding="utf-8")
    content = f.read()
    f.close()
    return content

def set_result(path,content):
    fo = codecs.open(path, "a", 'utf-8')
    fo.write(content)
    fo.close()
    return True


def main(name):




    try:
        curl_url = str(this_host()) + "number_list/getIdDiff_config"
        res = requests.post(url=curl_url, data={}, verify=False)
        print(res.text)
        res = json.loads(res.text)
    except Exception as e:
        print(time.strftime("%Y-%m-%d %H:%M:%S"), "|", 'getIdDiff_config', str(e))
        return

    if res['status'] == False:
        print(time.strftime("%Y-%m-%d %H:%M:%S"), "|", res['message'])




    config = res['config']
    is_diff = int(config['is_diff'])
    id_leng = config['id_leng']
    #
    # BASE_DIR = Path(__file__).resolve().parent.parent
    # IDOKpath = str(BASE_DIR) + "/ID_DIFF/OK/ok.txt"
    IDOKpath = "automationExe/ID_DIFF/OK/ok.txt"
    IDOKpath = IDOKpath.replace("\\", '/')

    if os.path.exists(IDOKpath) == True:
        os.remove(IDOKpath)

    id_list = []



    # IDpath = str(BASE_DIR) + "/ID_DIFF/ID/"
    IDpath = "automationExe/ID_DIFF/ID/"
    IDpath = IDpath.replace("\\", '/')





    for file in os.listdir(IDpath):
        file_name = str(file)
        path = str(IDpath) + str(file_name)
        id_son = get_contenttxt(path)
        id_son = id_son.split("\n")
        id_list = id_son + id_list

    print(time.strftime("%Y-%m-%d %H:%M:%S"),len(id_list),"个ID参与筛选")

    id_list.sort()
    list = []
    for id in id_list:

        if is_diff == 1:
            if id in list:
                print(time.strftime("%Y-%m-%d %H:%M:%S"),id, "重复")
                continue


        if len(id) >= int(id_leng):
            print(time.strftime("%Y-%m-%d %H:%M:%S"),id, len(id), "位")
            continue

        list.append(id)

        # IDOKpath = str(BASE_DIR) + "/ID_DIFF/OK/ok.txt"
        IDOKpath = "automationExe/ID_DIFF/OK/ok.txt"
        IDOKpath = IDOKpath.replace("\\", '/')

        set_result(str(IDOKpath), str(id) + "\n")

    print(time.strftime("%Y-%m-%d %H:%M:%S"),"筛选出ID", len(list), "个，已存储在[ ok.txt ]文件中")
    curl_url = str(this_host()) + "number_list/setIdDiff_config"
    res = requests.post(url=curl_url, data={}, verify=False)
    # print(res.text)



    # if is_diff == '1':
    #
    #     for id in id_list:
    #         print(id)

















# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    main('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
