#_*_coding:utf-8_*_
#!/usr/bin/env python
'__author__' == 'Alex_XT'

import re
import os
import cv2
def countPIc(img_dir):
    img_count = 0
    imgpath_list =[]
    sub_count =0
    for root_dir,sub_dir_list,fileNamelist in os.walk(img_dir):
        for imgName in fileNamelist:
            if re.match(".*[.]jpg$",imgName):
                img_count+=1

        for sub_dir in sub_dir_list:
            sub_count+=1
    return sub_count,img_count

def renameAllPIc(img_dir,save_dir):
    for root_dir,sub_dir_list,fileNamelist in os.walk(img_dir):
        for imgName in fileNamelist:
            if re.match(".*[.]jpg$",imgName):
                img=cv2.imread(os.path.join(root_dir,imgName))
                newDirName = os.path.dirname(root_dir).split('//')[-1]
                newPicName= os.path.basename(root_dir)+imgName
                save_path=os.path.join(save_dir,newDirName)
                if not os.path.exists(save_path):
                    os.mkdir(save_path)
                print os.path.join(save_path,newPicName)
                cv2.imwrite(os.path.join(newPicName,newPicName),img)


if __name__ == '__main__':
    img_dir = r""
    sub_count, img_count=countPIc(img_dir)
    print "根目录个数+子文件个数 = ",sub_count
    print "图片个数img_count = ",img_count

    save_dir = r''
    renameAllPIc(img_dir, save_dir)
