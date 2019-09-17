'''
    作者：罗毅荣
    版本：4.0
    日期：2019年3月25日
    功能：判断是json文件还是csv文件

'''

import json
import csv
import os

def process_json_file(filepath):
    '''
        解码json文件
    '''
    # f = open(filepath,mode='r',encoding='UTF-8')
    # city_list = json.load(f)
    # return city_list

    with open(filepath,mode='r',encoding='UTF-8') as f:
        city_list = json.load(f)
    print(city_list)

def  process_csv_file(filepath):
    '''
        解码csv文件
    '''
    with open(filepath,mode='r',encoding='UTF-8',newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(','.join(row))



def main():
    '''
        主函数
    '''
    filepath = input('请输入文件名称')
    filename,filetxt = os.path.splitext(filepath)
    if filetxt == '.json':
        # JSON文件
        process_json_file(filepath)

    elif filetxt == '.csv':
        # CSV文件
        process_csv_file(filepath)
    else:
        print('不支持文件格式！')


    pass

if __name__ == '__main__':
    main()