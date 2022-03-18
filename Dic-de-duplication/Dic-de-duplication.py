import sys
import os

#从键盘输入
dicfile = sys.argv[1]#源字典1
addfile = sys.argv[2]#源字典2
newfile = sys.argv[3]#去重完之后的字典

def merge(dic1,dic2):
    try:
        with open(dic1,'a+') as f1:
            with open(dic2,'r') as f2:
                f1.write('\n')
                for line in f2:#迭代的方式读取文件中的每一行
                    f1.write(line)
    except IOError:
        print("Error: 没有找到文件或读取文件失败")

def deplication(dic):
    disorder_set = set()#创建一个无序序列
    try:
        with open(newfile,'w') as outfile:
            with open(dic,'r') as f:
                for line in f:
                    if line not in disorder_set:
                        disorder_set.add(line)
                        outfile.write(line)
    except IOError:
        print("Error: 没有找到文件或读取文件失败")
    else:
        print("字典去重成功")


if __name__ == '__main__':
    merge(dicfile,addfile)
    deplication(dicfile)
