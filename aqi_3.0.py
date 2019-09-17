'''
    作者：罗毅荣
    版本：3.0
    日期：2019年3月24日
    功能：CSV文件输出

'''

import json
import csv

def process_json_file(filepath):
    '''
        解码json文件
    '''
    f = open(filepath,mode='r',encoding='UTF-8')
    city_list = json.load(f)
    return city_list

def main():
    '''
        主函数
    '''
    filepath = input('请输入JSON文件名称')
    city_list = process_json_file(filepath)
    city_list.sort(key=lambda city: city['aqi'])

    lines = []
    # 列名
    lines.append(list(city_list[0].keys()))
    for city in city_list:
        lines.append(list(city.values()))

    f = open('aqi.csv','w',encoding='UTF-8',newline='')
    writer = csv.writer(f)
    for line in lines:
        writer.writerow(line)
    f.close()

    pass

if __name__ == '__main__':
    main()