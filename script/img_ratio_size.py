import os
#import cv2
import numpy as np

img_dir = "image_10000"
txt_dir = "txt_10000"
xml_dir = "xml_10000"

img_list  = os.listdir(txt_dir)
img_len = len(img_list)

ratio_file = open(os.path.join(os.getcwd(),'anchor_ratio.txt'),'w')
size_file  = open(os.path.join(os.getcwd(),'anchor_size.txt'),'w')

for i in range(img_len):
    txt_file = open(os.path.join(txt_dir,img_list[i]))
    #print(os.path.join(txt_dir,img_list[i]))
    
    for line in txt_file:
        #print(line)
        
        x1, y1, x2, y2, x3, y3, x4, y4, content = line.split(',',8)
        #print('x1 ={:s}, x2={:s}, y1={:s}, y2={:s}, x3={:s}, y3={:s}, x4={:s}, y4={:s}, content={:s}'.format(x1, x2, y1, y2, x3, y3, x4, y4, content))

        x1 = float(x1)
        y1 = float(y1)
        x2 = float(x2)
        y2 = float(y2)
        x3 = float(x3)
        y3 = float(y3)
        x4 = float(x4)
        y4 = float(y4)
        
        #if (float(x1) > (float(x2) +10)) or (float(x1) > (float(x2) -10)):
        if((x1 > x2+15) or (x1 < x2-15)):
            #print('detect :x1={} ,x2={}'.format(x1,x2))
            continue #not horizontal
        
        xmin = min(float(x1),float(x2),float(x3),float(x4))
        xmax = max(float(x1),float(x2),float(x3),float(x4))
        ymin = min(float(y1),float(y2),float(y3),float(y4))
        ymax = max(float(y1),float(y2),float(y3),float(y4))
        
        if xmin<0:
            xmin = 0
        if ymin < 0:
            ymin = 0
        
        assert(xmax >= xmin)
        assert(ymax >= ymin)
        
        cur_size  = (xmax - xmin) * (ymax - ymin)
        cur_ratio = (ymax - ymin) / (xmax - xmin)
        
        size_file.write(str(cur_size)+'\n')
        ratio_file.write(str(cur_ratio)+'\n')
    
    txt_file.close()

ratio_file.close()
size_file.close()
