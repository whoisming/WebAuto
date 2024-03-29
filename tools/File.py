# -*- coding: utf-8 -*-
# author:liucong

import os


# 从一个目录里获取所有的文件名并返回一个列表，剔除其中的__init__.py和__pycache__。
def GetPyList(file_path):
    dirList = os.listdir(file_path)
    pyList = []
    for i in range(len(dirList)):
        fileName = dirList[i].split(".")
        if dirList[i] != "__init__.py" and dirList[i] != "__pycache__":
            if fileName[1].lower() == "py":
                pyList.append(fileName[0])
    return pyList
