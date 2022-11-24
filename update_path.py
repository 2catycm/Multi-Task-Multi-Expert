# coding:utf-8

import os, shutil

rootdir = './data'          # 原始带有后缀名的文件路径
remove_path = './data'   # 去除后缀名的文件路径

# 修改文件名
def renameFile(oldname, newname):
    print("oldname:", oldname)
    print("newname:", newname)
    os.rename(oldname, newname)
    # shutil.copyfile(oldname, newname)
    # shutil.move(newname,remove_path)

# 列出文件
def listTxtFile(filepath):
    if os.path.isfile(filepath) and filepath.startswith('./data/ali'):
    # if os.path.isfile(filepath) and filepath.startswith('./test'):
        print('filepath:', filepath)
        oldName = filepath
        newName = '.'.join(oldName.split('.')[0:2])+'.zip'
        renameFile(oldName, newName)
        # shutil.move(newName, remove_path)
        
# 遍历目录下所有的文件
def listPath(filepath):
    fileList = os.listdir(filepath)
    for fi in fileList:
        fi_d = os.path.join(filepath, fi)
        if os.path.isdir(fi_d):
            listPath(fi_d)
        else:
            listTxtFile(fi_d)

if __name__ == "__main__":
    listPath(rootdir)