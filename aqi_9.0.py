'''
    作者：罗毅荣
    版本：9.0
    日期：2019年3月29日
    功能：pandas
'''

import pandas as pd



def main():
    '''
        主函数
    '''
    aqi_data = pd.read_csv('China_city_aqi.csv')
    print('基本信息：')
    print(aqi_data.info())

    print('数据预览：')
    print(aqi_data.head())

    # 统计数据
    print('AQI最大值:', aqi_data['AQI'].max())
    print('AQI最小值:', aqi_data['AQI'].min())
    print('AQI均值:', aqi_data['AQI'].mean())

    # top 10
    top10_cities = aqi_data.sort_values(by=['AQI']).head(10)
    print('空气质量最好的10个城市：')
    print(top10_cities)

    # bottom 10
    # bottom10_cities = aqi_data.sort_values(by=['AQI']).tail(10)
    bottom10_cities = aqi_data.sort_values(by=['AQI'],ascending=False).head(10)
    print('空气质量最差的10个城市：')
    print(bottom10_cities)

    # 保存文件CSV
    top10_cities.to_csv('top10_aqi.csv',index=False)
    bottom10_cities.to_csv('bottom10_aqi.csv',index=False)



    pass

if __name__ == '__main__':
    main()