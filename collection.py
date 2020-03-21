#! encoding = utf-8

import sys
import string
from io import StringIO
from io import open
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, process_pdf,PDFPageInterpreter

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfdevice import PDFDevice
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

def str_count(str):
    '''找出字符串中的中英文、空格、数字、标点符号个数'''
    count_en = count_dg = count_sp = count_zh = count_pu = 0
    length = len(str)
    i=0
    while i < length:

        if str[i] in string.ascii_letters:
            while (str[i] in string.ascii_letters or str[i] == "-" or (i>=1 and str[i] == "\n" and str[i-1]=="-")):
                i+=1
                if i >=len(str):
                    break
            count_en += 1
        # 数字
        elif str[i].isdigit():
            count_dg += 1
        # 空格
        elif str[i].isspace():
            count_sp += 1
        # 中文
        elif str[i].isalpha():
            count_zh += 1
        # 特殊字符
        else:
            count_pu += 1
        i+=1

    print('英文单词：', count_en)
    print('数字：', count_dg)
    print('空格：', count_sp)
    print('中文：', count_zh)
    print('特殊字符：', count_pu)
    print('全部字数（去除标点）：',count_en+count_zh)

def write2file(fileName, content):
    with open(fileName, 'w') as file_object:
        file_object.write(content)

def read_pdf(pdf,save_path):
    # resource manager
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    # device
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    process_pdf(rsrcmgr, device, pdf)
    device.close()
    content = retstr.getvalue()
    retstr.close()
    # 获取所有行
    str_count(str(content))
    lines = str(content).split("\n")
    write2file(save_path+"result.txt",str(content))
    return lines
 
 
 
if __name__ == '__main__':
    fileName = sys.argv[1]
    path = sys.argv[2]
    with open(fileName, "rb") as my_pdf:
        read_pdf(my_pdf,path)
        #parse(my_pdf,"./text")
        #pass

