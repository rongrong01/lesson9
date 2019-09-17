'''
    作者：罗毅荣
    版本：10.0
    日期：2019年3月31日
    功能：数据过滤  及数据可视化
'''

import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    '''
        主函数
    '''
    aqi_data = pd.read_csv('China_city_aqi.csv')
    print('基本信息：')
    print(aqi_data.info())

    print('数据预览：')
    print(aqi_data.head())

    # 数据清洗
    # 只保留AQI>0的数据
    # filter_condition =aqi_data['AQI'] > 0
    # clear_aqi_data = aqi_data[filter_condition]

    clear_aqi_data = aqi_data[aqi_data['AQI'] > 0 ]


    # 统计数据
    print('AQI最大值:', clear_aqi_data['AQI'].max())
    print('AQI最小值:', clear_aqi_data['AQI'].min())
    print('AQI均值:', clear_aqi_data['AQI'].mean())

    # top 50
    top50_cities = clear_aqi_data.sort_values(by=['AQI']).head(50)
    top50_cities.plot(kind='bar',x='City',y='AQI',title='空气质量最好的50个城市',
                      figsize=(20,10))
    plt.savefig('top50_aqi_bar.png')
    plt.show()



    pass

if __name__ == '__main__':
    main()