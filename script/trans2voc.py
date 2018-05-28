import os
import cv2
import numpy as np
from lxml.etree import Element, SubElement, tostring, ElementTree

img_dir = "image_10000"
txt_dir = "txt_10000"
xml_dir = "xml_10000"

img_list  = os.listdir(img_dir)
img_len = len(img_list)

for i in range(img_len):
    img = cv2.imread(os.path.join(img_dir,img_list[i]))
    print(os.path.join(img_dir,img_list[i]))

    try:
        img_hgt = img.shape[0]
        img_wth = img.shape[1]
        img_dep = img.shape[2]
    except:
        continue
    
    node_root = Element('annotation')
    
    node_filename = SubElement(node_root, 'filename')
    node_filename.text = img_list[i]
    
    node_size = SubElement(node_root, 'size')
    
    node_wth  = SubElement(node_size, 'width')
    node_wth.text = str(img_wth)
    node_hgt  = SubElement(node_size, 'height')
    node_hgt.text = str(img_hgt)
    node_dep  = SubElement(node_size, 'depth')
    node_dep.text = str(img_dep)
    
    txt_name = img_list[i].rsplit('.',1)[0] + '.txt'
    #print(txt_name)
    
    for line in open(os.path.join(txt_dir,txt_name)):
        #print(line)
        
        node_obj = SubElement(node_root, 'object')
        node_name = SubElement(node_obj, 'name')
        node_name.text = "text"
        
        node_box = SubElement(node_obj, 'bndbox')
        node_dif = SubElement(node_obj, 'difficult')
        
        x1, y1, x2, y2, x3, y3, x4, y4, content = line.split(',',8)
        #print("x1 ={:s}, y1={:s}, x2={:s}, y2={:s}, x3={:s}, y3={:s}, x4={:s}, y4={:s}, content={:s}".format(x1, y1, x2, y2, x3, y3, x4, y4, content))

        if (float(x1) > float(x2) +15) or (float(x1) < float(x2) -15):
            node_dif.text = '1'
        else:
            node_dif.text = '0'

        xmin = min(float(x1),float(x2),float(x3),float(x4))
        xmax = max(float(x1),float(x2),float(x3),float(x4))
        ymin = min(float(y1),float(y2),float(y3),float(y4))
        ymax = max(float(y1),float(y2),float(y3),float(y4))
        
        if xmin<0:
            xmin = 0
        if xmax > img_wth:
            xmax = img_wth
        if ymin < 0:
            ymin = 0
        if ymax > img_hgt:
            ymax =img_hgt

        assert(xmax >= xmin)
        assert(ymax >= ymin)
        
        node_xmin = SubElement(node_box, 'xmin')
        node_xmin.text = str(xmin)
        
        node_xmax = SubElement(node_box, 'xmax')
        node_xmax.text = str(xmax)
        
        node_ymin = SubElement(node_box, 'ymin')
        node_ymin.text = str(ymin)
        
        node_ymax = SubElement(node_box, 'ymax')
        node_ymax.text = str(ymax)
        
    #xml = tostring(node_root, pretty_print=True)
    #print(xml)
    xml_name = img_list[i].rsplit('.',1)[0] + '.xml'
    tree = ElementTree(node_root)
    tree.write(os.path.join(xml_dir,xml_name))
