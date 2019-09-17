'''
    作者：罗毅荣
    版本：2.0
    日期：2019年3月24日
    功能：JSON文件输出

'''

import json

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
    top5_list = city_list[:5]

    f = open('top5_aqi.json',mode='w',encoding='UTF-8')
    json.dump(top5_list,f,ensure_ascii=False)
    f.close()

    pass

if __name__ == '__main__':
    main()