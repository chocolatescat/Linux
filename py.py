#coding=utf-8
"""
@author:FiaFia
@data:2018/7/9
@version:Python3.6
@FileName: CopyFile.py
"""
print("********** 注意：文本文件编码必须是 ANSI **********")

import sys
import os
import shutil
import tkinter as tk
from tkinter import filedialog



'''打开选择文件夹对话框'''
root = tk.Tk()
root.withdraw()

Filepath = filedialog.askopenfilename() #获得选择好的文件
Folderpath = filedialog.askdirectory() #获得选择好的文件夹


def moveFile(fileList, targetDir):
    log = open('running.log', 'w')
    with open(fileList) as f:
        for line in f.readlines():
            line = line.strip('\r\n')
            basename = os.path.basename(line)
            exists = os.path.exists(line)
            if exists:
                fullPath = os.getcwd() + '\\' + targetDir + '\\' + basename
                print('移动 %s 到 %s' % (line, fullPath))
                log.write('移动 %s 到 %s \r\n' % (line, fullPath))
                shutil.move(line, targetDir +'\\' + basename)
            else:
                print("%s 未能移动" % line)
                log.write("%s 未能移动 \r\n" % line)
    log.close()


if __name__ == '__main__':
    #fileList = 'filelist.txt'
    #targetDir = 'NewFolder'
    
    
    fileList = Filepath
    targetDir = Folderpath
    if not os.path.exists(targetDir):
        os.makedirs(targetDir)
    moveFile(fileList, targetDir)

input()
